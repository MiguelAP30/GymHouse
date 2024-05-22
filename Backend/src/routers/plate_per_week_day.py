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

@plate_per_week_day_router.get('/my_diets',response_model=List[PlatePerWeekDay],description="Devuelve todos mis platillos por día de la semana")
def get_all_my_plates_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[PlatePerWeekDay]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        current_user = payload.get("sub")
        if role_user >= 2:
            if status_user == True:
                result = PlatePerWeekDayRepository(db).get_all_my_plate_per_week_day(current_user)
                return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
            return JSONResponse(content={"message": "Your account is disabled", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@plate_per_week_day_router.get('/premium_diets',response_model=List[PlatePerWeekDay],description="Devuelve todos los platillos de usuarios premium por día de la semana")
def get_premium_plates_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[PlatePerWeekDay]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        if role_user >= 2:
            if status_user == True:
                result = PlatePerWeekDayRepository(db).get_all_premium_plate_per_week_day()
                return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
            return JSONResponse(content={"message": "Your account is disabled", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@plate_per_week_day_router.get('/client_diets',response_model=List[PlatePerWeekDay],description="Devuelve todos los platillos de clientes por día de la semana")
def get_client_plates_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[PlatePerWeekDay]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        status_user = payload.get("user.status")
        role_user = payload.get("user.role")
        if role_user >= 2:
            if status_user == True:
                result = PlatePerWeekDayRepository(db).get_all_client_plate_per_week_day()
                return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
            return JSONResponse(content={"message": "Your account is disabled", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)


@plate_per_week_day_router.get('/admin_diets',response_model=List[PlatePerWeekDay],description="Devuelve todos los platillos de administradores por día de la semana")
def get_admin_plates_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[PlatePerWeekDay]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        current_user = payload.get("sub")
        if role_user >= 2:
            if status_user == True:
                result = PlatePerWeekDayRepository(db).get_all_my_plate_per_week_day(current_user)
                return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
            return JSONResponse(content={"message": "Your account is disabled", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@plate_per_week_day_router.get('/{id}',response_model=PlatePerWeekDay,description="Devuelve un platillo por día de la semana en específico")
def get_plate_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> PlatePerWeekDay:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        current_user = payload.get("sub")
        if role_user >= 2:
            if status_user == True:
                result = PlatePerWeekDayRepository(db).get_plate_per_week_day_by_id(id,current_user)
                return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
            return JSONResponse(content={"message": "Your account is disabled", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@plate_per_week_day_router.post('/',response_model=dict,description="Crea un nuevo platillo por día de la semana")
def create_plate(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], plate_per_week_day: PlatePerWeekDay = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        current_user = payload.get("sub")
        if role_user >= 2:
            if status_user == True:
                new_plate_per_week_day = PlatePerWeekDayRepository(db).create_new_plate_per_week_day(plate_per_week_day)
                return JSONResponse(
                    content={        
                    "message": "The plate per week day was successfully created",        
                    "data": jsonable_encoder(new_plate_per_week_day)    
                    }, 
                    status_code=status.HTTP_201_CREATED
                )
            return JSONResponse(content={"message": "Your account is disabled", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@plate_per_week_day_router.delete('/{id}',response_model=dict,description="Elimina un platillo por día de la semana específico")
def remove_plate_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        current_user = payload.get("sub")
        if role_user >= 2:
            if status_user == True:
                PlatePerWeekDayRepository(db).delete_plate_per_week_day(id, current_user)
                return JSONResponse(
                    content= {
                            "message": "The plate per week day was successfully deleted",
                        },                        
                    status_code=status.HTTP_200_OK
                    )
            return JSONResponse(content={"message": "Your account is disabled", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
