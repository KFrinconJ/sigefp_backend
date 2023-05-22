from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey, DateTime, String, Date
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .programa_academico import ProgramaAcademico
    from .subfuncion_sustantiva import SubfuncionSustantiva
    from .estado_semanal import EstadoSemanal


class RegistroSemanal(Base):
    id = Column(Integer, primary_key=True, index=True)

    nombre = Column(String, index=True)
    fechaInicio = Column(Date, index=True)
    fechaFinal = Column(Date, index=True)

    descripcion = Column(String, index=True)
    horaEnvio = Column(DateTime, index=True)

    # EstadoSemanal
    estado_id = Column(Integer, ForeignKey("estadosemanal.id"))
    estado_semanal = relationship("EstadoSemanal", back_populates="registro_semanal")

    #Registro
    registro_id = Column(Integer, ForeignKey("registro.id"))
    registro = relationship("Registro", back_populates="registro_semanal")

    #Archivo
    archivo_evidencia = relationship("ArchivoEvidencia", back_populates="registro_semanal")



