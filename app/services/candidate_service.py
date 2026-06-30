class CandidateService:

    latest_results = []

    @classmethod
    def save_results(cls, matches):

        cls.latest_results = matches

    @classmethod
    def get_top_candidates(cls):

        return sorted(
            cls.latest_results,
            key=lambda x: x["score"],
            reverse=True
        )