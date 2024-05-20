from fastapi import APIRouter, Body, Query, Path, status, Depends
from fastapi.responses import JSONResponse
from typing import List, Annotated
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.diet_user import DietUser
from src.models.diet_user import DietUser as DietUsers
from src.repositories.diet_user import DietUserRepository

from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler

diet_user_router = APIRouter(tags=['Dietas de usuarios'])

#CRUD diet_user

@diet_user_router.get('/',response_model=List[DietUser],description="Returns all diet_user")
def get_diet_user(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[DietUser]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        current_user = payload.get("sub")
        role_current_user = payload.get("user.role")
        if role_current_user >= 2:
            result = DietUserRepository(db).get_all_diet_user(current_user)
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@diet_user_router.post('/',response_model=DietUser,description="Creates a new diet_user")
def create_diet_user(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)],diet_user: DietUser = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_current_user = payload.get("user.role")
        if role_current_user >= 2:
            current_user = payload.get("sub")
            diet_user.user_email = current_user
            new_diet_user = DietUserRepository(db).create_new_diet_user(diet_user)
            return JSONResponse(content={
                "message": "The diet_user was created successfully",
                "data": jsonable_encoder(new_diet_user)
                }, 
                status_code=status.HTTP_201_CREATED
            )
        else:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@diet_user_router.delete('/{id}',response_model=dict,description="Removes specific diet_user")
def remove_diet_user(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        current_user = payload.get("sub")
        role_current_user = payload.get("user.role")
        if role_current_user >= 2:
            element = DietUserRepository(db).delete_diet_user(id, current_user)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested diet_user was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )    
            return JSONResponse(
                content={            
                    "message": "The diet_user was deleted successfully",            
                    "data": None        
                    }, 
                status_code=status.HTTP_200_OK
                )
        else:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@diet_user_router.get('/{id}',response_model=DietUser,description="Returns specific diet_user")
def get_diet_user_by_id(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        current_user = payload.get("sub")
        role_current_user = payload.get("user.role")
        if role_current_user >= 2:
            element = DietUserRepository(db).get_diet_user_by_id(id, current_user)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested diet_user was not found",            
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