from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.diet_user import DietUser
from src.models.diet_user import DietUser as DietUsers
from src.repositories.diet_user import DietUserRepository

diet_user_router = APIRouter(tags=['diet_users'])

#CRUD diet_user

@diet_user_router.get('/diet-user',response_model=List[DietUser],description="Returns all diet_user")
def get_diet_user()-> List[DietUser]:
    db= SessionLocal()
    result = DietUserRepository(db).get_all_diet_user()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@diet_user_router.post('/diet-user',response_model=DietUser,description="Creates a new diet_user")
def create_diet_user(diet_user: DietUser = Body()) -> dict:
    db= SessionLocal()
    new_diet_user = DietUserRepository(db).create_new_diet_user(diet_user)
    return JSONResponse(
        content={        
        "message": "The diet_user was successfully created",        
        "data": jsonable_encoder(new_diet_user)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@diet_user_router.delete('/diet-user{id}',response_model=dict,description="Removes specific diet_user")
def remove_diet_user(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = DietUserRepository(db).get_diet_user_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested diet_user was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    DietUserRepository(db).delete_diet_user(id)  
    return JSONResponse(
        content={        
            "message": "The diet_user was removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )

@diet_user_router.get('/diet-user{id}',response_model=DietUser,description="Returns specific diet_user")
def get_diet_user_by_id(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = DietUserRepository(db).get_diet_user_by_id(id)
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
            "message": "The diet_user was found successfully",        
            "data": jsonable_encoder(element)    
            }, 
        status_code=status.HTTP_200_OK
        )