from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class TagOfTrainingPlan(BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la etiqueta del plan de entrenamiento")
    name: str = Field(min_length=4, title="nombre de la etiqueta del plan de entrenamiento", max_length=60)
    description: str = Field(min_length=4, title="Descripcion de la etiqueta del plan de entrenamiento", max_length=500)

    @validator("name")
    def name_must_be_str(cls, v):
        if not isinstance(v, str):
            raise ValueError("el nombre debe ser un string")
        return v
    
    @validator("description")
    def description_must_be_str(cls, v):
        if not isinstance(v, str):
            raise ValueError("la descripcion debe ser un string")
        return v
    
    class Config:
        orm_mode = True