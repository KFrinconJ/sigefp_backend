from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .nivel import Nivel
    from .programa_academico import ProgramaAcademico


class NivelProgramaAcademico(Base):
    id = Column(Integer, primary_key=True, index=True)
    nivel_id = Column(Integer, ForeignKey("nivel.id"))
    nombre = Column(String, index=True)

    nivel = relationship("Nivel", back_populates="niveles_programas_academicos")