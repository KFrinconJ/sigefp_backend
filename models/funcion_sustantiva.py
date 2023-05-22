from typing import TYPE_CHECKING

from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .programa_academico import ProgramaAcademico
    from .subfuncion_sustantiva import SubfuncionSustantiva

class FuncionSustantiva(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

    # ProgramaAcademico
    programa_academico_id = Column(Integer, ForeignKey('programaacademico.id'))
    programa_academico = relationship("ProgramaAcademico", back_populates="funciones_sustantivas")
    
    
    #SubfuncionSustantiva
    subfunciones_sustantivas = relationship("SubfuncionSustantiva", back_populates="funcion_sustantiva")

    #Oficina
    oficina_id = Column(Integer, ForeignKey("oficina.id"))
    oficina = relationship("Oficina", back_populates="funciones_sustantivas")
