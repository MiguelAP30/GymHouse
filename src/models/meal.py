from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity_food_id = Column(Integer, ForeignKey("quantity_foods.id"))
    name = Column(String(length=50))
    description = Column(String(length=200))

    quantity_foods = relationship("QuantityFood", back_populates="meals")
    diets_meals = relationship("DietMeal", back_populates="meals")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}