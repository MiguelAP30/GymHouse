from fastapi import APIRouter, Body, Depends, Query, Path, status
from fastapi.responses import JSONResponse
from typing import Annotated, List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.repositories.exercise_per_week_day import ExercisePerWeekDayRepository
from src.schemas.exercise_per_week_day import ExercisePerWeekDay
from src.models.exercise_per_week_day import ExercisePerWeekDay as ExercisePerWeekDayModel
from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler

exercise_per_week_day_router = APIRouter(tags=['Ejercicios para días de la semana'])

#CRUD exercise_per_week_day

@exercise_per_week_day_router.get('/my_exercises',response_model=List[ExercisePerWeekDay],description="Devuelve todos mis ejercicios por día de la semana")
def get_all_my_excercise_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[ExercisePerWeekDay]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        current_user = payload.get("sub")
        if role_user >= 2:
            result = ExercisePerWeekDayRepository(db).get_all_my_excercise_per_week_day(current_user)
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
        
@exercise_per_week_day_router.get('/premium_exercises',response_model=List[ExercisePerWeekDay],description="Devuelve todos los ejercicios de usuarios premium por dia de la semana")
def get_premium_excercise_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[ExercisePerWeekDay]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 2:
            result = ExercisePerWeekDayRepository(db).get_premium_excercise_per_week_day()
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
        
@exercise_per_week_day_router.get('/client_exercises',response_model=List[ExercisePerWeekDay],description="Returns all exercise_per_week_day")
def get_client_excercise_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[ExercisePerWeekDay]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 2:
            result = ExercisePerWeekDayRepository(db).get_client_excercise_per_week_day()
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
        
@exercise_per_week_day_router.get('/admin_exercises',response_model=List[ExercisePerWeekDay],description="Returns all exercise_per_week_day")
def get_admin_excercise_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[ExercisePerWeekDay]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 2:
            result = ExercisePerWeekDayRepository(db).get_admin_excercise_per_week_day()
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@exercise_per_week_day_router.get('/{id}',response_model=ExercisePerWeekDay,description="Returns data of one specific exercise_per_week_day")
def get_excercise_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> ExercisePerWeekDay:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        element=  ExercisePerWeekDayRepository(db).get_excercise_per_week_day_by_id(id)
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

@exercise_per_week_day_router.post('/',response_model=dict,description="Creates a new exercise_per_week_day")
def create_excercise_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], exercise: ExercisePerWeekDay = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        new_excercise = ExercisePerWeekDayRepository(db).create_new_excercise_per_week_day(exercise)
        return JSONResponse(
            content={        
            "message": "The exercise_per_week_day was successfully created",        
            "data": jsonable_encoder(new_excercise)    
            }, 
            status_code=status.HTTP_201_CREATED
        )

@exercise_per_week_day_router.delete('/{id}',response_model=dict,description="Removes specific exercise_per_week_day")
def remove_excercise_per_week_day(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        element = ExercisePerWeekDayRepository(db).delete_excercise_per_week_day(id)
        if not element:        
            return JSONResponse(
                content={            
                    "message": "The requested exercise_per_week_day was not found",            
                    "data": None        
                    }, 
                status_code=status.HTTP_404_NOT_FOUND
                )    
        return JSONResponse(
            content={        
                "message": "The exercise_per_week_day was successfully removed",        
                "data": jsonable_encoder(element)    
            }, 
            status_code=status.HTTP_200_OK
        )

