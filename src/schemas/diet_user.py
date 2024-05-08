from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

class DietUser (BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la dieta del usuario")
    diet_id: int = Field(title="Id de la dieta")
    user_email: str = Field(title="Email del usuario")
    
    @validator("diet_id")
    def diet_id_must_be_positive(cls, value):
        assert value > 0, "El id de la dieta debe ser positivo"
        return value
    def diet_id_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("El id de la dieta no debe estar vacio")
        return value
    
    @validator("user_email")
    def user_id_must_be_email(cls, value):
        assert "@" in value, "El email del usuario debe ser un email"
        return value
    def user_id_must_not_be_empty(cls, value):
        assert value.strip() != "", ValueError("El email del usuario no debe estar vacio")
        return value
    class Config:
        json_Schema_extra = {
            "example": {
                "diet_id": 1,
                "user_email": "hola@gmail.com"
            }
        }