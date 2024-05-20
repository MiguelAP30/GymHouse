from fastapi import APIRouter, Body, Depends, Query, Path, status
from fastapi.responses import JSONResponse
from typing import Annotated, List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.plate_per_week_day import PlatePerWeekDay
from src.models.plate_per_week_day import PlatePerWeekDay as plate_per_week_days
from src.repositories.plate_per_week_day import PlatePerWeekDayRepository

from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler

plate_per_week_day_router = APIRouter(tags=['Platillos por días de la semana'])

#CRUD plate_per_week_day

@plate_per_week_day_router.get('/my_diets',response_model=List[PlatePerWeekDay],description="Returns all plate_per_week_day")
def get_all_my_plates_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[PlatePerWeekDay]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        current_user = payload.get("sub")
        if role_user >= 2:
            result = PlatePerWeekDayRepository(db).get_all_my_plate_per_week_day(current_user)
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@plate_per_week_day_router.get('/premium_diets',response_model=List[PlatePerWeekDay],description="Returns all plate_per_week_day")
def get_premium_plates_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[PlatePerWeekDay]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 2:
            result = PlatePerWeekDayRepository(db).get_all_premium_plate_per_week_day()
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@plate_per_week_day_router.get('/client_diets',response_model=List[PlatePerWeekDay],description="Returns all plate_per_week_day")
def get_client_plates_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[PlatePerWeekDay]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 2:
            result = PlatePerWeekDayRepository(db).get_all_client_plate_per_week_day()
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@plate_per_week_day_router.get('/admin_diets',response_model=List[PlatePerWeekDay],description="Returns all plate_per_week_day")
def get_admin_plates_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[PlatePerWeekDay]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        current_user = payload.get("sub")
        if role_user >= 2:
            result = PlatePerWeekDayRepository(db).get_all_my_plate_per_week_day(current_user)
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)



@plate_per_week_day_router.get('/{id}',response_model=PlatePerWeekDay,description="Returns data of one specific plate_per_week_day")
def get_plate_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> PlatePerWeekDay:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        current_user = payload.get("sub")
        if role_user >= 2:
            result = PlatePerWeekDayRepository(db).get_plate_per_week_day_by_id(id,current_user)
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
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

@plate_per_week_day_router.post('/',response_model=dict,description="Creates a new plate_per_week_day")
def create_plate(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], plate_per_week_day: PlatePerWeekDay = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        new_plate_per_week_day = PlatePerWeekDayRepository(db).create_new_plate_per_week_day(plate_per_week_day)
        return JSONResponse(
            content={        
            "message": "The plate_per_week_day was successfully created",        
            "data": jsonable_encoder(new_plate_per_week_day)    
            }, 
            status_code=status.HTTP_201_CREATED
        )

@plate_per_week_day_router.delete('/{id}',response_model=dict,description="Removes specific plate_per_week_day")
def remove_plate_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        current_user = payload.get("sub")   
        PlatePerWeekDayRepository(db).delete_plate_per_week_day(id, current_user)
        return JSONResponse(
            content=jsonable_encoder(element),                        
            status_code=status.HTTP_200_OK
            )
    element = PlatePerWeekDayRepository(db).delete_plate_per_week_day(id, current_user)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested plate_per_week_day was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)
