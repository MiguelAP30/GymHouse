from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class User(BaseModel):
    email: str
    id_number: str 
    password: str
    name: str
    last_name: str
    phone: str
    address: str
    weight: float
    height: float
    birth_date: str
    physical_activity: int
    role_id: int

    @validator("email")
    def email_must_not_be_empty(cls, value):
        assert value.strip() != "", "The email must not be empty"
        return value
    
    @validator("id_number")
    def id_number_must_not_be_empty(cls, value):
        assert value.strip() != "", "The id number must not be empty"
        return value
    
    @validator("password")
    def password_must_not_be_empty(cls, value):
        assert value.strip() != "", "The password must not be empty"
        return value
    
    @validator("name")
    def name_must_not_be_empty(cls, value):
        assert value.strip() != "", "The name must not be empty"
        return value
    
    @validator("last_name")
    def last_name_must_not_be_empty(cls, value):
        assert value.strip() != "", "The last name must not be empty"
        return value
    
    @validator("weight")
    def weight_must_not_be_empty(cls, value):
        assert value.strip() != "", "The weight must not be empty"
        return value
    
    @validator("height")
    def height_must_not_be_empty(cls, value):
        assert value.strip() != "", "The height must not be empty"
        return value
    
    @validator("birth_date")
    def birth_date_must_not_be_empty(cls, value):
        assert value.strip() != "", "The birth date must not be empty"
        return value
    
    @validator("physical_activity")
    def physical_activity_must_not_be_empty(cls, value):
        assert value.strip() != "", "The physical activity must not be empty"
        return value
    
    @validator("role_id")
    def role_id_must_not_be_empty(cls, value):
        assert value.strip() != "", "The role id must not be empty"
        return value
    
    class Config:
        orm_mode = True


