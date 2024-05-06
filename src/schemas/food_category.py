from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class FoodCategory(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the food category")
    name: str = Field(min_length=4, max_length=60, title="Name of the food category")

    @validator("name")
    def name_must_contain_letter(cls, v):
        assert isinstance(v, str), ValueError("el nombre debe ser un string")
        return v
    
    class Config:
        orm_mode = True