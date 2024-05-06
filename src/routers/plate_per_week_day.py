from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.plate_per_week_day import PlatePerWeekDay
from src.models.plate_per_week_day import PlatePerWeekDay as plate_per_week_days
from src.repositories.plate_per_week_day import PlatePerWeekDayRepository

plate_per_week_day_router = APIRouter(prefix='/plate_per_week_day', tags=['plate_per_week_days'])

#CRUD plate_per_week_day

@plate_per_week_day_router.get('',response_model=List[PlatePerWeekDay],description="Returns all plate_per_week_day")
def get_categories()-> List[PlatePerWeekDay]:
    db= SessionLocal()
    result = PlatePerWeekDayRepository(db).get_all_plate_per_week_days()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@plate_per_week_day_router.get('{id}',response_model=PlatePerWeekDay,description="Returns data of one specific plate_per_week_day")
def get_plate_per_week_day(id: int = Path(ge=1)) -> PlatePerWeekDay:
    db = SessionLocal()
    element=  PlatePerWeekDayRepository(db).get_plate_per_week_day_by_id(id)
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

@plate_per_week_day_router.post('',response_model=dict,description="Creates a new plate_per_week_day")
def create_categorie(plate_per_week_day: PlatePerWeekDay = Body()) -> dict:
    db= SessionLocal()
    new_plate_per_week_day = PlatePerWeekDayRepository(db).create_new_plate_per_week_day(plate_per_week_day)
    return JSONResponse(
        content={        
        "message": "The plate_per_week_day was successfully created",        
        "data": jsonable_encoder(new_plate_per_week_day)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@plate_per_week_day_router.delete('{id}',response_model=dict,description="Removes specific plate_per_week_day")
def remove_plate_per_week_day(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = PlatePerWeekDayRepository(db).delete_plate_per_week_day(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested plate_per_week_day was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)
