from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.repositories.food import FoodRepository
from src.schemas.food import Food
from src.models.food import Food as FoodModel

food_router = APIRouter(prefix='/food', tags=['foods'])

#CRUD food

@food_router.get('',response_model=List[Food],description="Returns all food")
def get_categories()-> List[Food]:
    db= SessionLocal()
    result = FoodRepository(db).get_all_food()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@food_router.get('{id}',response_model=Food,description="Returns data of one specific food")
def get_food(id: int = Path(ge=1)) -> Food:
    db = SessionLocal()
    element=  FoodRepository(db).get_food_by_id(id)
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

@food_router.post('',response_model=dict,description="Creates a new food")
def create_categorie(food: Food = Body()) -> dict:
    db= SessionLocal()
    new_food = FoodRepository(db).create_new_food(food)
    return JSONResponse(
        content={        
        "message": "The food was successfully created",        
        "data": jsonable_encoder(new_food)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@food_router.delete('{id}',response_model=dict,description="Removes specific food")
def remove_food(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = FoodRepository(db).delete_food(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested food was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content={        
            "message": "The food was successfully removed",        
            "data": jsonable_encoder(element)    
            }, 
        status_code=status.HTTP_200_OK
        )

@food_router.put('{id}',response_model=Food,description="Updates specific food")
def update_food(id: int = Path(ge=1), food: Food = Body()) -> dict:
    db = SessionLocal()
    element = FoodRepository(db).update_food(id, food)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested food was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content={        
            "message": "The food was successfully updated",        
            "data": jsonable_encoder(element)    
            }, 
        status_code=status.HTTP_200_OK
        )