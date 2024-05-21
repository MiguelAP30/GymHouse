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
def get_users()-> List[User]:
    db= SessionLocal()
    result = UserRepository(db).get_all_users()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@user_router.get('/{email}',response_model=User,description="Returns data of one specific user")
def get_user(email: str = Path(min_length=5)) -> User:
    db = SessionLocal()
    element=  UserRepository(db).get_user_by_email(email)
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

@user_router.put('/{email}',response_model=dict,description="Desactiva el usuario del sistema")
def remove_user(email: str = Path(min_length=5)) -> dict:
    db = SessionLocal()
    element = UserRepository(db).delete_user(email)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested user was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
        )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)

@user_router.put('/user_role/{email}',response_model=dict,description="Updates the role of a specific user")
def update_role(email: str = Path(min_length=5), role_id: int = Query(...)) -> dict:
    db = SessionLocal()
    element = UserRepository(db).update_role(email, role_id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested user was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
        )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)


# @user_router.put('/{email}',response_model=dict,description="Updates specific user")
# def update_user(email: str = Path(min_length=5), user: User = Body()) -> dict:
#     db = SessionLocal()
#     element = UserRepository(db).update_user(email, user)
#     if not element:        
#         return JSONResponse(
#             content={            
#                 "message": "The requested user was not found",            
#                 "data": None        
#                 }, 
#             status_code=status.HTTP_404_NOT_FOUND
#         )
#     return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)