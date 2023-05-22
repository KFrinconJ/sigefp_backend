from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .user import User

class Vinculacion(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    
    #User
    user = relationship("User", back_populates="vinculaciones")