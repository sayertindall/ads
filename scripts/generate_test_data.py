# scripts/generate_test_data.py
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User

def generate_test_data():
    db = SessionLocal()
    test_user = User(email="test@example.com", hashed_password="testpass")
    db.add(test_user)
    db.commit()
    db.close()

if __name__ == "__main__":
    generate_test_data()