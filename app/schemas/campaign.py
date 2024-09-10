# app/schemas/campaign.py
from pydantic import BaseModel
from datetime import datetime

class CampaignBase(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime

class CampaignCreate(CampaignBase):
    pass

class Campaign(CampaignBase):
    id: int
    status: str

    class Config:
        orm_mode = True