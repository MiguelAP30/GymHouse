from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class Diet(Base):
    __tablename__ = "diets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50))
    description = Column(String(length=200))
    plate_per_week_day_id = Column(Integer, ForeignKey("plates_per_week_days.id"))

    diets_users = relationship("DietUser", back_populates="diets")
    plates_per_week_days = relationship("PlatePerWeekDay", back_populates="diets")
    tags_of_diets = relationship("TagOfDiet", back_populates="diets")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}