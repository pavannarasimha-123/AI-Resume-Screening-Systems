from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Resume(Base):
    __tablename__ = "resumes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    file_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    file_path: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    # Extracted text from the uploaded PDF
    parsed_text: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    uploaded_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    # Relationship with User
    user: Mapped["User"] = relationship(
        "User",
        back_populates="resumes"
    )

    def __repr__(self):
        return (
            f"<Resume(id={self.id}, "
            f"file_name='{self.file_name}', "
            f"user_id={self.user_id})>"
        )