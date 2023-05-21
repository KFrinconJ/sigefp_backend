from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .user import User
    from .subfuncion_sustantiva import SubfuncionSustantiva
    

class SubfuncionSustantivaUsuario(Base):
    id = Column(Integer, primary_key=True, index=True)
    
    # User
    usuario = relationship("User", back_populates="subfuncion_sustantiva_usuario")
    id_usuario = Column(Integer, ForeignKey("user.id"))

    # SubfuncionSustantiva
    subfuncion_sustantiva = relationship("SubfuncionSustantiva", back_populates="subfuncion_sustantiva_usuario")
    subfuncion_sustantiva_id = Column(Integer, ForeignKey("subfuncion_sustantiva.id"))

    # Registro
    registro = relationship("Registro", back_populates="subfuncion_sustantiva_usuario")
