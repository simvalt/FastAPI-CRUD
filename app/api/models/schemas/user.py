from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int]
    name: str
    email: str
    password: str

class UserCount(BaseModel):
    total: int

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
