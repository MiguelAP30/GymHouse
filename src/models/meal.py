from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, autoincrement=True)
    plates_id = Column(Integer, ForeignKey("plates.id"))
    quantity_food_id = Column(Integer, ForeignKey("quantity_foods.id"))

    plates = relationship("Plate", back_populates="meals")
    quantity_foods = relationship("QuantityFood", back_populates="meals")

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}