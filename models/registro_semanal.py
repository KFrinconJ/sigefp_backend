from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, Date
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .programa_academico import ProgramaAcademico
    from .subfuncion_sustantiva import SubfuncionSustantiva


class RegistroSemanal(Base):
    id = Column(Integer, primary_key=True, index=True)

    nombre = Column(String, index=True)
    fechaInicio = Column(Date, index=True)
    fechaFinal = Column(Date, index=True)

    descripcion = Column(String, index=True)
    horaEnvio = Column(Integer, nullable=False)

    # EstadoSemanal
    estado_id = Column(Integer, ForeignKey("estado_semanal.id"))
    estado = relationship("EstadoSemanal", back_populates="registro_semanal")
    # SubfuncionSustantiva
    SubfuncionSustantiva = relationship(
        "SubfuncionSustantiva", back_populates="registro_semanal"
    )
    SubfuncionSustantiva_id = Column(Integer, ForeignKey("subfuncion_sustantiva.id"))
