from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class User(BaseModel):
    email: str = Field(min_length=8, title="Email del usuario", max_length=150)
    id_number: str = Field(min_length=6, title="Numero de identificacion del usuario", max_length=20)
    password: str = Field(min_length=6,title="Contraseña del usuario", max_length=100)
    name: str = Field(min_length=2, title="Nombre del usuario", max_length=50)
    last_name: str = Field(min_length=2, title="Apellido del usuario", max_length=50)
    phone: str = Field(min_length=8, title="Telefono del usuario", max_length=20)
    address: str = Field(min_length=8, title="Direccion del usuario", max_length=150)
    weight: float = Field(title="Peso del usuario")
    height: float = Field(title="Altura del usuario")
    birth_date: str = Field(title="Fecha de nacimiento del usuario")
    physical_activity: int = Field(title="Actividad fisica del usuario")
    role_id: int = Field(title="Id del rol del usuario")

    @validator("email")
    def email_must_be_str(cls, v):
        assert "@" in v, ValueError("El email del usuario debe ser un email")
        return v
    
    @validator("id_number")
    def id_number_must_be_str(cls, v):
        assert isinstance(v, str), ValueError("El numero de identificacion del usuario debe ser un string")
        return v
    
    @validator("password")
    def password_must_be_str(cls, v):
        assert isinstance(v, str), ValueError("La contraseña del usuario debe ser un string")
        return v
    
    @validator("name")
    def name_must_be_str(cls, v):
        assert isinstance(v, str), ValueError("El nombre del usuario debe ser un string")
        return v
    
    @validator("last_name")
    def last_name_must_be_str(cls, v):
        assert isinstance(v, str), ValueError("El apellido del usuario debe ser un string")
        return v
    
    @validator("phone")
    def phone_must_be_str(cls, v):
        assert isinstance(v, str), ValueError("El telefono del usuario debe ser un string")
        return v
    
    @validator("address")
    def address_must_be_str(cls, v):
        assert isinstance(v, str), ValueError("La direccion del usuario debe ser un string")
        return v
    
    @validator("weight")
    def weight_must_be_float(cls, v):
        assert v > 0, ValueError("El peso debe ser positivo")
        return v
    
    @validator("height")
    def height_must_be_float(cls, v):
        assert v > 0, ValueError("La altura debe ser positiva")
        return v
    
    @validator("birth_date")
    def birth_date_must_be_str(cls, v):
        assert isinstance(v, str), ValueError("La fecha de nacimiento del usuario debe ser un string")
        return v
    
    @validator("physical_activity")
    def physical_activity_must_be_int(cls, v):
        assert isinstance(v, int), ValueError("La actividad fisica del usuario debe ser un entero")
        return v
    
    @validator("role_id")
    def role_id_must_be_int(cls, v):
        assert v > 0, ValueError("El id del rol debe ser positivo")
        return v
    class Config:
        orm_mode = True


