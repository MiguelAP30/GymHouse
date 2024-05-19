from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class TrainingPlanUser(BaseModel):
    id: Optional[int] = Field(default=None, title="Id del plan de entrenamiento del usuario")
    training_plan_id: int = Field(title="Id del plan de entrenamiento")
    user_email: str = Field(title="email del usuario")
    status: bool = Field(default=False, title="Estado del plan de entrenamiento")
    class Config:
        json_schema_extra = {
            "example": {
                "training_plan_id": 1,
                "user_email": "hola@gmail.com",
                "status": False
            }
        }