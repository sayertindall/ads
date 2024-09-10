# app/api/endpoints/users.py
from fastapi import APIRouter, Depends
from app.core.deps import get_current_user
from app.schemas.user import User

router = APIRouter()

@router.get("/me", response_model=User)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
