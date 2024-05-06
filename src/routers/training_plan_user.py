from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.training_plan_user import TrainingPlanUser
from src.models.training_plan_user import TrainingPlanUser as training_plan_users
from src.repositories.training_plan_user import TrainingPlanUserRepository

training_plan_user_router = APIRouter(prefix='/training_plan_user', tags=['training_plans_users'])

#CRUD training_plan_user

@training_plan_user_router.get('',response_model=List[TrainingPlanUser],description="Returns all training_plan_user")
def get_categories()-> List[TrainingPlanUser]:
    db= SessionLocal()
    result = TrainingPlanUserRepository(db).get_all_training_plan_users()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@training_plan_user_router.get('{id}',response_model=TrainingPlanUser,description="Returns data of one specific training_plan_user")
def get_training_plan_user(id: int = Path(ge=1)) -> TrainingPlanUser:
    db = SessionLocal()
    element=  TrainingPlanUserRepository(db).get_training_plan_user_by_id(id)
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

@training_plan_user_router.post('',response_model=dict,description="Creates a new training_plan_user")
def create_categorie(training_plan_user: TrainingPlanUser = Body()) -> dict:
    db= SessionLocal()
    new_training_plan_user = TrainingPlanUserRepository(db).create_new_training_plan_user(training_plan_user)
    return JSONResponse(
        content={        
        "message": "The training_plan_user was successfully created",        
        "data": jsonable_encoder(new_training_plan_user)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@training_plan_user_router.delete('{id}',response_model=dict,description="Removes specific training_plan_user")
def remove_training_plan_user(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = TrainingPlanUserRepository(db).delete_training_plan_user(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested training_plan_user was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)
