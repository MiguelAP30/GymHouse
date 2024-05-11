from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

class Categoria_Egreso (BaseModel):
    id: Optional[int] = Field(default=None, title="Id de la categoria")
    description: str = Field(min_length=4, max_length=500, title="Descripcion de la categoria")