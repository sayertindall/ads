
# app/models/analytics.py
from sqlalchemy import Column, Integer, Float, ForeignKey
from app.models.base import Base

class Analytics(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)
    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    impressions = Column(Integer)
    clicks = Column(Integer)
    conversions = Column(Integer)
    ctr = Column(Float)
    cac = Column(Float)