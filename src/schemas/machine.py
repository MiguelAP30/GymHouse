from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class Machine(BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la maquina")
    name: str = Field(min_length=4, title="nombre de la maquina", max_length=50)
    description: str = Field(min_length=4, title="descripción de la maquina ", max_length=500)

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
        orm_mode = True