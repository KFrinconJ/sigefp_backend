from typing import Optional

from pydantic import BaseModel


# Shared properties
class AdscripcionBase(BaseModel):
    nombre: Optional[str] = None
    user_id: Optional[int] = None


# Properties to receive via API on creation
class AdscripcionCreate(AdscripcionBase):
    nombre: str


# Properties to receive via API on update
class AdscripcionUpdate(AdscripcionBase):
    pass


class AdscripcionInDBBase(AdscripcionBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Adscripcion(AdscripcionInDBBase):
    pass


# Additional properties stored in DB
class AdscripcionInDB(AdscripcionInDBBase):
    pass
