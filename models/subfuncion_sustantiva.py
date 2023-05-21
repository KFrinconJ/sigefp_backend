from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .periodo_academico import PeriodoAcademico
    from .funcion_sustantiva import FuncionSustantiva
    from .subfuncion_sustantiva_usuario import SubfuncionSustantivaUsuario


class SubfuncionSustantiva(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    horas = Column(Integer, nullable=False)

    # PeridoAcademico
    periodo_academico = relationship(
        "PeriodoAcademico", back_populates="subfuncion_sustantiva"
    )
    periodo_academico_id = Column(Integer, ForeignKey("periodoAcademico.id"))
  
    # FuncionSustantiva
    funcion_sustantiva = relationship( "FuncionSustantiva", back_populates="subfuncion_sustantiva")
    funcion_sustantiva_id = Column(Integer, ForeignKey("funcionSustantiva.id"))

    #SubfuncionSustantivaUsuario
    subfuncion_sustantiva_usuario = relationship(  "SubfuncionSustantivaUsuario", back_populates="subfuncion_sustantiva")