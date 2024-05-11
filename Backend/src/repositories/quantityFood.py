from typing import List
from src.schemas.quantityFood import QuantityFood
from src.models.quantityFood import QuantityFood as quantity_foods

class QuantityFoodRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_quantity_foods(self) -> List[QuantityFood]:
        query = self.db.query(quantity_foods)
        return query.all()
    
    def get_quantity_food_by_id(self, id: int ):
        element = self.db.query(quantity_foods).filter(quantity_foods.id == id).first()
        return element
    
    def delete_quantity_food(self, id: int ) -> dict:
        element: QuantityFood= self.db.query(quantity_foods).filter(quantity_foods.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_quantity_food(self, quantity_food:QuantityFood ) -> dict:
        new_quantity_food = quantity_foods(**quantity_food.model_dump())
        self.db.add(new_quantity_food)
        
        self.db.commit()
        self.db.refresh(new_quantity_food)
        return new_quantity_food
    
    def update_quantity_food(self, id: int, quantity_food: QuantityFood) -> dict:
        element = self.db.query(quantity_foods).filter(quantity_foods.id == id).first()
        element.value = quantity_food.value
        element.calorie = quantity_food.calorie
        element.protein = quantity_food.protein
        element.carbohydrate = quantity_food.carbohydrate
        element.fat = quantity_food.fat


        self.db.commit()
        self.db.refresh(element)
        return element