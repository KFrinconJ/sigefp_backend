from typing import Optional

from pydantic import BaseModel


# Shared properties
class OficinaBase(BaseModel):
    nombre: Optional[str] = None
    user_id: Optional[int] = None


# Properties to receive via API on creation
class OficinaCreate(OficinaBase):
    nombre: str


# Properties to receive via API on update
class OficinaUpdate(OficinaBase):
    pass


class OficinaInDBBase(OficinaBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Oficina(OficinaInDBBase):
    pass


# Additional properties stored in DB
class OficinaInDB(OficinaInDBBase):
    pass
