from fastapi import APIRouter, Body, Query, Path, status
from fastapi.responses import JSONResponse
from typing import List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.schemas.machine import Machine
from src.models.machine import Machine as machines
from src.repositories.machine import MachineRepository

machine_router = APIRouter(tags=['Máquinas'])

#CRUD machine

@machine_router.get('/',response_model=List[Machine],description="Returns all machine")
def get_categories()-> List[Machine]:
    db= SessionLocal()
    result = MachineRepository(db).get_all_machines()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)

@machine_router.get('/{id}',response_model=Machine,description="Returns data of one specific machine")
def get_machine(id: int = Path(ge=1)) -> Machine:
    db = SessionLocal()
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
def create_categorie(machine: Machine = Body()) -> dict:
    db= SessionLocal()
    new_machine = MachineRepository(db).create_new_machine(machine)
    return JSONResponse(
        content={        
        "message": "The machine was successfully created",        
        "data": jsonable_encoder(new_machine)    
        }, 
        status_code=status.HTTP_201_CREATED
    )

@machine_router.delete('/{id}',response_model=dict,description="Removes specific machine")
def remove_machine(id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
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

@machine_router.put('/{id}',response_model=dict,description="Updates specific machine")
def update_machine(id: int = Path(ge=1), machine: Machine = Body()) -> dict:
    db = SessionLocal()
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