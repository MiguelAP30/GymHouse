from fastapi import APIRouter, Body, Depends, Query, Path, status
from fastapi.responses import JSONResponse
from typing import Annotated, List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.detailed_exercise import DetailedExercise
from src.repositories.detailed_exercise import DetailedExerciseRepository
from src.models.detailed_exercise import DetailedExercise as detailed_exercises
from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler

detailed_exercise_router = APIRouter(tags=['Ejercicios detallados'])

#CRUD detailed_exercise

@detailed_exercise_router.get('/',response_model=List[DetailedExercise],description="Returns all detailed_exercise")
def get_detailed_exercise(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[DetailedExercise]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_current_user = payload.get("user.role")
        if role_current_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        result = DetailedExerciseRepository(db).get_all_detailed_exercise(current_user)
        return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@detailed_exercise_router.post('/',response_model=DetailedExercise,description="Creates a new detailed_exercise")
def create_detailed_exercise(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], detailed_exercise: DetailedExercise = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_current_user = payload.get("user.role")
        if role_current_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        new_detailed_exercise = DetailedExerciseRepository(db).create_new_detailed_exercise(detailed_exercise)
        return JSONResponse(
            content={        
            "message": "The detailed_exercise was successfully created",        
            "data": jsonable_encoder(new_detailed_exercise)    
            }, 
            status_code=status.HTTP_201_CREATED
        )

@detailed_exercise_router.delete('/{id}',response_model=dict,description="Removes specific detailed_exercise")
def remove_detailed_exercise(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_current_user = payload.get("user.role")
        if role_current_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        DetailedExerciseRepository(db).delete_detailed_exercise(id, current_user)
        return JSONResponse(
            content={        
            "message": "The detailed_exercise was successfully deleted",        
            "data": None    
            }, 
            status_code=status.HTTP_200_OK
        )

@detailed_exercise_router.get('/{id}',response_model=DetailedExercise,description="Returns specific detailed_exercise")
def get_detailed_exercise_by_id(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_current_user = payload.get("user.role")
        if role_current_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        element=  DetailedExerciseRepository(db).get_detailed_exercise_by_id(id, current_user)
        if not element:        
            return JSONResponse(
                content={            
                    "message": "The requested detailed_exercise was not found",            
                    "data": None        
                    }, 
                status_code=status.HTTP_404_NOT_FOUND
                )    
        return JSONResponse(
            content=jsonable_encoder(element),                        
            status_code=status.HTTP_200_OK
            )

@detailed_exercise_router.put('/{id}',response_model=DetailedExercise,description="Updates specific detailed_exercise")
def update_detailed_exercise(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1), detailed_exercise: DetailedExercise = Body()) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_current_user = payload.get("user.role")
        if role_current_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        element = DetailedExerciseRepository(db).update_detailed_exercise(id, current_user, detailed_exercise)
        return JSONResponse(
            content={        
            "message": "The detailed_exercise was successfully updated",        
            "data": jsonable_encoder(element)    
            }, 
            status_code=status.HTTP_200_OK
        )