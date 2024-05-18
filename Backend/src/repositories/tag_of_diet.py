from typing import List
from src.schemas.tag_of_diet import TagOfDiet
from src.models.tag_of_diet import TagOfDiet as tag_of_diets

class TagOfDietRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_tag_of_diets(self) -> List[TagOfDiet]:
        query = self.db.query(tag_of_diets)
        return query.all()
    
    def get_tag_of_diet_by_id(self, id: int ):
        element = self.db.query(tag_of_diets).filter(tag_of_diets.id == id).first()
        return element
    
    def delete_tag_of_diet(self, id: int ) -> dict:
        element: TagOfDiet= self.db.query(tag_of_diets).filter(tag_of_diets.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_tag_of_diet(self, tag_of_diet:TagOfDiet ) -> dict:
        new_tag_of_diet = tag_of_diets(**tag_of_diet.model_dump())
        self.db.add(new_tag_of_diet)
        
        self.db.commit()
        self.db.refresh(new_tag_of_diet)
        return new_tag_of_diet
    
    def update_tag_of_diet(self, id: int, tag_of_diet: TagOfDiet) -> dict:    
        element = self.db.query(tag_of_diets).filter(tag_of_diets.id == id).first()
        element.name = tag_of_diet.name

        self.db.commit()
        self.db.refresh(element)
        return element