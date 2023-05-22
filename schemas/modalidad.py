from pydantic import BaseModel
from typing import Optional


class ModalidadBase(BaseModel):
    nombre: Optional[str] = None


class ModalidadUpdate(ModalidadBase):
    pass


class Modalidad(ModalidadBase):
    id: int

    class Config:
        orm_mode = True
