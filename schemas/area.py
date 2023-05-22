from pydantic import BaseModel
from typing import Optional


class AreaBase(BaseModel):
    nombre: Optional[str] = None


class AreaUpdate(AreaBase):
    pass


class Area(AreaBase):
    id: int

    class Config:
        orm_mode = True
