from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class Plate(Base):
    __tablename__ = "plates"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50))
    description = Column(String(length=200))

    plates_per_week_days = relationship("PlatePerWeekDay", back_populates="plates")
    meals = relationship("Meal", back_populates="plates")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}