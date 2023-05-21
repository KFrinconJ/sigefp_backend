from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, CHAR
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .user import User


class Rol(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(CHAR, index=True)
    users = relationship("User", back_populates="rol")
