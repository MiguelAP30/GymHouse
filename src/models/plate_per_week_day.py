from sqlalchemy import Column, ForeignKey, Integer, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class PlatePerWeekDay(Base):
    __tablename__ = "plates_per_week_days"

    id = Column(Integer, primary_key=True, autoincrement=True)
    plate_id = Column(Integer, ForeignKey("plates.id"))
    week_day_id = Column(Integer, ForeignKey("week_days.id"))
    diet_id = Column(Integer, ForeignKey("diets.id"))

    plates = relationship("Plate", back_populates="plates_per_week_days")
    week_days = relationship("WeekDay", back_populates="plates_per_week_days")
    diets = relationship("Diet", back_populates="plates_per_week_days")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}