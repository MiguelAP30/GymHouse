from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.role import Role
from src.models.role import Role as roles
from src.repositories.role import RoleRepository

role_router = APIRouter(prefix='/role', tags=['roles'])

#CRUD role

@role_router.get('',response_model=List[Role],description="Returns all role")
def get_categories()-> List[Role]:
    db= SessionLocal()
    result = RoleRepository(db).get_all_roles()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@role_router.get('{id}',response_model=Role,description="Returns data of one specific role")
def get_role(id: int = Path(ge=1)) -> Role:
    db = SessionLocal()
    element=  RoleRepository(db).get_role_by_id(id)
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

@role_router.post('',response_model=dict,description="Creates a new role")
def create_categorie(role: Role = Body()) -> dict:
    db= SessionLocal()
    new_role = RoleRepository(db).create_new_role(role)
    return JSONResponse(
        content={        
        "message": "The role was successfully created",        
        "data": jsonable_encoder(new_role)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@role_router.delete('{id}',response_model=dict,description="Removes specific role")
def remove_role(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = RoleRepository(db).delete_role(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested role was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content={        
            "message": "The role was successfully removed",        
            "data": jsonable_encoder(element)    
            }, 
        status_code=status.HTTP_200_OK
        )

@role_router.put('{id}',response_model=dict,description="Updates specific role")
def update_role(id: int = Path(ge=1), role: Role = Body()) -> dict:
    db = SessionLocal()
    element = RoleRepository(db).update_role(id, role)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested role was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(
        content={        
            "message": "The role was successfully updated",        
            "data": jsonable_encoder(element)    
            }, 
        status_code=status.HTTP_200_OK
        )