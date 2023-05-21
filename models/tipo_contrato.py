from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .contrato import Contrato


class TipoContrato(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    contratos = relationship("Contrato", back_populates="tipoContrato")
