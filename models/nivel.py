from typing import TYPE_CHECKING

from sqlalchemy import  Column, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .programa_academico import ProgramaAcademico


class Nivel(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

    # NivelProgramaAcademico
    niveles_programas_academicos = relationship("NivelProgramaAcademico", back_populates="nivel")
    # ProgramaAcademico
    programa_academico = relationship("ProgramaAcademico", back_populates="nivel")
