from typing import List
from schemas.detailed_exercise import DetailedExercise
from models.detailed_exercise import DetailedExercise as detailed_exercises

class DetailedExerciseRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_detailed_exercise(self) -> List[DetailedExercise]:
        query = self.db.query(detailed_exercises)
        return query.all()
    
    def get_detailed_exercise_by_id(self, id: int ):
        element = self.db.query(detailed_exercises).filter(detailed_exercises.id == id).first()
        return element
    
    def delete_detailed_exercise(self, id: int ) -> dict:
        element: DetailedExercise= self.db.query(detailed_exercises).filter(detailed_exercises.id == id).first()
        self.db.delete(element)

        self.db.commit()
        self.db.refresh(element)
        return element

    def create_new_detailed_exercise(self, detailed_exercise:DetailedExercise ) -> dict:
        new_detailed_exercise = detailed_exercises(**detailed_exercise.model_dump())
        self.db.add(new_detailed_exercise)
        
        self.db.commit()
        self.db.refresh(new_detailed_exercise)
        return new_detailed_exercise

    def update_detailed_exercise(self, id: int, detailed_exercise: DetailedExercise) -> dict:
        element: DetailedExercise = self.db.query(detailed_exercises).filter(detailed_exercises.id == id).first()
        element.sets = detailed_exercise.sets
        element.reps = detailed_exercise.reps
        element.rest = detailed_exercise.rest

        self.db.commit()
        self.db.refresh(element)
        return element
