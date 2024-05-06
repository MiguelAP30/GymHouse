from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

class Diet (BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la dieta")
    name: str = Field(min_length=4, max_length=50, title="Nombre de la dieta")
    description: str = Field(min_length=4, max_length=500, title="Descripcion de la dieta")
    
    @validator("name")
    def name_must_contain_letter(cls, v):
        assert isinstance(v, str), ValueError("el nombre debe ser un string")
        return v
    
    @validator("description")
    def description_must_contain_letter(cls, v):
        if v:
            assert isinstance(v, str), ValueError("la descripcion debe ser un string")
        return v
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Dieta 1",
                "description": "Dieta para bajar de peso"
            }
        }