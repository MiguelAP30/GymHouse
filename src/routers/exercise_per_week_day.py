from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.repositories.exercise_per_week_day import ExercisePerWeekDayRepository
from src.schemas.exercise_per_week_day import ExercisePerWeekDay
from src.models.exercise_per_week_day import ExercisePerWeekDay as ExercisePerWeekDayModel

exercise_per_week_day_router = APIRouter(prefix='/exercise_per_week_day', tags=['exercises_per_week_days'])

#CRUD exercise_per_week_day

@exercise_per_week_day_router.get('',response_model=List[ExercisePerWeekDay],description="Returns all exercise_per_week_day")
def get_categories()-> List[ExercisePerWeekDay]:
    db= SessionLocal()
    result = ExercisePerWeekDayRepository(db).get_all_excercise_per_week_day()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@exercise_per_week_day_router.get('{id}',response_model=ExercisePerWeekDay,description="Returns data of one specific exercise_per_week_day")
def get_excercise_per_week_day(id: int = Path(ge=1)) -> ExercisePerWeekDay:
    db = SessionLocal()
    element=  ExercisePerWeekDayRepository(db).get_excercise_per_week_day_by_id(id)
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

@exercise_per_week_day_router.post('',response_model=dict,description="Creates a new exercise_per_week_day")
def create_categorie(exercise: ExercisePerWeekDay = Body()) -> dict:
    db= SessionLocal()
    new_excercise = ExercisePerWeekDayRepository(db).create_new_excercise_per_week_day(exercise)
    return JSONResponse(
        content={        
        "message": "The exercise_per_week_day was successfully created",        
        "data": jsonable_encoder(new_excercise)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@exercise_per_week_day_router.delete('{id}',response_model=dict,description="Removes specific exercise_per_week_day")
def remove_excercise_per_week_day(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = ExercisePerWeekDayRepository(db).delete_excercise_per_week_day(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested exercise_per_week_day was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content={        
            "message": "The exercise_per_week_day was successfully removed",        
            "data": jsonable_encoder(element)    
        }, 
        status_code=status.HTTP_200_OK
    )

