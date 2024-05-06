from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class Role(BaseModel):
    id: Optional[int] = Field(default=None, title="Id del rol")
    name: str = Field(min_length=4, title="nombre del rol", max_length=60)
    description: str = Field(min_length=4, title="Descripcion del rol", max_length=500)

    @validator("name")
    def name_must_be_str(cls, v):
        if not isinstance(v, str):
            raise ValueError("name must be a string")
        return v
    
    @validator("description")
    def description_must_be_str(cls, v):
        if not isinstance(v, str):
            raise ValueError("description must be a string")
        return v
    
    class Config:
        orm_mode = True