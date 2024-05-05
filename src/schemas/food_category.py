from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class FoodCategoryBase(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the food category")
    name: str = Field(min_length=4, max_length=60, title="Name of the food category")
    description: str = Field(min_length=4, max_length=500, title="Description of the food category")

    @validator("name")
    def name_must_contain_letter(cls, v):
        assert any(char.isalpha() for char in v), "Must contain a letter"
        return v
    
    @validator("description")
    def description_must_contain_letter(cls, v):
        if v:
            assert any(char.isalpha() for char in v), "Must contain a letter"
        return v