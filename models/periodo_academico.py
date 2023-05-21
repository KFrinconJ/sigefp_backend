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
    canitdad_semanas = Column(Integer, nullable=False)
    nombre = Column(String, index=True)
    horas = Column(Integer, nullable=False)

    # SubfuncionSustantiva
    subfuncion_sustantiva = relationship(
        "SubfuncionSustantiva", back_populates="periodo_academico"
    )
