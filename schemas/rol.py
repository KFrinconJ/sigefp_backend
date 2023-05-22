from typing import Optional

from pydantic import BaseModel


# Shared properties
class RolBase(BaseModel):
    nombre: Optional[str] = None

# Properties to receive on rol update
class RolUpdate(RolBase):
    pass


# Properties shared by models stored in DB
class RolInDBBase(RolBase):
    id: int

    class Config:
        orm_mode = True