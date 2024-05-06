from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class Food(BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la comida")
    name: str = Field(min_length=4, title="nombre de la comida", max_length=50)
    description: str = Field(min_length=4, title="descripción de la comida ", max_length=500)
    image: str = Field(title="foto de la comida")
    food_category_id: int = Field(title="Id de la categoria de la comida")

    @validator("name")
    def name_must_contain_letter(cls, v):
        assert isinstance(v, str), ValueError("el nombre debe ser un string")
        return v
    
    @validator("description")
    def description_must_contain_letter(cls, v):
        if v:
            assert isinstance(v, str), ValueError("la descripcion debe ser un string")
        return v
    
    @validator("food_category_id")
    def food_category_id_must_be_int(cls, v):
        assert v.strip() != "", ValueError("el id de la categoria de la comida no debe estar vacio")
        return v
    
    class Config:
        orm_mode = True