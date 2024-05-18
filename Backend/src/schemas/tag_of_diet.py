from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class TagOfDiet(BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la etiqueta de dieta")
    name: str = Field(title="Nombre de la etiqueta de dieta")
    description : str = Field(title="Descripcion de la etiqueta de dieta")

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
        json_schema_extra = {
            "example": {
                "name": "Dieta de volumen",
                "description": "Dieta para ganar masa muscular"
            }
        }