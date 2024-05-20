from fastapi import APIRouter, Body, Query, Path, status, Depends
from fastapi.responses import JSONResponse
from typing import List, Annotated
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.diet import Diet
from src.models.diet import Diet as diets
from src.repositories.diet import DietRepository

from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler

diet_router = APIRouter(tags=['Dietas'])

#CRUD diet

@diet_router.get('/',response_model=List[Diet],description="Returns all diet")
def get_diets(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[Diet]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_current_user = payload.get("user.role")
        if role_current_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        result = DietRepository(db).get_all_diets(current_user)
        return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@diet_router.get('/{id}',response_model=Diet,description="Returns specific diet")
def get_diet_by_id(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_current_user = payload.get("user.role")
        if role_current_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        element=  DietRepository(db).get_diet_by_id(id, current_user)
        if not element:        
            return JSONResponse(
                content={            
                    "message": "The requested diet was not found",            
                    "data": None        
                    }, 
                status_code=status.HTTP_404_NOT_FOUND
                )    
        return JSONResponse(
            content=jsonable_encoder(element),                        
            status_code=status.HTTP_200_OK
            )

@diet_router.post('/',response_model=Diet,description="Creates a new diet")
def create_diet(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], diet: Diet = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_current_user = payload.get("user.role")
        if role_current_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        result = DietRepository(db).create_new_diet(diet, current_user)
        return JSONResponse(
            content=jsonable_encoder(result), 
            status_code=status.HTTP_200_OK
        )

@diet_router.delete('/{id}',response_model=dict,description="Removes specific diet")
def remove_diet(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_current_user = payload.get("user.role")
        if role_current_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        element = DietRepository(db).delete_diet(id, current_user)
        if not element:        
            return JSONResponse(
                content={            
                    "message": "The requested diet was not found",            
                    "data": None        
                    }, 
                status_code=status.HTTP_404_NOT_FOUND
                )
        return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)

@diet_router.put('/{id}',response_model=Diet,description="Updates specific diet")
def update_diet(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1), diet: Diet = Body()) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_current_user = payload.get("user.role")
        if role_current_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        result = DietRepository(db).update_diet(id, diet, current_user)
        if not result:        
            return JSONResponse(
                content={            
                    "message": "The requested diet was not found",            
                    "data": None        
                    }, 
                status_code=status.HTTP_404_NOT_FOUND
            )
        return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
