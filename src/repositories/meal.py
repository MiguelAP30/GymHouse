from typing import List
from src.schemas.meal import Meal
from src.models.meal import Meal as meals

class MealRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_meals(self) -> List[Meal]:
        query = self.db.query(meals)
        return query.all()
    
    def get_meal_by_id(self, id: int ):
        element = self.db.query(meals).filter(meals.id == id).first()
        return element
    
    def delete_meal(self, id: int ) -> dict:
        element: Meal= self.db.query(meals).filter(meals.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_meal(self, meal:Meal ) -> dict:
        new_meal = meals(**meal.model_dump())
        self.db.add(new_meal)
        
        self.db.commit()
        self.db.refresh(new_meal)
        return new_meal
    