from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.tag_of_diet import TagOfDiet
from src.models.tag_of_diet import TagOfDiet as tag_of_diets
from src.repositories.tag_of_diet import TagOfDietRepository

tag_of_diet_router = APIRouter(tags=['Etiquetas para dietas'])

#CRUD tag_of_diet

@tag_of_diet_router.get('/',response_model=List[TagOfDiet],description="Returns all tag_of_diet")
def get_diet_tags()-> List[TagOfDiet]:
    db= SessionLocal()
    result = TagOfDietRepository(db).get_all_tag_of_diets()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@tag_of_diet_router.get('/{id}',response_model=TagOfDiet,description="Returns data of one specific tag_of_diet")
def get_tag_of_diet(id: int = Path(ge=1)) -> TagOfDiet:
    db = SessionLocal()
    element=  TagOfDietRepository(db).get_tag_of_diet_by_id(id)
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

@tag_of_diet_router.post('/',response_model=dict,description="Creates a new tag_of_diet")
def create_tag(tag_of_diet: TagOfDiet = Body()) -> dict:
    db= SessionLocal()
    new_tag_of_diet = TagOfDietRepository(db).create_new_tag_of_diet(tag_of_diet)
    return JSONResponse(
        content={        
        "message": "The tag_of_diet was successfully created",        
        "data": jsonable_encoder(new_tag_of_diet)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@tag_of_diet_router.delete('/{id}',response_model=dict,description="Removes specific tag_of_diet")
def remove_tag_of_diet(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    element = TagOfDietRepository(db).delete_tag_of_diet(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested tag_of_diet was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)

@tag_of_diet_router.put('/{id}',response_model=dict,description="Updates specific tag_of_diet")
def update_tag_of_diet(id: int = Path(ge=1), tag_of_diet: TagOfDiet = Body()) -> dict:
    db = SessionLocal()
    element = TagOfDietRepository(db).update_tag_of_diet(id, tag_of_diet)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested tag_of_diet was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )
    return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)
