'''
from fastapi import APIRouter, Body, Depends, Query, Path, status
from fastapi.responses import JSONResponse
from typing import Annotated, List
from fastapi import APIRouter
from src.config.database import SessionLocal 
from fastapi.encoders import jsonable_encoder
from src.repositories.exercise_muscle_machine import ExerciseMuscleMachineRepository
from src.schemas.exercise_muscle import ExerciseMuscle
from models.exercise_muscle import ExerciseMuscle as ExcersiceMuscleMachineModel
from fastapi.security import HTTPAuthorizationCredentials
from src.auth.has_access import security
from src.auth import auth_handler

exercise_muscle_machine_router = APIRouter(tags=['Máquina para hacer ejercicio por músculo'])

#CRUD exercise_muscle_machine

@exercise_muscle_machine_router.get('/exercises_by_rate',response_model=List[ExerciseMuscle],description="Devuelve ejercicios ordenados según su calificación")
def get_all_excercise_muscle_by_rate(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id :int)-> List[ExerciseMuscle]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        if role_user >= 2 and status_user:
            result = ExerciseMuscleMachineRepository(db).get_all_excercise_muscle_by_rate(id)
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
        elif not status_user:
            return JSONResponse(
                content={            
                    "message": "Your account is inactive",            
                    "data": None        
                    }, 
                status_code=status.HTTP_403_FORBIDDEN
                )
        else:
            return JSONResponse(
                content={            
                    "message": "You do not have the necessary permissions",            
                    "data": None        
                    }, 
                status_code=status.HTTP_401_UNAUTHORIZED
                )

@exercise_muscle_machine_router.get('/exercises_by_machine_and_rate',response_model=List[ExerciseMuscle],description="Devuelve los ejercicios ordenados según su calificación y máquina")
def get_all_excercise_muscle_machine_by_rate(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id_machine: int, id_muscle : int)-> List[ExerciseMuscle]:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        if role_user >= 2 and status_user:
            result = ExerciseMuscleMachineRepository(db).get_all_excercise_muscle_machine_by_rate(id_muscle, id_machine)
            return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)
        elif not status_user:
            return JSONResponse(
                content={            
                    "message": "Your account is inactive",            
                    "data": None        
                    }, 
                status_code=status.HTTP_403_FORBIDDEN
                )
        else:
            return JSONResponse(
                content={            
                    "message": "You do not have the necessary permissions",            
                    "data": None        
                    }, 
                status_code=status.HTTP_401_UNAUTHORIZED
                )

@exercise_muscle_machine_router.get('/{id}',response_model=ExerciseMuscle,description="Devuelve un ejercicio-musculo-maquina por id")
def get_excercise_muscle_machine(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> ExerciseMuscle:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        if role_user >= 2 and status_user:
            element = ExerciseMuscleMachineRepository(db).get_excercise_muscle_machine_by_id(id)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested exercise-muscle-machine was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )    
            return JSONResponse(
                content=jsonable_encoder(element),                        
                status_code=status.HTTP_200_OK
                )
        elif not status_user:
            return JSONResponse(
                content={            
                    "message": "Your account is inactive",            
                    "data": None        
                    }, 
                status_code=status.HTTP_403_FORBIDDEN
                )
        else:
            return JSONResponse(
                content={            
                    "message": "You do not have the necessary permissions",            
                    "data": None        
                    }, 
                status_code=status.HTTP_401_UNAUTHORIZED
                )

@exercise_muscle_machine_router.post('/',response_model=dict,description="Crea un nuevo ejercicio-musculo-maquina")
def create_excercise_muscle_machine(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], exercise: ExerciseMuscle = Body()) -> dict:
    db= SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        if role_user >= 3 and status_user:
            new_excercise = ExerciseMuscleMachineRepository(db).create_new_excercise_muscle_machine(exercise)
            return JSONResponse(
                content={        
                "message": "The exercise-muscle-machine was successfully created",        
                "data": jsonable_encoder(new_excercise)    
                }, 
                status_code=status.HTTP_201_CREATED
            )
        elif not status_user:
            return JSONResponse(
                content={            
                    "message": "Your account is inactive",            
                    "data": None        
                    }, 
                status_code=status.HTTP_403_FORBIDDEN
                )
        else:
            return JSONResponse(
                content={            
                    "message": "You do not have the necessary permissions",            
                    "data": None        
                    }, 
                status_code=status.HTTP_401_UNAUTHORIZED
                )

@exercise_muscle_machine_router.delete('/{id}',response_model=dict,description="Elimina un ejercicio-musculo-maquina por id")
def remove_excercise_muscle_machine(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1)) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        if role_user >= 3 and status_user:
            element = ExerciseMuscleMachineRepository(db).delete_excercise_muscle_machine(id)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested exercise-muscle-machine was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )    
            return JSONResponse(
                content={        
                "message": "The exercise-muscle-machine was successfully removed",        
                "data": jsonable_encoder(element)    
                }, 
                status_code=status.HTTP_200_OK
            )
        elif not status_user:
            return JSONResponse(
                content={            
                    "message": "Your account is inactive",            
                    "data": None        
                    }, 
                status_code=status.HTTP_403_FORBIDDEN
                )
        else:
            return JSONResponse(
                content={            
                    "message": "You do not have the necessary permissions",            
                    "data": None        
                    }, 
                status_code=status.HTTP_401_UNAUTHORIZED
                )

@exercise_muscle_machine_router.put('/{id}',response_model=dict,description="Actualiza un ejercicio-musculo-maquina por id")
def update_excercise_muscle_machine(credentials: Annotated[HTTPAuthorizationCredentials,Depends(security)], id: int = Path(ge=1), exercise: ExerciseMuscle = Body()) -> dict:
    db = SessionLocal()
    payload = auth_handler.decode_token(credentials.credentials)
    if payload:
        role_user = payload.get("user.role")
        status_user = payload.get("user.status")
        if role_user >= 3 and status_user:
            element = ExerciseMuscleMachineRepository(db).update_rate_excercise_muscle_machine(id, exercise)
            if not element:        
                return JSONResponse(
                    content={            
                        "message": "The requested exercise-muscle-machine was not found",            
                        "data": None        
                        }, 
                    status_code=status.HTTP_404_NOT_FOUND
                    )    
            return JSONResponse(
                content={        
                "message": "The exercise-muscle-machine was successfully updated",        
                "data": jsonable_encoder(element)    
                }, 
                status_code=status.HTTP_200_OK
            )
        elif not status_user:
            return JSONResponse(
                content={            
                    "message": "Your account is inactive",            
                    "data": None        
                    }, 
                status_code=status.HTTP_403_FORBIDDEN
                )
        else:
            return JSONResponse(
                content={            
                    "message": "You do not have the necessary permissions",            
                    "data": None        
                    }, 
                status_code=status.HTTP_401_UNAUTHORIZED
                )

'''