# app/api/endpoints/analytics.py
from fastapi import APIRouter, Depends
from app.services.analytics.performance_tracker import PerformanceTracker
from app.services.analytics.cac_calculator import CACCalculator

router = APIRouter()

@router.get("/{campaign_id}")
def get_analytics(campaign_id: int):
    performance = PerformanceTracker().track_campaign(campaign_id)
    cac = CACCalculator().calculate(campaign_id)
    return {"performance": performance, "cac": cac}

