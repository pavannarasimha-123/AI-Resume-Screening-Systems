class MatchingService:

    @staticmethod
    def compare(job_skills, resume_skills):

        job = set(job_skills)

        resume = set(resume_skills)

        matched = sorted(job & resume)

        missing = sorted(job - resume)

        extra = sorted(resume - job)

        return {

            "matched_skills": matched,

            "missing_skills": missing,

            "extra_skills": extra
        }