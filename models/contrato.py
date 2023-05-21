from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .user import User
    from .tipo_contrato import TipoContrato


class Contrato(Base):
    id = Column(Integer, primary_key=True, index=True)
    fechaInicio = Column(Date, index=True)
    fechaFinal = Column(Date, index=True)

    # User
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="contratos")

    # Tipo Contrato
    tipoContrato_id = Column(Integer, ForeignKey("tipoContrato.id"))
    tipoContrato = relationship("TipoContrato", back_populates="contratos")
