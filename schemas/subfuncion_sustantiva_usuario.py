from typing import Optional

from pydantic import BaseModel


# Shared properties
class SubfuncionSustantivaUsuarioBase(BaseModel):
    user_id: Optional[int] = None
    subfuncion_sustantiva_id: Optional[int] = None
    registro_id: Optional[int] = None


# Properties to receive via API on creation
class SubfuncionSustantivaUsuarioCreate(SubfuncionSustantivaUsuarioBase):
    user_id: int
    subfuncion_sustantiva_id: int
    registro_id: int


# Properties to receive via API on update
class SubfuncionSustantivaUsuarioUpdate(SubfuncionSustantivaUsuarioBase):
    pass


class SubfuncionSustantivaUsuarioInDBBase(SubfuncionSustantivaUsuarioBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class SubfuncionSustantivaUsuario(SubfuncionSustantivaUsuarioInDBBase):
    pass


# Additional properties stored in DB
class SubfuncionSustantivaUsuarioInDB(SubfuncionSustantivaUsuarioInDBBase):
    pass
