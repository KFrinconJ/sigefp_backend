from typing import Optional

from pydantic import BaseModel

# Shared properties
class TipoContratoBase(BaseModel):
    nombre: Optional[str] = None

# Properties to receive on tipo de contrato update
class TipoContratoUpdate(TipoContratoBase):
    pass

# Properties shared by models stored in DB
class TipoContratoInDBBase(TipoContratoBase):
    id: int

    class Config:
        orm_mode = True



