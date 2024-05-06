from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class TypeQuantity(BaseModel):
    id: Optional[int] = Field(default=None, title="Id del tipo de cantidad")
    name: str = Field(min_length=4, title="nombre del tipo de cantidad", max_length=60)
    description: str = Field(min_length=4, title="Descripcion del tipo de cantidad", max_length=500)

    @validator("name")
    def name_must_not_be_empty(cls, value):
        assert isinstance(value,str), ValueError("el nombre debe ser un string")
        return value
    
    @validator("description")
    def description_must_not_be_empty(cls, value):
        assert isinstance(value,str), ValueError("la descripcion debe ser un string")
        return value
    class Config:
        orm_mode = True