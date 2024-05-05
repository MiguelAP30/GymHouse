from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class Muscle(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the muscle")
    name: str = Field(..., title="Name of the muscle", max_length=50)
    description: Optional[str] = Field(None, title="Description of the muscle", max_length=150)

    @validator("name")
    def name_must_contain_letter(cls, v):
        assert any(char.isalpha() for char in v), "Must contain a letter"
        return v
    
    @validator("description")
    def description_must_contain_letter(cls, v):
        if v:
            assert any(char.isalpha() for char in v), "Must contain a letter"
        return v
    class Config:
        orm_mode = True
