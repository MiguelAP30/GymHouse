from sqlalchemy import Column, ForeignKey, Integer, Float, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class QuantityFood(Base):
    __tablename__ = "quantity_foods"

    id = Column(Integer, primary_key=True, autoincrement=True)
    food_id = Column(Integer, ForeignKey("foods.id"))
    type_quantity_id = Column(Integer, ForeignKey("types_quantities.id"))
    meal_id = Column(Integer, ForeignKey("meals.id"))
    value = Column(Float)
    calorie = Column(Float)
    protein = Column(Float)
    fat = Column(Float)
    carbohydrate = Column(Float)


    foods = relationship("Food", back_populates="quantity_foods")
    types_quantities = relationship("TypeQuantity", back_populates="quantity_foods")
    meals = relationship("Meal", back_populates="quantity_foods")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}