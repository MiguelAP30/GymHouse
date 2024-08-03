from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class SpecificMuscle(BaseModel):
    id: Optional[int] = Field(default=None, title="Id del músculo específico")
    name: str = Field(title="Nombre del músculo específico")
    muscle_id: int = Field(title="Id del músculo")
    description: str = Field(title="Descripción del músculo específico")
    
    @validator("muscle_id")
    def muscle_id_must_be_positive(cls, value):
        assert value > 0, ValueError("El id del músculo debe ser positivo")
        return value
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Pectoral Mayor",
                "muscle_id": 1,
                "description": "Músculo grande que se encuentra en la parte superior del pecho"
            }
        }