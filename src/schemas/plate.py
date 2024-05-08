from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class Plate(BaseModel):
    id: int = Field(default=None, title="Id del plato")
    name: str = Field(min_length=4, title="nombre del plato", max_length=50)
    description: str = Field(min_length=4, title="Descripcion del plato", max_length=200)

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
                "name": "Ensalada de pollo",
                "description": "Ensalada de pollo con lechuga, tomate, cebolla, zanahoria y pollo a la plancha"
            }
        }
