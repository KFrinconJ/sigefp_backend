from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .registro_semanal import RegistroSemanal



class EstadoSemanal(Base):
    id = Column(Integer, primary_key=True, index=True)

    estado = Column(Integer, )

    #RegistroSemanal
    registro_semanal = relationship("RegistroSemanal", back_populates="estado_semanal")
