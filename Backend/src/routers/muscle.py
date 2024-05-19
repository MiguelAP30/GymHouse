from fastapi import APIRouter, Body, Depends, Query, Path, status
from fastapi.responses import JSONResponse
from typing import Annotated, List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.muscle import Muscle
from src.models.muscle import Muscle as muscles
from src.repositories.muscle import MuscleRepository
from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler


muscle_router = APIRouter(tags=['Músculos'])

#CRUD muscle

@muscle_router.get('/',response_model=List[Muscle],description="Returns all muscle")
def get_muscles(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[Muscle]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            result = MuscleRepository(db).get_all_muscles()
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
    
@muscle_router.get('/{id}',response_model=Muscle,description="Returns data of one specific muscle")
def get_muscle(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> Muscle:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            element=  MuscleRepository(db).get_muscle_by_id(id)
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
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@muscle_router.post('/',response_model=dict,description="Creates a new muscle")
def create_muscle(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], muscle: Muscle = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            new_muscle = MuscleRepository(db).create_new_muscle(muscle)
            return JSONResponse(
                content={        
                "message": "The muscle was successfully created",        
                "data": jsonable_encoder(new_muscle)    
                }, 
                status_code=status.HTTP_201_CREATED
            )
        else:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@muscle_router.delete('/{id}',response_model=dict,description="Removes specific muscle")
def remove_muscle(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            element = MuscleRepository(db).delete_muscle(id)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested muscle was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )
            return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@muscle_router.put('/{id}',response_model=dict,description="Updates specific muscle")
def update_muscle(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1), muscle: Muscle = Body()) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            element = MuscleRepository(db).update_muscle(id, muscle)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested muscle was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )
            return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
