from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

class ExerciseMuscle(BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la maquina de ejercicios")
    specific_muscle_id: str = Field(title="Musculo especifico")
    exercise_id: int = Field(title="Id del ejercicio")
    rate: int = Field(ge=0, le=10,title="Calificacion del ejercicio")
    
    @validator("exercise_id")
    def excercise_id_must_be_positive(cls, value):
        assert value > 0, ValueError("El id del ejercicio debe ser positivo")
        return value
    
    @validator("specific_muscle_id")
    def specific_muscle_id_must_be_positive(cls, value):
        assert value > 0, ValueError("El id del musculo especifico debe ser positivo")
        return value
    
    @validator("rate")
    def rate_must_be_positive(cls, value):
        assert isinstance(value,int), ValueError("La calificacion debe ser un entero")
        return value
    class Config:
        json_schema_extra = {
            "example": {
                "specific_muscle_id": 1,
                "exercise_id": 1,
                "rate": 10
            }
        }