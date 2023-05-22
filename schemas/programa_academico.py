from typing import Optional

from pydantic import BaseModel


# Shared properties
class ProgramaAcademicoBase(BaseModel):
    nombre: Optional[str] = None
    adscripcion_id: Optional[int] = None
    nivel_id: Optional[int] = None
    modalidad_id: Optional[int] = None
    area_id: Optional[int] = None


# Properties to receive via API on creation
class ProgramaAcademicoCreate(ProgramaAcademicoBase):
    nombre: str


# Properties to receive via API on update
class ProgramaAcademicoUpdate(ProgramaAcademicoBase):
    pass


class ProgramaAcademicoInDBBase(ProgramaAcademicoBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ProgramaAcademico(ProgramaAcademicoInDBBase):
    pass


# Additional properties stored in DB
class ProgramaAcademicoInDB(ProgramaAcademicoInDBBase):
    pass
