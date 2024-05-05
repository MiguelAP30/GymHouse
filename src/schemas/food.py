from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class Food(BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la comida")
    name: str = Field(min_length=4, title="nombre de la comida", max_length=50)
    description: str = Field(min_length=4, title="descripción de la comida ", max_length=500)
    photo: str = Field(title="foto de la comida")
    food_category_id: Optional[int] = Field(title="Id de la categoria de la comida")

    @validator("name")
    def name_must_contain_letter(cls, v):
        assert any(char.isalpha() for char in v), "Must contain a letter"
        return v
    
    @validator("description")
    def description_must_contain_letter(cls, v):
        if v:
            assert any(char.isalpha() for char in v), "Must contain a letter"
        return v
    
    @validator("photo")
    def photo_must_contain_letter(cls, v):
        if v:
            assert any(char.isalpha() for char in v), "Must contain a letter"
        return v
    class Config:
        orm_mode = True