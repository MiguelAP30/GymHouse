from typing import List
from src.schemas.exercise_muscle_machine import ExerciseMuscleMachine
from src.models.exercise_muscle_machine import ExerciseMuscleMachine as ExcersiceMuscleMachineModel



class ExerciseMuscleMachineRepository():
    def __init__(self, db) -> None:
        self.db = db

    def get_all_excercise_muscle_machine(self) -> List[ExerciseMuscleMachine]: 
        query = self.db.query(ExcersiceMuscleMachineModel)
        return query.all()

    def get_excercise_muscle_machine_by_id(self, id: int ):
        element = self.db.query(ExcersiceMuscleMachineModel).filter(ExcersiceMuscleMachineModel.id == id).first()    
        return element

    def delete_excercise_muscle_machine(self, id: int ) -> dict: 
        element: ExerciseMuscleMachine= self.db.query(ExcersiceMuscleMachineModel).filter(ExcersiceMuscleMachineModel.id == id).first()       
        self.db.delete(element)    
        self.db.commit()    
        return element

    def create_new_excercise_muscle_machine(self, excercise:ExerciseMuscleMachine ) -> dict:
        new_excercise = ExcersiceMuscleMachineModel(**excercise.model_dump())    
        
        self.db.add(new_excercise)
        self.db.commit()    
        self.db.refresh(new_excercise)
        return new_excercise

    def update_excercise_muscle_machine(self, id:int, excercise:ExerciseMuscleMachine) -> dict:
        element = self.db.query(ExcersiceMuscleMachineModel).filter(ExcersiceMuscleMachineModel.id == id).first()
        element.rate = excercise.rate

        self.db.commit()
        self.db.refresh(element)
        return element
