from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class ResumeEmbedding(Base):
    __tablename__ = "resume_embeddings"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    resume_id: Mapped[int] = mapped_column(
        ForeignKey("resumes.id", ondelete="CASCADE"),
        nullable=False,
        unique=True
    )

    faiss_position: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        unique=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )