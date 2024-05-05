from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class TrainingPlanUser(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the training plan user")
    training_plan_id: int
    user_id: int
    status: bool

    @validator("training_plan_id")
    def training_plan_id_must_not_be_empty(cls, value):
        assert value.strip() != "", "The training plan id must not be empty"
        return value
    
    @validator("user_id")
    def user_id_must_not_be_empty(cls, value):
        assert value.strip() != "", "The user id must not be empty"
        return value
    
    class Config:
        orm_mode = True