from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class Meal(BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la comida")
    plates_id: int = Field(title="Id del plato")
    quantity_food_id: int = Field(title="Id de la cantidad de comida")

    @validator("plates_id")
    def plates_id_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("los platos no deben estar vacios")
        return value
    
    @validator("quantity_food_id")
    def quantity_food_id_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("la cantidad de comida no debe estar vacia")
        return value
    class Config:
        orm_mode = True