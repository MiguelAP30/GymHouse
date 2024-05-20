from fastapi import APIRouter, Body, Query, Path, status, Depends
from fastapi.responses import JSONResponse
from typing import List, Annotated
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.training_plan_user import TrainingPlanUser
from src.models.training_plan_user import TrainingPlanUser as training_plan_users
from src.repositories.training_plan_user import TrainingPlanUserRepository

from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler

training_plan_user_router = APIRouter(tags=['Planes de entrenamiento de los usuarios'])

#CRUD training_plan_user

@training_plan_user_router.get('/',response_model=List[TrainingPlanUser],description="Devuelve todos los planes de entrenamiento de un usuario")
def get_all_training_plans(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[TrainingPlanUser]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        current_user = payload.get("sub")
        role_current_user = payload.get("user.role")
        if role_current_user >= 2:
            result = TrainingPlanUserRepository(db).get_all_training_plan_users(current_user)
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@training_plan_user_router.get('/{id}',response_model=TrainingPlanUser,description="Devuelve un solo plan de entrenamiento de un usuario")
def get_training_plan_user(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> TrainingPlanUser:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        current_user = payload.get("sub")
        role_current_user = payload.get("user.role")
        if role_current_user >= 2:
            element=  TrainingPlanUserRepository(db).get_training_plan_user_by_id(id, current_user)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested training plan was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )    
            return JSONResponse(
                content=jsonable_encoder(element),                        
                status_code=status.HTTP_200_OK
                )
        else:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@training_plan_user_router.post('/',response_model=dict,description="Crear un nuevo plan de entrenamiento de un usuario")
def create_training_plan_user(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], training_plan_user: TrainingPlanUser = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_current_user = payload.get("user.role")
        if role_current_user >= 2:
            current_user = payload.get("sub")
            training_plan_user.user_email = current_user
            new_training_plan_user = TrainingPlanUserRepository(db).create_new_training_plan_user(training_plan_user)
            return JSONResponse(
                content={        
                "message": "The training_plan_user was successfully created",        
                "data": jsonable_encoder(new_training_plan_user)    
                }, 
                status_code=status.HTTP_201_CREATED
            )
        else:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@training_plan_user_router.delete('/{id}',response_model=dict,description="Remover un plan de entrenamiento de un usuario")
def remove_training_plan_user(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        current_user = payload.get("sub")
        role_current_user = payload.get("user.role")
        if role_current_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        else:
            element = TrainingPlanUserRepository(db).delete_training_plan_user(id, current_user)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested training_plan_user was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )
            return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)