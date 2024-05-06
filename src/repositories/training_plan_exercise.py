from typing import List
from schemas.training_plan_exercise import TrainingPlanExercise
from models.training_plan_exercise import TrainingPlanExercise as training_plan_excersices

class TrainingPlanExerciseRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_training_plan_exercises(self) -> List[TrainingPlanExercise]:
        query = self.db.query(training_plan_excersices)
        return query.all()
    
    def get_training_plan_exercise_by_id(self, id: int ):
        element = self.db.query(training_plan_excersices).filter(training_plan_excersices.id == id).first()
        return element
    
    def delete_training_plan_exercise(self, id: int ) -> dict:
        element: TrainingPlanExercise= self.db.query(training_plan_excersices).filter(training_plan_excersices.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element

    def create_new_training_plan_exercise(self, training_plan_exercise:TrainingPlanExercise ) -> dict:
        new_training_plan_exercise = training_plan_excersices(**training_plan_exercise.model_dump())
        self.db.add(new_training_plan_exercise)
        
        self.db.commit()
        self.db.refresh(new_training_plan_exercise)
        return new_training_plan_exercise
    
