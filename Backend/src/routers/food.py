from fastapi import APIRouter, Body, Query, Path, status, Depends
from fastapi.responses import JSONResponse
from typing import List, Annotated
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.repositories.food import FoodRepository
from src.schemas.food import Food
from src.models.food import Food as FoodModel

from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler

food_router = APIRouter(tags=['Alimentos'])

#CRUD food

@food_router.get('/',response_model=List[Food],description="Devuelve todos los alimentos")
def get_foods(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[Food]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        if role_user >= 3:
            if status_user:
                result = FoodRepository(db).get_all_foods()
                return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
            else:
                return JSONResponse(content={"message": "Your account is inactive", "data": None}, status_code=status.HTTP_403_FORBIDDEN)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@food_router.get('/{id}',response_model=Food,description="Devuelve la información de un solo alimento")
def get_food(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> Food:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        if role_user >= 3:
            if status_user:
                element=  FoodRepository(db).get_food_by_id(id)
                if not element:        
                    return JSONResponse(
                        content={            
                            "message": "The requested food was not found",            
                            "data": None        
                            }, 
                        status_code=status.HTTP_404_NOT_FOUND
                        )    
                return JSONResponse(
                    content=jsonable_encoder(element),                        
                    status_code=status.HTTP_200_OK
                    )
            else:
                return JSONResponse(content={"message": "Your account is inactive", "data": None}, status_code=status.HTTP_403_FORBIDDEN)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@food_router.post('/',response_model=dict,description="Crea un nuevo alimento")
def create_food(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], food: Food = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        if role_user >= 3:
            if status_user:
                new_food = FoodRepository(db).create_new_food(food)
                return JSONResponse(
                    content={            
                        "message": "The food was successfully created",            
                        "data": jsonable_encoder(new_food)        
                        }, 
                    status_code=status.HTTP_201_CREATED
                    )
            else:
                return JSONResponse(content={"message": "Your account is inactive", "data": None}, status_code=status.HTTP_403_FORBIDDEN)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@food_router.delete('/{id}',response_model=dict,description="Elimina un alimento específico")
def remove_food(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        if role_user >= 3:
            if status_user:
                element = FoodRepository(db).delete_food(id)
                if not element:        
                    return JSONResponse(
                        content={            
                            "message": "The requested food was not found",            
                            "data": None        
                            }, 
                        status_code=status.HTTP_404_NOT_FOUND
                        )    
                return JSONResponse(
                    content={        
                        "message": "The food was successfully removed",        
                        "data": jsonable_encoder(element)    
                        }, 
                    status_code=status.HTTP_200_OK
                    )
            else:
                return JSONResponse(content={"message": "Your account is inactive", "data": None}, status_code=status.HTTP_403_FORBIDDEN)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
    

@food_router.put('/{id}',response_model=Food,description="Actualiza un alimento específico")
def update_food(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1), food: Food = Body()) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        if role_user >= 3:
            if status_user:
                element = FoodRepository(db).update_food(id, food)
                if not element:        
                    return JSONResponse(
                        content={            
                            "message": "The requested food was not found",            
                            "data": None        
                            }, 
                        status_code=status.HTTP_404_NOT_FOUND
                        )    
                return JSONResponse(
                    content={        
                        "message": "The food was successfully updated",        
                        "data": jsonable_encoder(element)    
                        }, 
                    status_code=status.HTTP_200_OK
                    )
            else:
                return JSONResponse(content={"message": "Your account is inactive", "data": None}, status_code=status.HTTP_403_FORBIDDEN)
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)