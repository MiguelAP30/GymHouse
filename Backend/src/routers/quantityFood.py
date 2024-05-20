from fastapi import APIRouter, Body, Depends, Query, Path, security, status
from fastapi.responses import JSONResponse
from typing import Annotated, List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.quantityFood import QuantityFood
from src.models.quantityFood import QuantityFood as quantityFoods
from src.repositories.quantityFood import QuantityFoodRepository

from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler



quantityFood_router = APIRouter(tags=['Cantidad de alimentos'])

#CRUD quantityFood

@quantityFood_router.get('/',response_model=List[QuantityFood],description="Devuelve todas mis cantidades de alimentos")
def get_quantity_foods(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[QuantityFood]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        result = QuantityFoodRepository(db).get_all_quantity_foods(current_user)
        return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@quantityFood_router.get('/{id}',response_model=QuantityFood,description="Devuelve la información de una cantidad de alimento específica")
def get_quantity_Food(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> QuantityFood:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        element=  QuantityFoodRepository(db).get_quantity_food_by_id(id, current_user)
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

@quantityFood_router.post('/',response_model=dict,description="Crea una nueva cantidad de alimento")
def create_quantity_Food(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], quantityFood: QuantityFood = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        new_quantityFood = QuantityFoodRepository(db).create_new_quantity_food(quantityFood)
        return JSONResponse(
            content={        
            "message": "The quantityFood was successfully created",        
            "data": jsonable_encoder(new_quantityFood)    
            }, 
            status_code=status.HTTP_201_CREATED
        )

@quantityFood_router.delete('/{id}',response_model=dict,description="Remueve una cantidad de alimento específica")
def remove_quantityFood(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        element = QuantityFoodRepository(db).get_quantity_food_by_id(id, current_user)
        if not element:        
            return JSONResponse(
                content={            
                    "message": "The requested quantityFood was not found",            
                    "data": None        
                    }, 
                status_code=status.HTTP_404_NOT_FOUND
                )    
        QuantityFoodRepository(db).delete_quantity_food(element)
        return JSONResponse(
            content={        
            "message": "The quantityFood was successfully deleted",        
            "data": None    
            }, 
            status_code=status.HTTP_200_OK
        )

@quantityFood_router.put('/{id}',response_model=dict,description="Actualiza una cantidad de alimento específica")
def update_quantity_Food(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1), quantityFood: QuantityFood = Body()) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user < 2:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
        current_user = payload.get("sub")
        element = QuantityFoodRepository(db).get_quantity_food_by_id(id, current_user)
        if not element:
            return JSONResponse(
                content={            
                    "message": "The requested quantityFood was not found",            
                    "data": None        
                    }, 
                status_code=status.HTTP_404_NOT_FOUND
                )
        QuantityFoodRepository(db).update_quantity_food(id, element, quantityFood)
        return JSONResponse(
            content={        
            "message": "The quantityFood was successfully updated",        
            "data": jsonable_encoder(element)    
            }, 
            status_code=status.HTTP_200_OK
        )
