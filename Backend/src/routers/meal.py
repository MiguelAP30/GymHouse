from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.meal import Meal
from src.models.meal import Meal as meals
from src.repositories.meal import MealRepository

meal_router = APIRouter(tags=['Comidas'])

#CRUD meal

@meal_router.get('/',response_model=List[Meal],description="Returns all meal")
def get_categories()-> List[Meal]:
    db= SessionLocal()
    result = MealRepository(db).get_all_meals()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@meal_router.get('/{id}',response_model=Meal,description="Returns data of one specific meal")
def get_meal(id: int = Path(ge=1)) -> Meal:
    db = SessionLocal()
    element=  MealRepository(db).get_meal_by_id(id)
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

@meal_router.post('/',response_model=dict,description="Creates a new meal")
def create_categorie(meal: Meal = Body()) -> dict:
    db= SessionLocal()
    new_meal = MealRepository(db).create_new_meal(meal)
    return JSONResponse(
        content={        
        "message": "The meal was successfully created",        
        "data": jsonable_encoder(new_meal)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@meal_router.delete('/{id}',response_model=dict,description="Removes specific meal")
def remove_meal(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = MealRepository(db).delete_meal(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested meal was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)
