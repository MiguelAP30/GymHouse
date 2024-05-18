from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class TrainingPlan(BaseModel):
    id: Optional[int] = Field(default=None, title="Id del plan de entrenamiento")
    name: str = Field(min_length=4, title="nombre del plan de entrenamiento", max_length=60)
    description: str = Field(min_length=4, title="Descripcion del plan de entrenamiento", max_length=200)
    tag_of_training_plan_id: int = Field(default=None, title="Id de la etiqueta del plan de entrenamiento")
    exercise_per_week_day_id: int = Field(default=None, title="Id de la tabla de ejercicios por dia de la semana")

    @validator("name")
    def name_must_not_be_empty(cls, value):
        assert isinstance(value,str), ValueError("el nombre debe ser un string")
        return value
    
    @validator("description")
    def description_must_not_be_empty(cls, value):
        assert isinstance(value,str), ValueError("la descripcion debe ser un string")
        return value
    
    @validator("tag_of_training_plan_id")
    def tag_of_training_plan_id_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("el id de la etiqueta del plan de entrenamiento no debe estar vacio")
        return value
    
    @validator("exercise_per_week_day_id")
    def exercise_per_week_day_id_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("el id de la tabla de ejercicios por dia de la semana no debe estar vacio")
        return value
    class Config:
        json_schema_extra = {
            "example": {
                "name": "push pull legs",
                "description": "El push pull legs es un plan de entrenamiento que se basa en dividir los musculos en 3 grupos principales, los musculos que empujan, los musculos que jalan y las piernas",
                "tag_of_training_plan_id": 1,
                "exercise_per_week_day_id": 1
            }
        }