from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.quantityFood import QuantityFood
from src.models.quantityFood import QuantityFood as quantityFoods
from src.repositories.quantityFood import QuantityFoodRepository

quantityFood_router = APIRouter(prefix='/quantityFood', tags=['quantity_foods'])

#CRUD quantityFood

@quantityFood_router.get('',response_model=List[QuantityFood],description="Returns all quantityFood")
def get_categories()-> List[QuantityFood]:
    db= SessionLocal()
    result = QuantityFoodRepository(db).get_all_quantity_foods()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@quantityFood_router.get('{id}',response_model=QuantityFood,description="Returns data of one specific quantityFood")
def get_quantityFood(id: int = Path(ge=1)) -> QuantityFood:
    db = SessionLocal()
    element=  QuantityFoodRepository(db).get_quantity_food_by_id(id)
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

@quantityFood_router.post('',response_model=dict,description="Creates a new quantityFood")
def create_categorie(quantityFood: QuantityFood = Body()) -> dict:
    db= SessionLocal()
    new_quantityFood = QuantityFoodRepository(db).create_new_quantity_food(quantityFood)
    return JSONResponse(
        content={        
        "message": "The quantityFood was successfully created",        
        "data": jsonable_encoder(new_quantityFood)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@quantityFood_router.delete('{id}',response_model=dict,description="Removes specific quantityFood")
def remove_quantityFood(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = QuantityFoodRepository(db).delete_quantity_food(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested quantityFood was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)

@quantityFood_router.put('{id}',response_model=dict,description="Updates specific quantityFood")
def update_quantityFood(id: int = Path(ge=1), quantityFood: QuantityFood = Body()) -> dict:
    db = SessionLocal()
    element = QuantityFoodRepository(db).update_quantity_food(id, quantityFood)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested quantityFood was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(
        content={        
        "message": "The quantityFood was successfully updated",        
        "data": jsonable_encoder(element)    
        }, 
        status_code=status.HTTP_200_OK
    )
