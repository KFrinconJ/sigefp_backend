from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .programa_academico import ProgramaAcademico
    from .subfuncion_sustantiva_usuario import SubfuncionSustantivaUsuario


class Registro(Base):
    id = Column(Integer, primary_key=True, index=True)

    cantidad_semanas = Column(Integer, nullable=False)

    # PeriodoAcademico
    periodo_academico = relationship("PeriodoAcademico", back_populates="registro")
    periodo_academico_id = Column(Integer, ForeignKey("periodo_academico.id"))

    #SubfuncionSustantiva_Usuario
    subfuncion_sustantiva_usuario = relationship("SubfuncionSustantivaUsuario", back_populates="registro")
    subfuncion_sustantiva_usuario_id = Column(Integer, ForeignKey("subfuncion_sustantiva_usuario.id"))