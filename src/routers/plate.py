from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.plate import Plate
from src.models.plate import Plate as plates
from src.repositories.plate import PlateRepository

plate_router = APIRouter(prefix='/plate', tags=['plates'])

#CRUD plate

@plate_router.get('',response_model=List[Plate],description="Returns all plate")
def get_categories()-> List[Plate]:
    db= SessionLocal()
    result = PlateRepository(db).get_all_plates()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@plate_router.get('{id}',response_model=Plate,description="Returns data of one specific plate")
def get_plate(id: int = Path(ge=1)) -> Plate:
    db = SessionLocal()
    element=  PlateRepository(db).get_plate_by_id(id)
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

@plate_router.post('',response_model=dict,description="Creates a new plate")
def create_categorie(plate: Plate = Body()) -> dict:
    db= SessionLocal()
    new_plate = PlateRepository(db).create_new_plate(plate)
    return JSONResponse(
        content={        
        "message": "The plate was successfully created",        
        "data": jsonable_encoder(new_plate)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@plate_router.delete('{id}',response_model=dict,description="Removes specific plate")
def remove_plate(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = PlateRepository(db).delete_plate(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested plate was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)

@plate_router.put('{id}',response_model=dict,description="Updates specific plate")
def update_plate(id: int = Path(ge=1), plate: Plate = Body()) -> dict:
    db = SessionLocal()
    updated_plate = PlateRepository(db).update_plate(id, plate)
    if not updated_plate:        
        return JSONResponse(
            content={            
                "message": "The requested plate was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content={        
            "message": "The plate was successfully updated",        
            "data": jsonable_encoder(updated_plate)    
            }, 
        status_code=status.HTTP_200_OK
        )
