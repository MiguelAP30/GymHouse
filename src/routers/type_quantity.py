from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.type_quantity import TypeQuantity
from src.models.type_quantity import TypeQuantity as type_quantities
from src.repositories.type_quantity import TypeQuantityRepository

type_quantity_router = APIRouter(prefix='/type_quantity', tags=['type_quantities'])

#CRUD type_quantity

@type_quantity_router.get('',response_model=List[TypeQuantity],description="Returns all type_quantity")
def get_categories()-> List[TypeQuantity]:
    db= SessionLocal()
    result = TypeQuantityRepository(db).get_all_type_quantities()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@type_quantity_router.get('{id}',response_model=TypeQuantity,description="Returns data of one specific type_quantity")
def get_type_quantity(id: int = Path(ge=1)) -> TypeQuantity:
    db = SessionLocal()
    element=  TypeQuantityRepository(db).get_type_quantity_by_id(id)
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

@type_quantity_router.post('',response_model=dict,description="Creates a new type_quantity")
def create_categorie(type_quantity: TypeQuantity = Body()) -> dict:
    db= SessionLocal()
    new_type_quantity = TypeQuantityRepository(db).create_new_type_quantity(type_quantity)
    return JSONResponse(
        content={        
        "message": "The type_quantity was successfully created",        
        "data": jsonable_encoder(new_type_quantity)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@type_quantity_router.delete('{id}',response_model=dict,description="Removes specific type_quantity")
def remove_type_quantity(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = TypeQuantityRepository(db).delete_type_quantity(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested type_quantity was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)

@type_quantity_router.put('{id}',response_model=dict,description="Updates specific type_quantity")
def update_type_quantity(id: int = Path(ge=1), type_quantity: TypeQuantity = Body()) -> dict:
    db = SessionLocal()
    element = TypeQuantityRepository(db).update_type_quantity(id, type_quantity)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested type_quantity was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)