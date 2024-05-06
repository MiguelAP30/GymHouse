from typing import List
from src.schemas.food_category import FoodCategory
from src.models.food_category import FoodCategory as FoodCategoryModel

class FoodCategoryRepository:
    def __init__(self, db):
        self.db = db

    def get_all_food_categories(self):
        return self.db.query(FoodCategoryModel).all()

    def get_food_category_by_id(self, id):
        return self.db.query(FoodCategoryModel).filter(FoodCategoryModel.id == id).first()

    def create_new_food_category(self, food_category: FoodCategory):
        new_food_category = FoodCategoryModel(**food_category.model_dump())

        self.db.add(new_food_category)
        self.db.commit()
        self.db.refresh(new_food_category)
        return new_food_category

    def delete_food_category(self, id):
        element = self.db.query(FoodCategoryModel).filter(FoodCategoryModel.id == id).first()

        self.db.delete(element)
        self.db.commit()
        return element
    
    def update_food_category(self, id: int, food_category: FoodCategory) -> dict:
        element = self.db.query(FoodCategoryModel).filter(FoodCategoryModel.id == id).first()
        element.name = food_category.name

        self.db.commit()
        self.db.refresh(element)
        return element
