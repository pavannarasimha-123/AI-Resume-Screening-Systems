class SummaryService:

    @staticmethod
    def generate_summary(
        matched_skills,
        missing_skills
    ):

        if len(matched_skills) >= 4:

            recommendation = (
                "Shortlist for Interview"
            )

        elif len(matched_skills) >= 2:

            recommendation = (
                "Consider for Interview"
            )

        else:

            recommendation = (
                "Needs Further Review"
            )

        strengths = matched_skills[:5]

        summary = (
            f"Candidate demonstrates experience in "
            f"{', '.join(matched_skills)}."
        )

        if missing_skills:

            summary += (
                f" Missing skills include "
                f"{', '.join(missing_skills)}."
            )

        return {

            "summary": summary,

            "strengths": strengths,

            "recommendation":
                recommendation
        }