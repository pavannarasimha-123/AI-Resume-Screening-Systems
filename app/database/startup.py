from app.database.database import SessionLocal
from app.services.index_service import IndexService


def build_faiss():

    db = SessionLocal()

    try:

        IndexService.build_index(db)

    finally:

        db.close()