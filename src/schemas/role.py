from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class Role(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the role")
    name: str
    description: str

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