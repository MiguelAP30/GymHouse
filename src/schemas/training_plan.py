from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class TrainingPlan(BaseModel):
    id: Optional[int] = Field(default=None, title="Id del plan de entrenamiento")
    name: str = Field(min_length=4, title="nombre del plan de entrenamiento", max_length=60)
    description: str = Field(min_length=4, title="Descripcion del plan de entrenamiento", max_length=500)
    tag_of_training_plan_id: int = Field(default=None, title="Id de la etiqueta del plan de entrenamiento")

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
    class Config:
        orm_mode = True