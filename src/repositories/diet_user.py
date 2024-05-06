from typing import List
from src.schemas.diet_user import DietUser
from src.models.diet_user import DietUser as diet_users

class DietUserRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_diet_user(self) -> List[DietUser]:
        query = self.db.query(diet_users)
        return query.all()
    
    def get_diet_user_by_id(self, id: int ):
        element = self.db.query(diet_users).filter(diet_users.id == id).first()
        return element
    
    def delete_diet_user(self, id: int ) -> dict:
        element: DietUser= self.db.query(diet_users).filter(diet_users.id == id).first()
        self.db.delete(element)

        self.db.commit()
        self.db.refresh(element)
        return element

    def create_new_diet_user(self, diet_user:DietUser ) -> dict:
        new_diet_user = diet_users(**diet_user.model_dump())
        self.db.add(new_diet_user)
        
        self.db.commit()
        self.db.refresh(new_diet_user)
        return new_diet_user
    