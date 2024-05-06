from typing import List
from src.schemas.diet import Diet
from src.models.diet import Diet as diets

class DietRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_diets(self) -> List[Diet]:
        query = self.db.query(diets)
        return query.all()
    
    def get_diet_by_id(self, id: int ):
        element = self.db.query(diets).filter(diets.id == id).first()
        return element
    
    def delete_diet(self, id: int ) -> dict:
        element: Diet= self.db.query(diets).filter(diets.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_diet(self, diet:Diet ) -> dict:
        new_diet = diets(**diet.model_dump())
        self.db.add(new_diet)
        self.db.commit()
        self.db.refresh(new_diet)
        return new_diet
    
    def update_diet(self, id: int, diet: Diet) -> dict:
        element = self.db.query(diets).filter(diets.id == id).first()
        element.name = diet.name
        element.description = diet.description
        self.db.commit()
        return element