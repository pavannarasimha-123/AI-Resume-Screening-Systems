from collections import Counter

from app.services.candidate_service import CandidateService


class DashboardService:

    @staticmethod
    def get_stats():

        candidates = CandidateService.get_top_candidates()

        total_resumes = len(candidates)

        highly_recommended = 0
        recommended = 0
        needs_review = 0

        skills_counter = Counter()

        for candidate in candidates:

            recommendation = candidate.get(
                "recommendation",
                ""
            )

            if recommendation == "Highly Recommended":
                highly_recommended += 1

            elif recommendation == "Recommended":
                recommended += 1

            else:
                needs_review += 1

            for skill in candidate.get(
                "matched_skills",
                []
            ):
                skills_counter[skill] += 1

        top_skill = "N/A"

        if skills_counter:
            top_skill = skills_counter.most_common(
                1
            )[0][0]

        return {
            "total_resumes": total_resumes,
            "highly_recommended": highly_recommended,
            "recommended": recommended,
            "needs_review": needs_review,
            "top_skill": top_skill
        }