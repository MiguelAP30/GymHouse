from typing import List
from src.schemas.training_plan_user import TrainingPlanUser
from src.models.training_plan_user import TrainingPlanUser as training_plan_users

class TrainingPlanUserRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_training_plan_users(self, user: str) -> List[TrainingPlanUser]:
        query = self.db.query(training_plan_users).filter(training_plan_users.user_email == user)
        return query.all()
    
    def get_training_plan_user_by_id(self, id: int, user: str):
        element = self.db.query(training_plan_users).filter(training_plan_users.id == id, training_plan_users.user_email == user).first()
        return element
    
    def delete_training_plan_user(self, id: int, user: str) -> dict:
        element: TrainingPlanUser= self.db.query(training_plan_users).filter(training_plan_users.id == id, training_plan_users.user_email == user).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_training_plan_user(self, training_plan_user:TrainingPlanUser ) -> dict:
        new_training_plan_user = training_plan_users(**training_plan_user.model_dump())
        self.db.add(new_training_plan_user)
        self.db.commit()
        self.db.refresh(new_training_plan_user)
        return new_training_plan_user