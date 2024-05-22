from fastapi import APIRouter, Body, Depends, Query, Path, status
from fastapi.responses import JSONResponse
from typing import Annotated, List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.tag_of_diet import TagOfDiet
from src.models.tag_of_diet import TagOfDiet as tag_of_diets
from src.repositories.tag_of_diet import TagOfDietRepository
from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler

tag_of_diet_router = APIRouter(tags=['Etiquetas para dietas'])

#CRUD tag_of_diet

@tag_of_diet_router.get('/',response_model=List[TagOfDiet],description="Devuelve todas las etiquetas de dietas")
def get_diet_tags()-> List[TagOfDiet]:
    db= SessionLocal()    
    result = TagOfDietRepository(db).get_all_tag_of_diets()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@tag_of_diet_router.get('/{id}',response_model=TagOfDiet,description="Devuelve la información de una sola etiqueta de dieta")
def get_tag_of_diet(id: int = Path(ge=1)) -> TagOfDiet:
    db = SessionLocal()
    element=  TagOfDietRepository(db).get_tag_of_diet_by_id(id)
    if not element:        
        return JSONResponse(
            content={            
                "message": "The requested tag of diet was not found",            
                "data": None        
                }, 
            status_code=status.HTTP_404_NOT_FOUND
            )    
    return JSONResponse(
        content=jsonable_encoder(element),                        
        status_code=status.HTTP_200_OK
        )

@tag_of_diet_router.post('/',response_model=dict,description="Crea una nueva etiqueta de dieta")
def create_tag(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], tag_of_diet: TagOfDiet = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        user_status = payload.get("user.status")
        if role_user >= 3 and user_status == True:
            new_tag_of_diet = TagOfDietRepository(db).create_new_tag_of_diet(tag_of_diet)
            return JSONResponse(
                content={        
                "message": "The tag of diet was successfully created",        
                "data": jsonable_encoder(new_tag_of_diet)    
                }, 
                status_code=status.HTTP_201_CREATED
            )
        return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
    return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@tag_of_diet_router.delete('/{id}',response_model=dict,description="Elimina una etiqueta de dieta específica")
def remove_tag_of_diet(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        user_status = payload.get("user.status")
        if role_user >= 3 and user_status == True:
            element = TagOfDietRepository(db).delete_tag_of_diet(id)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested tag of diet was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )
            return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)
    return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@tag_of_diet_router.put('/{id}',response_model=dict,description="Actualiza una etiqueta de dieta específica")
def update_tag_of_diet(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1), tag_of_diet: TagOfDiet = Body()) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        user_status = payload.get("user.status")
        if role_user >= 3 and user_status == True:
            element = TagOfDietRepository(db).update_tag_of_diet(id, tag_of_diet)
            if not element:        
                return JSONResponse(
                    content={
                        "message": "The requested tag of diet was not found",            
                        "data": None        
                        },
                    status_code=status.HTTP_404_NOT_FOUND
                    )
            return JSONResponse(content=jsonable_encoder(element), status_code=status.HTTP_200_OK)            
