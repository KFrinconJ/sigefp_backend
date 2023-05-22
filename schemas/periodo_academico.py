from typing import Optional
from datetime import date as Date

from pydantic import BaseModel


# Shared properties
class PeriodoAcademicoBase(BaseModel):
    fechaInicio: Optional[Date] = None
    fechaFinal: Optional[Date] = None
    estado: Optional[bool] = True
    canitdad_semanas: Optional[int] = None
    nombre: Optional[str] = None
    horas: Optional[int] = None


# Properties to receive via API on creation
class PeriodoAcademicoCreate(PeriodoAcademicoBase):
    fechaInicio: Date
    fechaFinal: Date
    canitdad_semanas: int
    nombre: str
    horas: int


# Properties to receive via API on update
class PeriodoAcademicoUpdate(PeriodoAcademicoBase):
    pass


class PeriodoAcademicoInDBBase(PeriodoAcademicoBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class PeriodoAcademico(PeriodoAcademicoInDBBase):
    pass


# Additional properties stored in DB
class PeriodoAcademicoInDB(PeriodoAcademicoInDBBase):
    pass
