from fastapi import APIRouter, Body, Depends, Query, Path, Security, status 
from fastapi.responses import JSONResponse 
from typing import Annotated, List 
from fastapi.security import HTTPAuthorizationCredentials 
from fastapi.encoders import jsonable_encoder 
from src.repositories.auth import AuthRepository 
from src.config.database import SessionLocal 
from src.schemas.user import User as UserCreateSchema 
from src.schemas.user import UserLogin as UserLoginSchema 
from src.auth.has_access import has_access, security    
from src.auth import auth_handler

auth_router = APIRouter()

@auth_router.post( "/register", tags=["Autorización"], response_model=dict, description="Registrar un nuevo usuario") 
def register_user(user: UserCreateSchema = Body()) -> dict: 
    try: 
        new_user = AuthRepository().register_user(user) 
        return JSONResponse( 
            content={ 
                "message": "The user was successfully registered", 
                "data": jsonable_encoder(new_user),
                }, 
                status_code=status.HTTP_201_CREATED, 
            ) 
    except Exception as err: 
        return JSONResponse( 
            content={"message": str(err), "data": None}, 
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
        )

@auth_router.post("/login",tags=["Autorización"], response_model=dict, description="Autenticar un usuario") 
def login_user(user: UserLoginSchema) -> dict: 
    access_token, refresh_token = AuthRepository().login_user(user)
    return JSONResponse( 
        content={"access_token": access_token,                      
            "refresh_token": refresh_token}, 
        status_code=status.HTTP_200_OK, 
    )   

@auth_router.get("/refresh_token", tags=["Autorización"], response_model=dict, description="Crear un nuevo token con tiempo de vida extendido") 
def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)) -> dict: 
    refresh_token = credentials.credentials 
    new_token = auth_handler.refresh_token(refresh_token) 
    return {"access_token": new_token}

