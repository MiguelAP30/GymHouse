from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class Diet(Base):
    __tablename__ = "diets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=50))
    description = Column(String(length=200))

    diets_users = relationship("DietUser", back_populates="diets")
    diet_meals = relationship("DietMeal", back_populates="diets")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}