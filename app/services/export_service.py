import pandas as pd

from app.services.candidate_service import CandidateService


class ExportService:

    @staticmethod
    def export_csv():

        candidates = CandidateService.get_top_candidates()

        if not candidates:
            return None

        df = pd.DataFrame(candidates)

        file_name = "candidate_ranking.csv"

        df.to_csv(
            file_name,
            index=False
        )

        return file_name