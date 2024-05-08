from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

class DietMeal(BaseModel):
    id: Optional[int] = Field(default=None, title="Id de dieta de comida")
    diet_id: int = Field(title="Id de la dieta")
    meal_id: int = Field(title="Id de la comida")

    @validator("diet_id")
    def diet_id_must_be_positive(cls, value):
        assert value > 0, "El id de la dieta debe ser positivo"
        return value
    
    @validator("meal_id")
    def meal_id_must_be_positive(cls, value):
        assert value > 0, "El id de la comida debe ser positivo"
        return value

    class Config:
        json_Schema_extra = {
            "example": {
                "diet_id": 1,
                "meal_id": 1
            }
        }