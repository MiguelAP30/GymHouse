from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class ExercisePerWeekDay(BaseModel):
    id: Optional[int] = Field(default=None, title="Id del ejercicio")
    week_day_id: int = Field(title="Id del dia de la semana")
    detail_exercise_id: int = Field(title="Id del ejercicio en el plan de entrenamiento")

    
    @validator("week_day_id")
    def weekDayId_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("El id del dia de la semana no debe estar vacio")
        return value
    
    @validator("detail_exercise_id")
    def detailExerciseId_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("El id del ejercicio en el plan de entrenamiento no debe estar vacio")
        return value
    class Config:
        json_schema_extra = {
            "example": {
                "week_day_id": 1,
                "detail_exercise_id": 1
            }
        }
