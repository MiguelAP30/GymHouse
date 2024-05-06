from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.training_plan_exercise import TrainingPlanExercise
from src.models.training_plan_exercise import TrainingPlanExercise as training_plan_exercises
from src.repositories.training_plan_exercise import TrainingPlanExerciseRepository

training_plan_exercise_router = APIRouter(tags=['Ejercicios para planes de entrenamiento'])

#CRUD training_plan_exercise

@training_plan_exercise_router.get('/',response_model=List[TrainingPlanExercise],description="Returns all training_plan_exercise")
def get_categories()-> List[TrainingPlanExercise]:
    db= SessionLocal()
    result = TrainingPlanExerciseRepository(db).get_all_training_plan_exercises()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@training_plan_exercise_router.get('/{id}',response_model=TrainingPlanExercise,description="Returns data of one specific training_plan_exercise")
def get_training_plan_exercise(id: int = Path(ge=1)) -> TrainingPlanExercise:
    db = SessionLocal()
    element=  TrainingPlanExerciseRepository(db).get_training_plan_exercise_by_id(id)
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

@training_plan_exercise_router.post('/',response_model=dict,description="Creates a new training_plan_exercise")
def create_categorie(training_plan_exercise: TrainingPlanExercise = Body()) -> dict:
    db= SessionLocal()
    new_training_plan_exercise = TrainingPlanExerciseRepository(db).create_new_training_plan_exercise(training_plan_exercise)
    return JSONResponse(
        content={        
        "message": "The training_plan_exercise was successfully created",        
        "data": jsonable_encoder(new_training_plan_exercise)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@training_plan_exercise_router.delete('/{id}',response_model=dict,description="Removes specific training_plan_exercise")
def remove_training_plan_exercise(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = TrainingPlanExerciseRepository(db).delete_training_plan_exercise(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested training_plan_exercise was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
        )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)
