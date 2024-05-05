from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class Meal(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the meal")
    plates_id: int
    quantity_food_id: int

    @validator("plates_id")
    def plates_id_must_not_be_empty(cls, value):
        assert value.strip() != "", "The plate id must not be empty"
        return value
    
    @validator("quantity_food_id")
    def quantity_food_id_must_not_be_empty(cls, value):
        assert value.strip() != "", "The quantity food id must not be empty"
        return value
    class Config:
        orm_mode = True