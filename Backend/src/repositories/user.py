from typing import List
from sqlalchemy.orm import load_only
from src.schemas.user import User
from src.models.user import User as users

class UserRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_users(self) -> List[User]:
        query = self.db.query(users)
        return query.all()
    
    def get_user_by_id(self, id: str ):
        element = self.db.query(users).filter(users.id_number == id).first()
        return element
    
    def get_user_by_email(self, email: str):
        element = (
            self.db.query(users)
            .options(load_only(users.email,users.id_number, users.user_name, users.name, users.phone, users.birth_date, users.gender, users.address))
            .filter(users.email == email)
            .first()
        )
        return element
    
    def delete_user(self, email: str ) -> dict:
        element: User= self.db.query(users).filter(users.email == email).first()
        element.status = False
        self.db.commit()
        self.db.refresh(element)
        return element

    def create_new_user(self, user:User ) -> dict:
        new_user = users(**user.model_dump())
        self.db.add(new_user)
        
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    
    def update_user(self, email: str, user: User) -> dict:
        element = self.db.query(users).filter(users.email == email).first()
        element.id_number = user.id_number
        element.password = user.password
        element.user_name = user.user_name
        element.name = user.name
        element.address = user.address
        element.phone = user.phone
        element.gender = user.gender
        element.birth_date = user.birth_date

        self.db.commit()
        self.db.refresh(element)
        return element

    def update_role(self, email: str, role_id: int) -> dict:
        element = self.db.query(users).filter(users.email == email).first()
        element.role_id = role_id
        self.db.commit()
        self.db.refresh(element)
        return element
