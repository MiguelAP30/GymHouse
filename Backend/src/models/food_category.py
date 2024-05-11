from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class FoodCategory(Base):
    __tablename__ = "food_categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=40))

    foods = relationship("Food", back_populates="food_categories")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}