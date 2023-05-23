from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .subfuncion_sustantiva import SubfuncionSustantiva


class PeriodoAcademico(Base):
    id = Column(Integer, primary_key=True, index=True)
    fechaInicio = Column(Date, index=True)
    fechaFinal = Column(Date, index=True)
    estado = Column(Boolean, default=True)
    cantidad_semanas = Column(
        Integer,
    )
    nombre = Column(String, index=True)
    horas = Column(
        Integer,
    )
    
    subfunciones_sustantivas = relationship("SubfuncionSustantiva", back_populates="periodo_academico")



    # Registro
    registros = relationship("Registro", back_populates="periodo_academico")
