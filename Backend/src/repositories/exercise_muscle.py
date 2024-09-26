from typing import List

from sqlalchemy import desc
from src.schemas.exercise_muscle import ExerciseMuscle
from src.models.exercise_muscle import ExerciseMuscle as ExcersiceMuscleModel
from src.models.muscle import Muscle as MuscleModel
from src.models.machine import Machine as MachineModel



class ExerciseMuscleRepository():
    def __init__(self, db) -> None:
        self.db = db
    
    def get_all_excercise_muscle_by_rate(self) -> List[ExerciseMuscle]:
        query = self.db.query(ExcersiceMuscleModel).order_by(desc(ExcersiceMuscleModel.rate))
        return query.all()
    
    def get_all_excercise_muscle_machine_by_rate(self) -> List[ExerciseMuscle]:
        query = self.db.query(ExcersiceMuscleModel).order_by(desc(ExcersiceMuscleModel.rate))
        return query.all()
    
    def get_excercise_muscle_machine_by_id(self, id: int ):
        element = self.db.query(ExcersiceMuscleModel).filter(ExcersiceMuscleModel.id == id).first()
        return element
    
    def create_new_excercise_muscle_machine(self, excercise_muscle:ExerciseMuscle ) -> dict:
        new_excercise_muscle = ExcersiceMuscleModel(**excercise_muscle.model_dump())
        self.db.add(new_excercise_muscle)

        self.db.commit()
        self.db.refresh(new_excercise_muscle)
        return new_excercise_muscle
    
    def delete_excercise_muscle_machine(self, id: int ) -> dict:
        element: ExerciseMuscle= self.db.query(ExcersiceMuscleModel).filter(ExcersiceMuscleModel.id == id).first()
        self.db.delete(element)
        self.db.commit()
        return element
    
    def update_rate_excercise_muscle_machine(self, id:int, rate:int) -> dict:
        element = self.db.query(ExcersiceMuscleModel).filter(ExcersiceMuscleModel.id == id).first()
        element.rate = rate
        self.db.commit()
        self.db.refresh(element)
        return element
    
    