from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.repositories.exercise_muscle_machine import ExerciseMuscleMachineRepository
from src.schemas.exercise_muscle_machine import ExerciseMuscleMachine
from src.models.exercise_muscle_machine import ExerciseMuscleMachine as ExcersiceMuscleMachineModel

exercise_muscle_machine_router = APIRouter(tags=['Máquina para hacer ejercicio por músculo'])

#CRUD exercise_muscle_machine

@exercise_muscle_machine_router.get('/',response_model=List[ExerciseMuscleMachine],description="Returns all exercise_muscle_machine")
def get_categories()-> List[ExerciseMuscleMachine]:
    db= SessionLocal()
    result = ExerciseMuscleMachineRepository(db).get_all_excercise_muscle_machine()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@exercise_muscle_machine_router.get('/{id}',response_model=ExerciseMuscleMachine,description="Returns data of one specific exercise_muscle_machine")
def get_excercise_muscle_machine(id: int = Path(ge=1)) -> ExerciseMuscleMachine:
    db = SessionLocal()
    element=  ExerciseMuscleMachineRepository(db).get_excercise_muscle_machine_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested income was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content=jsonable_encoder(element),                        
        status_code=status.HTTP_200_OK
        )

@exercise_muscle_machine_router.post('/',response_model=dict,description="Creates a new exercise_muscle_machine")
def create_categorie(exercise: ExerciseMuscleMachine = Body()) -> dict:
    db= SessionLocal()
    new_excercise = ExerciseMuscleMachineRepository(db).create_new_excercise_muscle_machine(exercise)
    return JSONResponse(
        content={        
        "message": "The exercise_muscle_machine was successfully created",        
        "data": jsonable_encoder(new_excercise)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@exercise_muscle_machine_router.delete('/{id}',response_model=dict,description="Removes specific exercise_muscle_machine")
def remove_excercise_muscle_machine(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = ExerciseMuscleMachineRepository(db).delete_excercise_muscle_machine(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested exercise_muscle_machine was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content={        
        "message": "The exercise_muscle_machine was successfully removed",        
        "data": jsonable_encoder(element)    
        }, 
        status_code=status.HTTP_200_OK
    )

@exercise_muscle_machine_router.put('/{id}',response_model=dict,description="Updates specific exercise_muscle_machine")
def update_excercise_muscle_machine(id: int = Path(ge=1), exercise: ExerciseMuscleMachine = Body()) -> dict:
    db = SessionLocal()
    element = ExerciseMuscleMachineRepository(db).update_excercise_muscle_machine(id, exercise)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested exercise_muscle_machine was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content={        
        "message": "The exercise_muscle_machine was successfully updated",        
        "data": jsonable_encoder(element)    
        }, 
        status_code=status.HTTP_200_OK
    )
