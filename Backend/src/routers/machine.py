from fastapi import APIRouter, Body, Depends, Query, Path, status
from fastapi.responses import JSONResponse
from typing import Annotated, List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.machine import Machine
from src.models.machine import Machine as machines
from src.repositories.machine import MachineRepository
from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler

machine_router = APIRouter(tags=['Máquinas'])

#CRUD machine

@machine_router.get('/',response_model=List[Machine],description="Returns all machine")
def get_machines(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[Machine]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            result = MachineRepository(db).get_all_machines()
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@machine_router.get('/{id}',response_model=Machine,description="Returns data of one specific machine")
def get_machine(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> Machine:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            element=  MachineRepository(db).get_machine_by_id(id)
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

@machine_router.post('/',response_model=dict,description="Creates a new machine")
def create_machine(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], machine: Machine = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            new_machine = MachineRepository(db).create_new_machine(machine)
            return JSONResponse(
                content={        
                "message": "The machine was successfully created",        
                "data": jsonable_encoder(new_machine)    
                }, 
                status_code=status.HTTP_201_CREATED
            )
        else:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@machine_router.delete('/{id}',response_model=dict,description="Removes specific machine")
def remove_machine(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            element = MachineRepository(db).delete_machine(id)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested machine was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )    
            return JSONResponse(
                content={        
                "message": "The machine was successfully deleted",        
                "data": None    
                }, 
                status_code=status.HTTP_200_OK
            )
        else:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)

@machine_router.put('/{id}',response_model=dict,description="Updates specific machine")
def update_machine(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1), machine: Machine = Body()) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            updated_machine = MachineRepository(db).update_machine(id, machine)
            if not updated_machine:
                return JSONResponse(
                    content={            
                        "message": "The requested machine was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )    
            return JSONResponse(
                content={        
                "message": "The machine was successfully updated",        
                "data": jsonable_encoder(updated_machine)    
                }, 
                status_code=status.HTTP_200_OK
            )
        else:
            return JSONResponse(content={"message": "You do not have the necessary permissions", "data": None}, status_code=status.HTTP_401_UNAUTHORIZED)