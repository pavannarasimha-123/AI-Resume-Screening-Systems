from sqlalchemy import create_engine, text
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("✅ Connected successfully!")
        print(result.fetchone())
except Exception as e:
    print("❌ Connection failed!")
    print(e)