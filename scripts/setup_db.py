# scripts/setup_db.py
from sqlalchemy import create_engine
from app.models.base import Base
from app.core.config import settings

def setup_database():
    engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    setup_database()
