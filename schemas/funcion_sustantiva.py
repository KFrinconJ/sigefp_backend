from typing import Optional

from pydantic import BaseModel


# Shared properties
class FuncionSustantivaBase(BaseModel):
    nombre: Optional[str] = None
    programa_academico_id: Optional[int] = None
    oficina_id: Optional[int] = None


# Properties to receive via API on creation
class FuncionSustantivaCreate(FuncionSustantivaBase):
    nombre: str


# Properties to receive via API on update
class FuncionSustantivaUpdate(FuncionSustantivaBase):
    pass


class FuncionSustantivaInDBBase(FuncionSustantivaBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class FuncionSustantiva(FuncionSustantivaInDBBase):
    pass


# Additional properties stored in DB
class FuncionSustantivaInDB(FuncionSustantivaInDBBase):
    pass
