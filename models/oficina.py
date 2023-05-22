from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .user import User
    
class Oficina(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

    #User
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="oficinas")

    #FuncionesSustantivas
    funciones_sustantivas = relationship("FuncionSustantiva", back_populates="oficina")
    