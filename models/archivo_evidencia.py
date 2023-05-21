from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .archivo_evidencia import ArchivoEvidencia


class ArchivoEvidencia(Base):
    id = Column(Integer, primary_key=True, index=True)

    nombre = Column(String, nullable=False)
    ubicacion = Column(String, nullable=False)

    # RegistroSemanal
    registro_semanal = relationship(
        "RegistroSemanal", back_populates="archivo_evidencia"
    )
    registro_semanal_id = Column(Integer, ForeignKey("registro_semanal.id"))
