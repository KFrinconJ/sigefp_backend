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
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="subfunciones_sustantivas_usuarios")

    # SubfuncionSustantiva

    subfuncion_sustantiva_id = Column(Integer, ForeignKey("subfuncionsustantiva.id"))
    subfuncion_sustantiva = relationship(
        "SubfuncionSustantiva", back_populates="subfunciones_sustantivas_usuarios"
    )
    # Registro
    registro_id = Column(Integer, ForeignKey("registro.id"))
    registro = relationship("Registro", back_populates="subfunciones_usuarios")
