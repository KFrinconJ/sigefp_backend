from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .programa_academico import ProgramaAcademico
    from .user import User


class Adscripcion(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

    # ProgramaAcademico
    programa_academico = relationship("ProgramaAcademico", back_populates="area")

    #User
    user = relationship("User", back_populates="adscripciones")
    user_id = Column(Integer, ForeignKey("user.id"))