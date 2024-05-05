from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class QuantityFood(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the quantity food")
    value: float
    food_id: int
    type_quantity_id: int
    calorie: float
    protein: float
    fat: float
    carbohydrate: float

    @validator("value")
    def value_must_be_positive(cls, value):
        assert value > 0, "The value must be positive"
        return value
    
    @validator("food_id")
    def food_id_must_not_be_empty(cls, value):
        assert value.strip() != "", "The food id must not be empty"
        return value
    
    @validator("type_quantity_id")
    def type_quantity_id_must_not_be_empty(cls, value):
        assert value.strip() != "", "The type quantity id must not be empty"
        return value
    
    @validator("calorie")
    def calorie_must_be_positive(cls, value):
        assert value > 0, "The calorie must be positive"
        return value
    
    @validator("protein")
    def protein_must_be_positive(cls, value):
        assert value > 0, "The protein must be positive"
        return value
    
    @validator("fat")
    def fat_must_be_positive(cls, value):
        assert value > 0, "The fat must be positive"
        return value
    
    @validator("carbohydrate")
    def carbohydrate_must_be_positive(cls, value):
        assert value > 0, "The carbohydrate must be positive"
        return value
    class Config:
        orm_mode = True