from typing import List
from schemas.detailed_exercise import TrainingPlanExercise
from models.detailed_exercise import DetailedExercise as detailed_exercises_Model

class DetailedExerciseRepository:
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_details_exercises(self) -> List[detailed_exercises_Model]:
        query = self.db.query(detailed_exercises_Model)
        return query.all()
    
    def get_details_exercise_by_id(self, id: int ) -> detailed_exercises_Model:
        element = self.db.query(detailed_exercises_Model).filter(detailed_exercises_Model.id == id).first()
        return element
    
    def delete_details_exercise_by_id(self, id: int ) -> detailed_exercises_Model:
        element: TrainingPlanExercise= self.db.query(detailed_exercises_Model).filter(detailed_exercises_Model.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_training_plan_exercise(self, training_plan_exercise:TrainingPlanExercise ) -> dict:
        new_training_plan_exercise = detailed_exercises_Model(**training_plan_exercise.model_dump())
        self.db.add(new_training_plan_exercise)
        
        self.db.commit()
        self.db.refresh(new_training_plan_exercise)
        return new_training_plan_exercise
    
    def update_training_plan_exercise(self, id:int, training_plan_exercise:TrainingPlanExercise ) -> dict:
        element = self.db.query(detailed_exercises_Model).filter(detailed_exercises_Model.id == id).first()
        element.sets = training_plan_exercise.sets
        element.reps = training_plan_exercise.reps
        element.rest = training_plan_exercise.rest

        self.db.commit()
        self.db.refresh(element)
        return element
