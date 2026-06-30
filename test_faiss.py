from app.services.embedding_service import EmbeddingService
from app.services.faiss_service import FAISSService

faiss_service = FAISSService()

resume1 = """
Python
Machine Learning
FastAPI
"""

resume2 = """
Java
Spring Boot
MySQL
"""

resume3 = """
Data Science
TensorFlow
Deep Learning
"""

e1 = EmbeddingService.generate_embedding(resume1)
e2 = EmbeddingService.generate_embedding(resume2)
e3 = EmbeddingService.generate_embedding(resume3)

faiss_service.add_embedding(1, e1)
faiss_service.add_embedding(2, e2)
faiss_service.add_embedding(3, e3)

job = """
Python
FastAPI
Docker
"""

job_embedding = EmbeddingService.generate_embedding(job)

results = faiss_service.search(job_embedding)

print(results)