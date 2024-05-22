from pydantic import BaseModel, EmailStr, Field, validator, model_validator
from typing import List, Optional

class User(BaseModel):
    email: EmailStr = Field(min_length=6, title="Email del usuario", max_length=250, example="hola@gmail.com")
    id_number: str = Field(min_length=6, title="Numero de identificacion del usuario", max_length=20, example="123456789")
    name: str = Field(min_length=2, title="Nombre del usuario", max_length=50, example="Miguel Angel")
    password: str = Field(min_length=6,title="Contraseña del usuario", max_length=60, example="123456")
    lastname: str = Field(min_length=2, title="Apellido del usuario", max_length=50, example="Perez Clavijo")
    phone: str = Field(min_length=8, title="Telefono del usuario", max_length=20, example="12345678")
    address: Optional[str] = Field(default=None, min_length=8, title="Direccion del usuario", max_length=150, example="Calle 123")
    weight: float = Field(title="Peso del usuario", example=74.5)
    height: float = Field(title="Altura del usuario", example=180)
    birth_date: str = Field(title="Fecha de nacimiento del usuario", example="2003-11-12")
    gender: str = Field(min_length=1,title="Genero del usuario", max_length=1, example="m")
    physical_activity: int = Field(title="Total de días de ejercicio que hace el usuario", ge=0, le=7, example=6)
    role_id: Optional[int] = Field(default= 1, title="Rol del usuario", ge=1, example=1)
    status: Optional[bool] = Field(default= True, title="Estado del usuario", example=True)

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
    
    @validator("lastname")
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
    
    @validator("gender")
    def gender_must_be_str(cls, v):
        assert isinstance(v, str), ValueError("El genero del usuario debe ser un string")
        return v

class UserLogin (BaseModel):
    email: EmailStr = Field(min_length=6, max_length=64, alias="email", title="Correo del usuario")
    password: str = Field(min_length=6, title="Contraseña del usuario")




