from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.user import User
from src.models.user import User as users
from src.repositories.user import UserRepository

user_router = APIRouter(tags=['Usuarios'])

#CRUD user

@user_router.get('/',response_model=List[User],description="Returns all user")
def get_categories()-> List[User]:
    db= SessionLocal()
    result = UserRepository(db).get_all_users()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@user_router.get('/{id}',response_model=User,description="Returns data of one specific user")
def get_user(id: int = Path(ge=1)) -> User:
    db = SessionLocal()
    element=  UserRepository(db).get_user_by_id(id)
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

@user_router.post('/',response_model=dict,description="Creates a new user")
def create_categorie(user: User = Body()) -> dict:
    db= SessionLocal()
    new_user = UserRepository(db).create_new_user(user)
    return JSONResponse(
        content={        
        "message": "The user was successfully created",        
        "data": jsonable_encoder(new_user)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@user_router.delete('/{id}',response_model=dict,description="Removes specific user")
def remove_user(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = UserRepository(db).delete_user(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested user was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
        )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)

@user_router.put('/{id}',response_model=dict,description="Updates specific user")
def update_user(id: int = Path(ge=1), user: User = Body()) -> dict:
    db = SessionLocal()
    element = UserRepository(db).update_user(id, user)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested user was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
        )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)