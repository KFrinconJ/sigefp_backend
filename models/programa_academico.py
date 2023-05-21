from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .adscripcion import Adscripcion
    from .nivel import Nivel
    from .modalidad import Modalidad
    from .funcion_sustantiva import FuncionSustantiva
    from .area import Area


class ProgramaAcademico(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

    # Adscripcion
    adscripcion_id = Column(Integer, ForeignKey("facultad.id"))
    adscripcion = relationship("Adscripcion", back_populates="programa_academico")

    # Nivel
    nivel_id = Column(Integer, ForeignKey("nivel.id"))
    nivel = relationship("Nivel", back_populates="programa_academico")

    # Modalidad
    modalidad_id = Column(Integer, ForeignKey("modalidad.id"))
    modalidad = relationship("Modalidad", back_populates="programa_academico")

    # Area
    area_id = Column(Integer, ForeignKey("area.id"))
    area = relationship("Area", back_populates="programa_academico")

    # Funcion_sustantiva
    funciones_sustantiva = relationship("FuncionSustantiva", back_populates="programa_academico")