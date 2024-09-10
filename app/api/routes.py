# app/api/routes.py
from fastapi import APIRouter
from app.api.endpoints import campaigns, analytics, users

router = APIRouter()

router.include_router(campaigns.router, prefix="/campaigns", tags=["campaigns"])
router.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
router.include_router(users.router, prefix="/users", tags=["users"])
