from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class PlatePerWeekDay(BaseModel):
    id: Optional[int] = Field(default=None, title="Id del plato por dia de la semana")
    plate_id: int = Field(title="Id del plato")
    week_day_id: int = Field(title="Id del dia de la semana")
    diet_id: int = Field(title="Id de la dieta")

    @validator("plate_id")
    def plate_id_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("el id del plato no debe estar vacio")
        return value
    
    @validator("week_day_id")
    def week_day_id_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("el id del dia de la semana no debe estar vacio")
        return value
    
    @validator("diet_id")
    def diet_id_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("el id de la dieta no debe estar vacio")
        return value
    class Config:
        orm_mode = True