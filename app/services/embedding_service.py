from sentence_transformers import SentenceTransformer


class EmbeddingService:

    # Load model only once
    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    @staticmethod
    def generate_embedding(text: str):

        embedding = EmbeddingService.model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding