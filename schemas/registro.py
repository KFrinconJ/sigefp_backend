from typing import Optional

from pydantic import BaseModel


# Shared properties
class RegistroBase(BaseModel):
    cantidad_semanas: Optional[int] = None
    periodo_academico_id: Optional[int] = None


# Properties to receive via API on creation
class RegistroCreate(RegistroBase):
    cantidad_semanas: int


# Properties to receive via API on update
class RegistroUpdate(RegistroBase):
    pass


class RegistroInDBBase(RegistroBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Registro(RegistroInDBBase):
    pass


# Additional properties stored in DB
class RegistroInDB(RegistroInDBBase):
    pass
