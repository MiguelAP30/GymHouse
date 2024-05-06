from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.repositories.exercise import ExerciseRepository
from src.schemas.exercise import Exercise
from src.models.exercise import Exercise as ExerciseModel

exercise_router = APIRouter(prefix='/exercise', tags=['exercises'])

#CRUD exercise

@exercise_router.get('',response_model=List[Exercise],description="Returns all exercises")
def get_categories()-> List[Exercise]:
    db= SessionLocal()
    result = ExerciseRepository(db).get_all_excercise()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@exercise_router.get('{id}',response_model=Exercise,description="Returns data of one specific exercise")
def get_excercise(id: int = Path(ge=1)) -> Exercise:
    db = SessionLocal()
    element=  ExerciseRepository(db).get_excercise_by_id(id)
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

@exercise_router.post('',response_model=dict,description="Creates a new exercise")
def create_categorie(exercise: Exercise = Body()) -> dict:
    db= SessionLocal()
    new_excercise = ExerciseRepository(db).create_new_excercise(exercise)
    return JSONResponse(
        content={        
        "message": "The exercise was successfully created",        
        "data": jsonable_encoder(new_excercise)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@exercise_router.delete('{id}',response_model=dict,description="Removes specific exercise")
def remove_excercise(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = ExerciseRepository(db).delete_excercise(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested exercise was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
        )
    return JSONResponse(
        content={        
        "message": "The exercise was successfully removed",        
        "data": jsonable_encoder(element)    
        }, 
        status_code=status.HTTP_200_OK
    )

@exercise_router.put('{id}',response_model=Exercise,description="Updates specific exercise")
def update_excercise(id: int = Path(ge=1), exercise: Exercise = Body()) -> dict:
    db = SessionLocal()
    element = ExerciseRepository(db).update_excercise(id, exercise)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested exercise was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
        )
    return JSONResponse(
        content={        
        "message": "The exercise was successfully updated",        
        "data": jsonable_encoder(element)    
        }, 
        status_code=status.HTTP_200_OK
    )
