from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .item import Item 
    from .rol import Rol
    from .contrato import Contrato
    from .vinculacion import Vinculacion
    from .oficina import Oficina
    from .adscripcion import Adscripcion


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    cargo = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    items = relationship("Item", back_populates="owner")
    
    #Roles
    rol_id = Column(Integer, ForeignKey("rol.id"))
    rol = relationship("Rol", back_populates="users")

    #Contratos
    contratos = relationship("Contrato", back_populates="user")

    #Vinculaciones
    vinculaciones = relationship("Vinculacion", back_populates="user")

    #Oficinas
    oficinas = relationship("Oficina", back_populates="user")

    #Adscripciones
    adscripciones = relationship("Adscripcion", back_populates="user")
