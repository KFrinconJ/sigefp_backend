from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .programa_academico import ProgramaAcademico
    from .subfuncion_sustantiva_usuario import SubfuncionSustantivaUsuario


class Registro(Base):
    id = Column(Integer, primary_key=True, index=True)

    cantidad_semanas = Column(Integer, index=True)

    # PeriodoAcademico
    periodo_academico_id = Column(Integer, ForeignKey("periodoacademico.id"))
    periodo_academico = relationship("PeriodoAcademico", back_populates="registros")
    # SubfuncionSustantiva_Usuario
    subfunciones_usuarios = relationship(
        "SubfuncionSustantivaUsuario", back_populates="registro"
    )
    
    #RegistroSemanal
    registro_semanal = relationship("RegistroSemanal", back_populates="registro")