from app.services.embedding_service import EmbeddingService
from app.core.faiss_manager import faiss_manager
from app.services.index_service import IndexService
from app.services.skill_service import SkillService
from app.services.matching_service import MatchingService
from app.services.candidate_service import CandidateService


class RankingService:

    @staticmethod
    def rank_resumes(job_description: str):

        print("\n" + "=" * 70)
        print("🚀 AI RANKING STARTED")
        print("=" * 70)

        # Generate embedding
        job_embedding = EmbeddingService.generate_embedding(
            job_description
        )

        # Extract job skills
        job_skills = SkillService.extract_skills(
            job_description
        )

        print("\n" + "=" * 50)
        print("JOB DESCRIPTION")
        print(job_description)
        print("\nJOB SKILLS")
        print(job_skills)
        print("=" * 50)

        # Search FAISS
        distances, indices = faiss_manager.search(
            job_embedding,
            top_k=10
        )

        matches = []

        for distance, position in zip(distances, indices):

            if position == -1:
                continue

            resume = IndexService.resumes[position]

            # Extract skills from resume
            resume_skills = SkillService.extract_skills(
                resume.parsed_text
            )

            print("\n" + "=" * 50)
            print(f"RESUME ID : {resume.id}")
            print(f"FILE      : {resume.file_name}")
            print("RESUME SKILLS")
            print(resume_skills)
            print("=" * 50)

            comparison = MatchingService.compare(
                job_skills,
                resume_skills
            )

            print("MATCHED SKILLS:")
            print(comparison["matched_skills"])

            print("MISSING SKILLS:")
            print(comparison["missing_skills"])

            # Score calculation
            score = round(
                (1 / (1 + float(distance))) * 100,
                2
            )

            # Recommendation
            if score >= 80:
                recommendation = "Highly Recommended"
            elif score >= 60:
                recommendation = "Recommended"
            else:
                recommendation = "Needs Review"

            print("\nDistance:", distance)
            print("Score:", score)
            print("Recommendation:", recommendation)

            matches.append(
                {
                    "resume_id": resume.id,
                    "file_name": resume.file_name,
                    "score": score,
                    "matched_skills":
                        comparison["matched_skills"],
                    "missing_skills":
                        comparison["missing_skills"],
                    "recommendation":
                        recommendation
                }
            )

        # Sort highest score first
        matches.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        # Save for dashboard
        CandidateService.save_results(
            matches
        )

        print("\n" + "=" * 70)
        print("✅ AI RANKING COMPLETED")
        print("=" * 70)

        return {
            "matches": matches
        }