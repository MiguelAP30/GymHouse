from typing import List
from src.models.diet_meal import DietMeal
from src.schemas.diet_meal import DietMeal as DietMealModel

class DietMealRepository:
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_diet_meal(self) -> List[DietMealModel]:
        query = self.db.query(DietMeal)
        return query.all()
    
    def get_diet_meal_by_id(self, id: int ):
        element = self.db.query(DietMeal).filter(DietMeal.id == id).first()
        return element
    
    def delete_diet_meal(self, id: int ) -> dict:
        element: DietMeal= self.db.query(DietMeal).filter(DietMeal.id == id).first()
        self.db.delete(element)

        self.db.commit()
        self.db.refresh(element)
        return element
    
    def create_new_diet_meal(self, diet_meal:DietMealModel ) -> dict:
        new_diet_meal = DietMeal(**diet_meal.model_dump())
        self.db.add(new_diet_meal)
        
        self.db.commit()
        self.db.refresh(new_diet_meal)
        return new_diet_meal
    