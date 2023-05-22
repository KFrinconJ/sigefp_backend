from typing import Optional
from pydantic import BaseModel


class VinculacionBase(BaseModel):
    nombre: Optional[str] = None


class VinculacionUpdate(VinculacionBase):
    pass


class VinculacionInDB(VinculacionBase):
    id: int

    class Config:
        orm_mode = True
