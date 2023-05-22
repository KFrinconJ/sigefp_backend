from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

if TYPE_CHECKING:
    from .rol import Rol
    from .contrato import Contrato
    from .vinculacion import Vinculacion
    from .oficina import Oficina
    from .adscripcion import Adscripcion
    from .subfuncion_sustantiva_usuario import SubfuncionSustantivaUsuario
    


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)
    cargo = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    
    #Roles
    rol_id = Column(Integer, ForeignKey("rol.id"))
    rol = relationship("Rol", back_populates="users")

    #Contratos
    contratos = relationship("Contrato", back_populates="user")
    contratos_id = Column(Integer, ForeignKey("contrato.id"))

    #Vinculaciones
    vinculaciones = relationship("Vinculacion", back_populates="user")
    vinculaciones_id = Column(Integer, ForeignKey("vinculacion.id"))
    #Oficinas
    oficinas = relationship("Oficina", back_populates="user")

    #Adscripciones
    adscripciones = relationship("Adscripcion", back_populates="user")

    #Subfunciones
    subfunciones_sustantivas_usuarios = relationship("SubfuncionSustantivaUsuario", back_populates="user")
