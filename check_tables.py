from sqlalchemy import create_engine, text
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:

    print("Connected Successfully\n")

    result = conn.execute(text("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema='public'
        ORDER BY table_name
    """))

    tables = result.fetchall()

    print("Tables:")
    for table in tables:
        print(table[0])