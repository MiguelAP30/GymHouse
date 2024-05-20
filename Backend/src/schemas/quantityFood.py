from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class QuantityFood(BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la cantidad de comida")
    food_id: int = Field(title="Id de la comida")
    type_quantity_id: int = Field(title="Id del tipo de cantidad")
    meal_id: int = Field(title="Id de la comida")
    value: float = Field(ge=1,title="Valor de la cantidad de comida",le=10000)
    calorie: float = Field(ge=0 , title="Calorias de la cantidad de comida", le=10000)
    protein: float = Field(ge=0, title="Proteinas de la cantidad de comida", le=10000)
    fat: float = Field(ge=0, title="Grasas de la cantidad de comida", le=10000)
    carbohydrate: float = Field(ge=0,title="Carbohidratos de la cantidad de comida", le=10000)

    @validator("value")
    def value_must_be_positive(cls, value):
        assert isinstance(value,float), ValueError("el valor debe ser un float")
        return value
    
    @validator("food_id")
    def food_id_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("la comida no debe estar vacia")
        return value
    
    @validator("type_quantity_id")
    def type_quantity_id_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("el tipo de cantidad no debe estar vacio")
        return value
    
    @validator("calorie")
    def calorie_must_be_positive(cls, value):
        assert isinstance(value,float), ValueError("las calorias deben ser un float")
        return value
    
    @validator("protein")
    def protein_must_be_positive(cls, value):
        assert isinstance(value,float), ValueError("las proteinas deben ser un float")
        return value
    
    @validator("fat")
    def fat_must_be_positive(cls, value):
        assert isinstance(value,float), ValueError("las grasas deben ser un float")
        return value
    
    @validator("carbohydrate")
    def carbohydrate_must_be_positive(cls, value):
        assert isinstance(value,float), ValueError("los carbohidratos deben ser un float")
        return value
    class Config:
        json_schema_extra = {
            "example": {
                "food_id": 1,
                "type_quantity_id": 1,
                "meal_id": 1,
                "value": 200.0,
                "calorie": 100.0,
                "protein": 40,
                "fat": 10.0,
                "carbohydrate": 2.0
            }
        }