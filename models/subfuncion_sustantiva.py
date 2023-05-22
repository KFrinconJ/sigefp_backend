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
    horas = Column(Integer, index=True)

    # PeridoAcademico
    periodo_academico_id = Column(Integer, ForeignKey('periodoacademico.id'))
    periodo_academico = relationship("PeriodoAcademico", back_populates="subfunciones_sustantivas")

    


    # subfunciones_sustantivas_usuarios = relationship("SubfuncionSustantivaUsuario", back_populates="subfuncion_sustantiva")
    subfunciones_sustantivas_usuarios = relationship("SubfuncionSustantivaUsuario", back_populates="subfuncion_sustantiva")


    funcion_sustantiva_id = Column(Integer, ForeignKey('funcionsustantiva.id'))
    funcion_sustantiva = relationship("FuncionSustantiva", back_populates="subfunciones_sustantivas")