# app/models/campaign.py
from sqlalchemy import Column, Integer, String, DateTime
from app.models.base import Base

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String)