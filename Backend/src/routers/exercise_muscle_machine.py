from fastapi import APIRouter, Body, Depends, Query, Path, status
from fastapi.responses import JSONResponse
from typing import Annotated, List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.repositories.exercise_muscle_machine import ExerciseMuscleMachineRepository
from src.schemas.exercise_muscle_machine import ExerciseMuscleMachine
from src.models.exercise_muscle_machine import ExerciseMuscleMachine as ExcersiceMuscleMachineModel
from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler

exercise_muscle_machine_router = APIRouter(tags=['Máquina para hacer ejercicio por músculo'])

#CRUD exercise_muscle_machine

@exercise_muscle_machine_router.get('/exercises_by_rate',response_model=List[ExerciseMuscleMachine],description="Devuelve ejercicios ordenados según su calificación")
def get_all_excercise_muscle_by_rate(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[ExerciseMuscleMachine]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 2:
            result = ExerciseMuscleMachineRepository(db).get_all_excercise_muscle_by_rate()
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(
                content={            
                    "message": "You do not have the necessary permissions",            
                    "data": None        
                    }, 
                status_code=status.HTTP_401_UNAUTHORIZED
                )

@exercise_muscle_machine_router.get('/exercises_by_machine_and_rate',response_model=List[ExerciseMuscleMachine],description="Devuelve los ejercicios ordenados según su calificación y máquina")
def get_all_excercise_muscle_machine_by_rate(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)])-> List[ExerciseMuscleMachine]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 2:
            result = ExerciseMuscleMachineRepository(db).get_all_excercise_muscle_machine_by_rate()
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
        else:
            return JSONResponse(
                content={            
                    "message": "You do not have the necessary permissions",            
                    "data": None        
                    }, 
                status_code=status.HTTP_401_UNAUTHORIZED
                )

@exercise_muscle_machine_router.get('/{id}',response_model=ExerciseMuscleMachine,description="Devuelve un ejercicio_muscle_machine por id")
def get_excercise_muscle_machine(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> ExerciseMuscleMachine:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 2:
            element = ExerciseMuscleMachineRepository(db).get_excercise_muscle_machine_by_id(id)
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
        else:
            return JSONResponse(
                content={            
                    "message": "You do not have the necessary permissions",            
                    "data": None        
                    }, 
                status_code=status.HTTP_401_UNAUTHORIZED
                )

@exercise_muscle_machine_router.post('/',response_model=dict,description="Crea un nuevo ejercicio_muscle_machine")
def create_excercise_muscle_machine(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], exercise: ExerciseMuscleMachine = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        current_user = payload.get("sub")
        if role_user >= 3:
            new_excercise = ExerciseMuscleMachineRepository(db).create_new_excercise_muscle_machine(exercise)
            return JSONResponse(
                content={        
                "message": "The exercise_muscle_machine was successfully created",        
                "data": jsonable_encoder(new_excercise)    
                }, 
                status_code=status.HTTP_201_CREATED
            )
        else:
            return JSONResponse(
                content={            
                    "message": "You do not have the necessary permissions",            
                    "data": None        
                    }, 
                status_code=status.HTTP_401_UNAUTHORIZED
                )

@exercise_muscle_machine_router.delete('/{id}',response_model=dict,description="Elimina un ejercicio_muscle_machine por id")
def remove_excercise_muscle_machine(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        current_user = payload.get("sub")
        if role_user >= 3:
            element = ExerciseMuscleMachineRepository(db).delete_excercise_muscle_machine(id)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested exercise_muscle_machine was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )    
            return JSONResponse(
                content={        
                "message": "The exercise_muscle_machine was successfully removed",        
                "data": jsonable_encoder(element)    
                }, 
                status_code=status.HTTP_200_OK
            )
        else:
            return JSONResponse(
                content={            
                    "message": "You do not have the necessary permissions",            
                    "data": None        
                    }, 
                status_code=status.HTTP_401_UNAUTHORIZED
                )

@exercise_muscle_machine_router.put('/{id}',response_model=dict,description="Actualiza un ejercicio_muscle_machine por id")
def update_excercise_muscle_machine(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1), exercise: ExerciseMuscleMachine = Body()) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        if role_user >= 3:
            element = ExerciseMuscleMachineRepository(db).update_rate_excercise_muscle_machine(id, exercise)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested exercise_muscle_machine was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )    
            return JSONResponse(
                content={        
                "message": "The exercise_muscle_machine was successfully updated",        
                "data": jsonable_encoder(element)    
                }, 
                status_code=status.HTTP_200_OK
            )
        else:
            return JSONResponse(
                content={            
                    "message": "You do not have the necessary permissions",            
                    "data": None        
                    }, 
                status_code=status.HTTP_401_UNAUTHORIZED
                )
