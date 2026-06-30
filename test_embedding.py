from app.services.embedding_service import EmbeddingService

text = """
Python
FastAPI
Machine Learning
Docker
"""

embedding = EmbeddingService.generate_embedding(text)

print(type(embedding))

print(len(embedding))

print(embedding[:10])