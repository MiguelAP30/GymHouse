from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class PlatePerWeekDay(BaseModel):
    id: Optional[int] = Field(default=None, title="Id del plato por dia de la semana")
    week_day_id: int = Field(title="Id del dia de la semana")
    meal_id: int = Field(title="Id de la comida")
    diet_id: int = Field(title="Id de la dieta")

    @validator("week_day_id")
    def week_day_id_must_not_be_empty(cls, value):
        assert isinstance(value, int) and value > 0, ValueError("el id del dia de la semana debe ser un entero positivo")
        return value
    
    @validator("meal_id")
    def diet_meal_id_must_not_be_empty(cls, value):
        assert isinstance(value, int) and value > 0, ValueError("el id de la dieta de la comida debe ser un entero positivo")
        return value
    
    @validator("diet_id")
    def diet_id_must_not_be_empty(cls, value):
        assert isinstance(value, int) and value > 0, ValueError("el id de la dieta debe ser un entero positivo")
        return value
    
    class Config:
        json_schema_extra = {
            "example": {
                "week_day_id": 1,
                "meal_id": 1,
                "diet_id": 1
            }
        }