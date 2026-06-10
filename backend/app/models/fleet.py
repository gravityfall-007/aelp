from sqlalchemy import Column, Integer, String, Float
from app.models.base import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    vehicle_type = Column(String)

    capacity = Column(Float)
    fuel_level = Column(Float)

    latitude = Column(Float)
    longitude = Column(Float)

    status = Column(String)