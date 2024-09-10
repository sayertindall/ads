# tests/test_models.py
from sqlalchemy.orm import Session
from app.models.user import User

def test_create_user(db: Session):
    user = User(email="test@example.com", hashed_password="testpass")
    db.add(user)
    db.commit()
    assert user.id is not None