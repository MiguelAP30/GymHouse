from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class TrainingPlanExcersice(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the training plan excersice")
    training_plan_id: int
    excersice_id: int
    sets: int
    reps: int
    rest: float

    @validator("sets")
    def sets_must_be_int(cls, v):
        if not isinstance(v, int):
            raise ValueError("sets must be an integer")
        return v
    
    @validator("reps")
    def reps_must_be_int(cls, v):
        if not isinstance(v, int):
            raise ValueError("reps must be an integer")
        return v
    
    @validator("rest")
    def rest_must_be_int(cls, v):
        if not isinstance(v, int):
            raise ValueError("rest must be an integer")
        return v
    
    
    class Config:
        orm_mode = True