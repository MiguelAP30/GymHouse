from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class TypeQuantity(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the type quantity")
    name: str

    @validator("name")
    def name_must_not_be_empty(cls, value):
        assert value.strip() != "", "The name must not be empty"
        return value
    
    class Config:
        orm_mode = True