from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class ExercisePerWeekDayBase(BaseModel):
    id: Optional[int] = Field(default=None, title="Id del ejercicio")
    exerciseId: Optional[int] = Field(title="Id del ejercicio")
    weekDayId: Optional[int] = Field(title="Id del dia de la semana")

    @validator("exerciseId")
    def exerciseId_must_not_be_empty(cls, value):
        assert value.strip() != "", "El id del ejercicio no debe estar vacio"
        return value
    
    @validator("weekDayId")
    def weekDayId_must_not_be_empty(cls, value):
        assert value.strip() != "", "El id del dia de la semana no debe estar vacio"
        return value
    class Config:
        orm_mode = True
