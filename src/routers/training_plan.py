from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.training_plan import TrainingPlan
from src.models.training_plan import TrainingPlan as training_plans
from src.repositories.training_plan import TrainingPlanRepository

training_plan_router = APIRouter(prefix='/training_plan', tags=['training_plans'])

#CRUD training_plan

@training_plan_router.get('',response_model=List[TrainingPlan],description="Returns all training_plan")
def get_categories()-> List[TrainingPlan]:
    db= SessionLocal()
    result = TrainingPlanRepository(db).get_all_training_plans()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@training_plan_router.get('{id}',response_model=TrainingPlan,description="Returns data of one specific training_plan")
def get_training_plan(id: int = Path(ge=1)) -> TrainingPlan:
    db = SessionLocal()
    element=  TrainingPlanRepository(db).get_training_plan_by_id(id)
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

@training_plan_router.post('',response_model=dict,description="Creates a new training_plan")
def create_categorie(training_plan: TrainingPlan = Body()) -> dict:
    db= SessionLocal()
    new_training_plan = TrainingPlanRepository(db).create_new_training_plan(training_plan)
    return JSONResponse(
        content={        
        "message": "The training_plan was successfully created",        
        "data": jsonable_encoder(new_training_plan)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@training_plan_router.delete('{id}',response_model=dict,description="Removes specific training_plan")
def remove_training_plan(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = TrainingPlanRepository(db).delete_training_plan(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested training_plan was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)

@training_plan_router.put('{id}',response_model=dict,description="Updates specific training_plan")
def update_training_plan(id: int = Path(ge=1), training_plan: TrainingPlan = Body()) -> dict:
    db = SessionLocal()
    element = TrainingPlanRepository(db).update_training_plan(id, training_plan)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested training_plan was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)

