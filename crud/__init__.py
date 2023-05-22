from .crud_user import user
from .crud_rol import rol
from .crud_area import area
from .crud_estado_semanal import estado_semanal
from .crud_modalidad import modalidad
from .crud_nivel_programa_academico import nivel_programa_academico
from .crud_nivel import nivel
from .crud_tipo_contrato import tipo_contrato
from .crud_vinculacion import vinculacion

from .crud_adscripcion import adscripcion
from .crud_archivo_evidencia import archivo_evidencia
from .crud_contrato import contrato
from .crud_funcion_sustantiva import funcion_sustantiva
from .crud_oficina import oficina
from .crud_periodo_academico import periodo_academico
from .crud_registro import registro
from .crud_registro_semanal import registro_semanal
from .crud_subfuncion_sustantiva import subfuncion_sustantiva
from .crud_subfuncion_sustantiva_usuario import subfuncion_sustantiva_usuario
from .crud_programa_academico import programa_academico


# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
