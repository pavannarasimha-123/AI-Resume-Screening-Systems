from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.services.embedding_service import EmbeddingService
from app.core.faiss_manager import faiss_manager


class IndexService:

    resumes = []

    @classmethod
    def build_index(cls, db: Session):

        print("\n" + "=" * 70)
        print("🚀 BUILDING FAISS INDEX")
        print("=" * 70)

        faiss_manager.clear()

        cls.resumes = db.query(Resume).order_by(Resume.id).all()

        print(f"Found {len(cls.resumes)} resumes")

        for resume in cls.resumes:

            if not resume.parsed_text:
             print(f"Skipping Resume {resume.id} (No parsed text)")
             continue

            embedding = EmbeddingService.generate_embedding(
                resume.parsed_text
            )

            faiss_manager.add_embedding(
                embedding
            )

            print(f"Indexed Resume {resume.id}")

        print("=" * 70)
        print("✅ FAISS READY")
        print("=" * 70)