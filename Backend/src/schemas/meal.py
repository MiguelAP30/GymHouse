from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class Meal(BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la comida")
    name: str = Field(min_length=4, title="Nombre de la comida", max_length=50)
    description: str = Field(min_length=4, title="Descripcion de la comida", max_length=200)

    
    @validator("name")
    def name_must_not_be_empty(cls, value):
        assert isinstance(value, str) and value.strip() != "", ValueError("el nombre de la comida debe ser un string no vacio")
        return value
    
    @validator("description")
    def description_must_not_be_empty(cls, value):
        assert isinstance(value, str) and value.strip() != "", ValueError("la descripcion de la comida debe ser un string no vacio")
        return value
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Ensalada de pollo",
                "description": "Ensalada de pollo con lechuga, tomate, cebolla, zanahoria y pollo a la plancha"
            }
        }