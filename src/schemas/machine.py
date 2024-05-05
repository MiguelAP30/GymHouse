from pydantic import BaseModel, Field, validator, model_validator
from typing import List, Optional

class Machine(BaseModel):
    id: Optional[int] = Field(default=None, title="Id of the machine")
    name: str = Field(..., title="Name of the machine", max_length=50)

    @validator("name")
    def name_must_contain_letter(cls, v):
        assert any(char.isalpha() for char in v), "Must contain a letter"
        return v
    class Config:
        orm_mode = True