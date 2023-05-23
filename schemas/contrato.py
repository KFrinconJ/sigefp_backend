from typing import Optional
from datetime import date as Date
from pydantic import BaseModel


# Shared properties
class ContratoBase(BaseModel):
    fechaInicio: Optional[Date] = None
    fechaFinal: Optional[Date] = None
    numero: Optional[int] = None
    tipo_contrato_id: Optional[int] = None


# Properties to receive via API on creation
class ContratoCreate(ContratoBase):
    fechaInicio: Date
    fechaFinal: Date
    numero: int
    tipo_contrato_id: int


# Properties to receive via API on update
class ContratoUpdate(ContratoBase):
    pass


class ContratoInDBBase(ContratoBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True




# Additional properties stored in DB
class ContratoInDB(ContratoInDBBase):
    pass


# Additional properties to return via API
class Contrato(ContratoInDBBase):
    pass
