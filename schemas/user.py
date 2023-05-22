from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    cargo: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = True
    rol_id: Optional[int] = None
    contratos_id: Optional[int] = None
    vinculaciones_id: Optional[int] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: str
    password: str
    rol_id: int


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
