from typing import Optional
from datetime import date as Date
from datetime import datetime as DateTime
from pydantic import BaseModel


# Shared properties
class RegistroSemanalBase(BaseModel):
    nombre: Optional[str] = None
    fechaInicio: Optional[Date] = None
    fechaFinal: Optional[Date] = None
    descripcion: Optional[str] = None
    horaEnvio: Optional[DateTime] = None
    estado_id: Optional[int] = None
    registro_id: Optional[int] = None


# Properties to receive via API on creation
class RegistroSemanalCreate(RegistroSemanalBase):
    nombre: str
    fechaInicio: Date
    fechaFinal: Date
    descripcion: str


# Properties to receive via API on update
class RegistroSemanalUpdate(RegistroSemanalBase):
    pass


class RegistroSemanalInDBBase(RegistroSemanalBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class RegistroSemanal(RegistroSemanalInDBBase):
    pass


# Additional properties stored in DB
class RegistroSemanalInDB(RegistroSemanalInDBBase):
    pass
