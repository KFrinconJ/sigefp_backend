from typing import Optional

from pydantic import BaseModel


# Shared properties
class SubfuncionSustantivaBase(BaseModel):
    nombre: Optional[str] = None
    horas: Optional[int] = None
    periodo_academico_id: Optional[int] = None
    funcion_sustantiva_id: Optional[int] = None


# Properties to receive via API on creation
class SubfuncionSustantivaCreate(SubfuncionSustantivaBase):
    nombre: str
    horas: int


# Properties to receive via API on update
class SubfuncionSustantivaUpdate(SubfuncionSustantivaBase):
    pass


class SubfuncionSustantivaInDBBase(SubfuncionSustantivaBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class SubfuncionSustantiva(SubfuncionSustantivaInDBBase):
    pass


# Additional properties stored in DB
class SubfuncionSustantivaInDB(SubfuncionSustantivaInDBBase):
    pass
