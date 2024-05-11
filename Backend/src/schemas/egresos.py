from pydantic import BaseModel, Field, validator, model_validator
from typing import Optional

class Egresos (BaseModel):
    id: Optional[int] = Field(default=None, title="Id del egreso")
    fecha: str = Field(title="Fecha del egreso")
    description: Optional[str] = Field(title="Descripcion del egreso")
    value: float = Field( ge=100, le=5000001,title="Valor del egreso") 
    categoria: Optional[int] = Field(title="Contraseña del egreso")
