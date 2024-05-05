from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

class Diet (BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la dieta")
    name: str = Field(min_length=4, max_length=50, title="Nombre de la dieta")
    description: str = Field(min_length=4, max_length=500, title="Descripcion de la dieta")
    