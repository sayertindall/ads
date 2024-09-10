# app/schemas/analytics.py
from pydantic import BaseModel

class AnalyticsBase(BaseModel):
    campaign_id: int
    impressions: int
    clicks: int
    conversions: int
    ctr: float
    cac: float

class AnalyticsCreate(AnalyticsBase):
    pass

class Analytics(AnalyticsBase):
    id: int

    class Config:
        orm_mode = True