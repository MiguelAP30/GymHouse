from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class PlatePerWeekDay(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the plate per week day")
    plate_id: int
    week_day_id: int
    diet_id: int

    @validator("plate_id")
    def plate_id_must_not_be_empty(cls, value):
        assert value.strip() != "", "The plate id must not be empty"
        return value
    
    @validator("week_day_id")
    def week_day_id_must_not_be_empty(cls, value):
        assert value.strip() != "", "The week day id must not be empty"
        return value
    
    @validator("diet_id")
    def diet_id_must_not_be_empty(cls, value):
        assert value.strip() != "", "The diet id must not be empty"
        return value
    class Config:
        orm_mode = True