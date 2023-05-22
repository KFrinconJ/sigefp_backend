from pydantic import BaseModel
from typing import Optional

class EstadoSemanalBase(BaseModel):
    nombre: Optional[str] = None

class EstadoSemanalCreate(EstadoSemanalBase):
    pass

class EstadoSemanalUpdate(EstadoSemanalBase):
    pass

class EstadoSemanal(EstadoSemanalBase):
    id: int

    class Config:
        orm_mode = True
