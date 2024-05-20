from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

class Diet (BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la dieta")
    name: str = Field(min_length=4, max_length=50, title="Nombre de la dieta")
    description: str = Field(min_length=4, max_length=200, title="Descripcion de la dieta")
    tags_of_diet_id: int = Field(default=None, title="Id de las etiquetas de la dieta")
    user_email : Optional[str] = Field(default=None, title="Email del usuario")
    is_active: Optional[bool] = Field(default=False, title="Estado de la dieta")
    
    @validator("name")
    def name_must_contain_letter(cls, v):
        assert isinstance(v, str), ValueError("el nombre debe ser un string")
        return v
    
    @validator("description")
    def description_must_contain_letter(cls, v):
        if v:
            assert isinstance(v, str), ValueError("la descripcion debe ser un string")
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Dieta cetogenica",
                "description": "Se centra en consumir alimentos bajos en carbohidratos y altos en grasas saludables, lo que lleva al cuerpo a un estado de cetosis donde quema grasa como principal fuente de energía.",
                "tags_of_diet_id": 1,
                "is_active": True
            }
        }