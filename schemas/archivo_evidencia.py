from typing import Optional

from pydantic import BaseModel


# Shared properties
class ArchivoEvidenciaBase(BaseModel):
    nombre: Optional[str] = None
    ubicacion: Optional[str] = None
    registro_semanal_id: Optional[int] = None


# Properties to receive via API on creation
class ArchivoEvidenciaCreate(ArchivoEvidenciaBase):
    nombre: str
    ubicacion: str


# Properties to receive via API on update
class ArchivoEvidenciaUpdate(ArchivoEvidenciaBase):
    pass


class ArchivoEvidenciaInDBBase(ArchivoEvidenciaBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class ArchivoEvidencia(ArchivoEvidenciaInDBBase):
    pass


# Additional properties stored in DB
class ArchivoEvidenciaInDB(ArchivoEvidenciaInDBBase):
    pass
