from typing import List
from src.schemas.training_plan import TrainingPlan
from src.models.training_plan import TrainingPlan as training_plans
from src.models.training_plan_user import TrainingPlanUser as training_plan_user

class TrainingPlanRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_training_plans(self, user: str) -> List[TrainingPlan]:
        query = self.db.query(training_plans).join(training_plan_user).filter(training_plan_user.user_email == user)
        return query.all()
    
    def get_training_plan_by_id(self, id: int, user: str):
        element = self.db.query(training_plans).join(training_plan_user).filter(training_plans.id == id, training_plan_user.user_email == user).first()
        return element
    
    def delete_training_plan(self, id: int, user: str) -> dict:
        element = self.db.query(training_plans).join(training_plan_user).filter(training_plans.id == id, training_plan_user.user_email == user).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_training_plan(self, training_plan:TrainingPlan ) -> dict:
        new_training_plan = training_plans(**training_plan.model_dump())
        self.db.add(new_training_plan)
        self.db.commit()
        self.db.refresh(new_training_plan)
        return new_training_plan

    def update_training_plan(self, id: int, training_plan: TrainingPlan, user: str) -> dict:    
        element = self.db.query(training_plans).join(training_plan_user).filter(training_plans.id == id, training_plan_user.user_email == user).first()
        element.name = training_plan.name
        element.description = training_plan.description

        self.db.commit()
        self.db.refresh(element)
        return element