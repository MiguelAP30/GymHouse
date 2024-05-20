from fastapi import APIRouter, Body, Query, Path, status, Depends
from fastapi.responses import JSONResponse
from typing import List, Annotated
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.repositories.food_category import FoodCategoryRepository
from src.schemas.food_category import FoodCategory
from src.models.food_category import FoodCategory as FoodCategoryModel

from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler

food_category_router = APIRouter(tags=['Categorías de alimentos'])

#CRUD food_category

@food_category_router.get('/',response_model=List[FoodCategory],description="Returns all food_category")
def get_food_categories(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[FoodCategory]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            result = FoodCategoryRepository(db).get_all_food_categories()
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@food_category_router.get('/{id}',response_model=FoodCategory,description="Returns data of one specific food_category")
def get_food_category(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> FoodCategory:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            element=  FoodCategoryRepository(db).get_food_category_by_id(id)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested food_category was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )    
            return JSONResponse(
                content=jsonable_encoder(element),                        
                status_code=status.HTTP_200_OK
                )
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@food_category_router.post('/',response_model=dict,description="Creates a new food_category")
def create_food_category(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], food: FoodCategory = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            new_food = FoodCategoryRepository(db).create_new_food_category(food)
            return JSONResponse(
                content={            
                    "message": "The food_category was successfully created",            
                    "data": jsonable_encoder(new_food)        
                    }, 
                status_code=status.HTTP_201_CREATED
                )
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@food_category_router.delete('/{id}',response_model=dict,description="Removes specific food_category")
def remove_food_category(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            element = FoodCategoryRepository(db).delete_food_category(id)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested food_category was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )    
            return JSONResponse(
                content={        
                "message": "The food_category was successfully deleted",        
                "data": jsonable_encoder(element)    
                }, 
                status_code=status.HTTP_200_OK
            )
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@food_category_router.put('/{id}',response_model=dict,description="Updates specific food_category")
def update_food_category(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1), food: FoodCategory = Body()) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            element = FoodCategoryRepository(db).update_food_category(id, food)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested food_category was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )    
            return JSONResponse(
                content={        
                "message": "The food_category was successfully updated",        
                "data": jsonable_encoder(element)    
                }, 
                status_code=status.HTTP_200_OK
            )
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)