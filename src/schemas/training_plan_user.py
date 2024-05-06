from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class TrainingPlanUser(BaseModel):
    id: Optional[int] = Field(default=None, title="Id del plan de entrenamiento del usuario")
    training_plan_id: int = Field(title="Id del plan de entrenamiento")
    user_id: int = Field(title="Id del usuario")
    status: bool = Field(default=False, title="Estado del plan de entrenamiento")

    @validator("training_plan_id")
    def training_plan_id_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("el id del plan de entrenamiento no debe estar vacio")
        return value
    
    @validator("user_id")
    def user_id_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("el id del usuario no debe estar vacio")
        return value
    class Config:
        orm_mode = True