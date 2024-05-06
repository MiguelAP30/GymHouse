from typing import List
from src.schemas.food import Food
from src.models.food import Food as foods

class FoodRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_foods(self) -> List[Food]:
        query = self.db.query(foods)
        return query.all()
    
    def get_food_by_id(self, id: int ):
        element = self.db.query(foods).filter(foods.id == id).first()
        return element
    
    def delete_food(self, id: int ) -> dict:
        element: Food= self.db.query(foods).filter(foods.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_food(self, food:Food ) -> dict:
        new_food = foods(**food.model_dump())
        self.db.add(new_food)
        
        self.db.commit()
        self.db.refresh(new_food)
        return new_food
    
    def update_food(self, id: int, food: Food) -> dict:
        element = self.db.query(foods).filter(foods.id == id).first()
        element.name = food.name
        element.description = food.description
        element.image = food.image

        self.db.commit()
        self.db.refresh(element)
        return element