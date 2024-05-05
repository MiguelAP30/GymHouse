from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

class ExcerciseMuscleMachine (BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la maquina de ejercicios")
    excercise_id: int = Field(title="Id del ejercicio")
    muscle_id: int = Field(title="Id del musculo")
    machine_id: int = Field(title="Id de la maquina")
    rate: int = Field(ge=0, le=10,title="Calificacion del ejercicio")
    
    @validator("excercise_id")
    def excercise_id_must_be_positive(cls, value):
        assert value > 0, "El id del ejercicio debe ser positivo"
        return value
    
    @validator("muscle_id")
    def muscle_id_must_be_positive(cls, value):
        assert value > 0, "El id del musculo debe ser positivo"
        return value
    
    @validator("machine_id")
    def machine_id_must_be_positive(cls, value):
        assert value > 0, "El id de la maquina debe ser positivo"
        return value
    
    @validator("rate")
    def rate_must_be_positive(cls, value):
        assert value > 0, "La calificacion debe ser positiva"
        return value

    
    class Config:
        orm_mode = True