import datetime
from sqlalchemy import Column, DateTime, Float, Integer, String

from smart_plant.db import Base


class Actions(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    actor = Column(String, nullable=False)
    action = Column(String, nullable=False)
    dt = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))


class Pump(Base):
    __tablename__ = "pump"

    id = Column(Integer, primary_key=True, autoincrement=True)
    start = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    stop = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    duration = Column(Integer, default=0)

    def __repr__(self):
        return f"<Pump(id={self.id}, status={self.status}, last_action={self.last_action})>"
    
class MoistureSensorData(Base):
    __tablename__ = "moisture_sensor_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    moisture_level = Column(Integer, nullable=False)
    moisture_percentage = Column(Float, nullable=False)

    def __repr__(self):
        return f"<MoistureSensorData(id={self.id}, timestamp={self.timestamp}, moisture_level={self.moisture_level})>"