from typing import TYPE_CHECKING

from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .programa_academico import ProgramaAcademico


class FuncionSustantiva(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

    # ProgramaAcademico
    programa_academico_id = Column(Integer, ForeignKey("programa_academico.id"))
    programa_academico = relationship("ProgramaAcademico", back_populates="area")
    programa_academico = relationship("ProgramaAcademico", back_populates="funciones_sustantiva")