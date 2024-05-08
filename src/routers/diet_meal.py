from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.models.diet_meal import DietMeal
from src.schemas.diet_meal import DietMeal as DietMealModel
from src.repositories.diet_meal import DietMealRepository

diet_meal_router = APIRouter(tags=['Dietas de comidas'])

#CRUD diet_meal

@diet_meal_router.get('/',response_model=List[DietMealModel],description="Returns all diet_meal")
def get_diet_meal()-> List[DietMealModel]:
    db= SessionLocal()
    result = DietMealRepository(db).get_all_diet_meal()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@diet_meal_router.get('/{id}',response_model=DietMealModel,description="Returns specific diet_meal")
def get_diet_meal_by_id(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = DietMealRepository(db).get_diet_meal_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested diet_meal was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content={        
            "message": "The diet_meal was found successfully",        
            "data": jsonable_encoder(element)    
            }, 
        status_code=status.HTTP_200_OK
        )

@diet_meal_router.post('/',response_model=DietMealModel,description="Creates a new diet_meal")
def create_diet_meal(diet_meal: DietMealModel = Body()) -> dict:
    db= SessionLocal()
    new_diet_meal = DietMealRepository(db).create_new_diet_meal(diet_meal)
    return JSONResponse(
        content={        
        "message": "The diet_meal was successfully created",        
        "data": jsonable_encoder(new_diet_meal)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@diet_meal_router.delete('/{id}',response_model=dict,description="Removes specific diet_meal")
def remove_diet_meal(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = DietMealRepository(db).get_diet_meal_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested diet_meal was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    DietMealRepository(db).delete_diet_meal(id)  
    return JSONResponse(
        content={        
            "message": "The diet_meal was removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )