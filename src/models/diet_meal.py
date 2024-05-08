from sqlalchemy import Column, ForeignKey, Integer, String, inspect
from sqlalchemy.orm import relationship
from src.config.database import Base

class DietMeal(Base):
    __tablename__ = 'diets_meals'

    id = Column(Integer, primary_key=True, index=True)
    diet_id = Column(Integer, ForeignKey('diets.id'))
    meal_id = Column(Integer, ForeignKey('meals.id'))

    diets = relationship('Diet', back_populates='diets_meals')
    meals = relationship('Meal', back_populates='diets_meals')
    plates_per_week_days = relationship('PlatePerWeekDay', back_populates='diets_meals')

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
