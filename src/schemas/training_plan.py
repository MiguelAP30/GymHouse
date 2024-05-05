from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class TrainingPlan(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the training plan")
    name: str
    description: str
    tag_of_training_plan_id: int

    @validator("name")
    def name_must_not_be_empty(cls, value):
        assert value.strip() != "", "The name must not be empty"
        return value
    
    @validator("description")
    def description_must_not_be_empty(cls, value):
        assert value.strip() != "", "The description must not be empty"
        return value
    
    @validator("tag_of_training_plan_id")
    def tag_of_training_plan_id_must_not_be_empty(cls, value):
        assert value.strip() != "", "The tag of training plan id must not be empty"
        return value
    
    class Config:
        orm_mode = True