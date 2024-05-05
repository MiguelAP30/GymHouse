from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

class DietUser (BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la dieta del usuario")
    diet_id: int = Field(title="Id de la dieta")
    user_id: str = Field(title="Email del usuario")
    
    @validator("diet_id")
    def diet_id_must_be_positive(cls, value):
        assert value > 0, "El id de la dieta debe ser positivo"
        return value
    
    @validator("user_id")
    def user_id_must_be_email(cls, value):
        assert "@" in value, "El email del usuario debe ser un email"
        return value
    
    class Config:
        orm_mode = True