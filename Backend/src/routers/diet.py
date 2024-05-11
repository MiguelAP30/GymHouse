from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.diet import Diet
from src.models.diet import Diet as diets
from src.repositories.diet import DietRepository

diet_router = APIRouter(tags=['Dietas'])

#CRUD diet

@diet_router.get('/',response_model=List[Diet],description="Returns all diet")
def get_diet()-> List[Diet]:
    db= SessionLocal()
    result = DietRepository(db).get_all_diets()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@diet_router.get('/{id}',response_model=Diet,description="Returns specific diet")
def get_diet_by_id(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = DietRepository(db).get_diet_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested diet was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content={        
            "message": "The diet was found successfully",        
            "data": jsonable_encoder(element)    
            }, 
        status_code=status.HTTP_200_OK
        )

@diet_router.post('/',response_model=Diet,description="Creates a new diet")
def create_diet(diet: Diet = Body()) -> dict:
    db= SessionLocal()
    new_diet = DietRepository(db).create_new_diet(diet)
    return JSONResponse(
        content={        
        "message": "The diet was successfully created",        
        "data": jsonable_encoder(new_diet)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@diet_router.delete('/{id}',response_model=dict,description="Removes specific diet")
def remove_diet(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = DietRepository(db).get_diet_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested diet was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    DietRepository(db).delete_diet(id)  
    return JSONResponse(
        content={        
            "message": "The diet was removed successfully",        
            "data": None    
            }, 
        status_code=status.HTTP_200_OK
        )

@diet_router.put('/{id}',response_model=Diet,description="Updates specific diet")
def update_diet(id: int = Path(ge=1), diet: Diet = Body()) -> dict:
    db = SessionLocal()
    element = DietRepository(db).get_diet_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested diet was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    updated_diet = DietRepository(db).update_diet(id, diet)  
    return JSONResponse(
        content={        
            "message": "The diet was updated successfully",        
            "data": jsonable_encoder(updated_diet)    
            }, 
        status_code=status.HTTP_200_OK
        )

