from fastapi import APIRouter, Body, Query, Path, status, Depends
from fastapi.responses import JSONResponse
from typing import List, Annotated
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.meal import Meal
from src.models.meal import Meal as meals
from src.repositories.meal import MealRepository

from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler

meal_router = APIRouter(tags=['Comidas'])

#CRUD meal

@meal_router.get('/',response_model=List[Meal],description="Devuelve todas las comidas")
def get_meals(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[Meal]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        result = MealRepository(db).get_all_meals(current_user)
        return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@meal_router.get('/{id}',response_model=Meal,description="Devuelve la información de una comida específica")
def get_meal(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> Meal:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        element = MealRepository(db).get_meal_by_id(id, current_user)
        if not element:        
            return JSONResponse(
                content={            
                    "message": "The requested meal was not found",            
                    "data": None        
                    }, 
                status_code=status.HTTP_404_NOT_FOUND
                )    
        return JSONResponse(
            content=jsonable_encoder(element),                        
            status_code=status.HTTP_200_OK
            )

@meal_router.post('/',response_model=dict,description="Crea una nueva comida")
def create_meal(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], meal: Meal = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        new_meal = MealRepository(db).create_new_meal(meal)
        return JSONResponse(
            content={        
            "message": "The meal was successfully created",        
            "data": jsonable_encoder(new_meal)    
            }, 
            status_code=status.HTTP_201_CREATED
        )

@meal_router.delete('/{id}',response_model=dict,description="Removes specific meal")
def remove_meal(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        MealRepository(db).delete_meal(id, current_user)
        return JSONResponse(
            content={        
            "message": "The meal was successfully deleted",        
            "data": None    
            }, 
            status_code=status.HTTP_200_OK
        )

@meal_router.put('/{id}',response_model=dict,description="Actualiza una comida específica")
def update_meal(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1), meal: Meal = Body()) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        result = MealRepository(db).update_meal(id, meal, current_user)
        return JSONResponse(
            content={        
            "message": "The meal was successfully updated",        
            "data": jsonable_encoder(result)    
            }, 
            status_code=status.HTTP_200_OK
        )