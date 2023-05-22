from pydantic import BaseModel
from typing import Optional

class NivelBase(BaseModel):
    nombre: Optional[str] = None

class NivelUpdate(NivelBase):
    pass

class Nivel(NivelBase):
    id: int

    class Config:
        orm_mode = True
