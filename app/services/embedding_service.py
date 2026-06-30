from sentence_transformers import SentenceTransformer


class EmbeddingService:

    model = None

    @classmethod
    def get_model(cls):

        if cls.model is None:

            print("====================================")
            print("Loading AI Embedding Model...")
            print("====================================")

            cls.model = SentenceTransformer(
                "all-MiniLM-L6-v2"
            )

            print("====================================")
            print("Model Loaded Successfully")
            print("====================================")

        return cls.model

    @staticmethod
    def generate_embedding(text: str):

        model = EmbeddingService.get_model()

        embedding = model.encode(
            text,
            convert_to_numpy=True
        )

        return embedding