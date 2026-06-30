import os
import shutil
import uuid

from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.utils.pdf_parser import extract_text
from app.services.embedding_service import EmbeddingService
from app.core.faiss_manager import faiss_manager

UPLOAD_FOLDER = "uploads"


class ResumeService:

    @staticmethod
    def save_resume(db: Session, file, user_id: int):

        print("\n" + "=" * 70)
        print("🚀 ResumeService.save_resume() called")
        print("=" * 70)

        # Create uploads folder if it doesn't exist
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        # Generate unique filename
        unique_filename = f"{uuid.uuid4()}_{file.filename}"

        file_path = os.path.join(
            UPLOAD_FOLDER,
            unique_filename
        )

        print(f"📄 Original File : {file.filename}")
        print(f"📁 Saved Path    : {file_path}")

        # Save PDF
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print("✅ PDF saved successfully")

        # Extract text
        print("\n📖 Extracting text from PDF...")

        parsed_text = extract_text(file_path)

        print("✅ Text extracted")
        print(f"Characters extracted : {len(parsed_text)}")

        # Save to PostgreSQL
        print("\n💾 Saving resume to PostgreSQL...")

        resume = Resume(
            file_name=file.filename,
            file_path=file_path,
            parsed_text=parsed_text,
            user_id=user_id
        )

        db.add(resume)
        db.commit()
        db.refresh(resume)

        print(f"✅ Resume saved with ID : {resume.id}")

        # -----------------------------
        # AI Pipeline
        # -----------------------------
        try:

            print("\n🤖 AI PIPELINE STARTED")

            print("Step 1 → Generating embedding...")

            embedding = EmbeddingService.generate_embedding(
                parsed_text
            )

            print("✅ Embedding generated")
            print(f"Embedding Dimension : {len(embedding)}")

            print("Step 2 → Adding embedding to FAISS...")

            faiss_manager.add_embedding(
                resume.id,
                embedding
            )

            print("✅ Added to FAISS successfully")

        except Exception as e:

            print("\n❌ AI PIPELINE FAILED")
            print(type(e).__name__)
            print(e)

        print("=" * 70)
        print("🎉 Resume upload completed successfully")
        print("=" * 70 + "\n")

        return resume