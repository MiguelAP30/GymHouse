from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.muscle import Muscle
from src.models.muscle import Muscle as muscles
from src.repositories.muscle import MuscleRepository

muscle_router = APIRouter(prefix='/muscle', tags=['muscles'])

#CRUD muscle

@muscle_router.get('',response_model=List[Muscle],description="Returns all muscle")
def get_categories()-> List[Muscle]:
    db= SessionLocal()
    result = MuscleRepository(db).get_all_muscles()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@muscle_router.get('{id}',response_model=Muscle,description="Returns data of one specific muscle")
def get_muscle(id: int = Path(ge=1)) -> Muscle:
    db = SessionLocal()
    element=  MuscleRepository(db).get_muscle_by_id(id)
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

@muscle_router.post('',response_model=dict,description="Creates a new muscle")
def create_categorie(muscle: Muscle = Body()) -> dict:
    db= SessionLocal()
    new_muscle = MuscleRepository(db).create_new_muscle(muscle)
    return JSONResponse(
        content={        
        "message": "The muscle was successfully created",        
        "data": jsonable_encoder(new_muscle)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@muscle_router.delete('{id}',response_model=dict,description="Removes specific muscle")
def remove_muscle(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = MuscleRepository(db).delete_muscle(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested muscle was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)

@muscle_router.put('{id}',response_model=dict,description="Updates specific muscle")
def update_muscle(id: int = Path(ge=1), muscle: Muscle = Body()) -> dict:
    db = SessionLocal()
    element = MuscleRepository(db).update_muscle(id, muscle)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested muscle was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)
