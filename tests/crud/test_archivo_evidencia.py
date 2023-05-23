from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import crud
from schemas.archivo_evidencia import ArchivoEvidenciaCreate, ArchivoEvidenciaUpdate
from tests.utils.utils import random_lower_string

def test_create_archivo_evidencia(db: Session) -> None:
    nombre = "Example"
    ubicacion = "example_location"
    archivo_evidencia_in = ArchivoEvidenciaCreate(nombre=nombre, ubicacion=ubicacion, registro_semanal_id=1)
    archivo_evidencia = crud.archivo_evidencia.create(db, obj_in=archivo_evidencia_in)
    assert archivo_evidencia.nombre == nombre
    assert archivo_evidencia.ubicacion == ubicacion

def test_get_archivo_evidencia(db: Session) -> None:
    nombre = "Example"
    ubicacion = "example_location"
    archivo_evidencia_in = ArchivoEvidenciaCreate(nombre=nombre, ubicacion=ubicacion, registro_semanal_id=1)
    archivo_evidencia = crud.archivo_evidencia.create(db, obj_in=archivo_evidencia_in)
    archivo_evidencia_2 = crud.archivo_evidencia.get(db, id=archivo_evidencia.id)
    assert archivo_evidencia_2
    assert jsonable_encoder(archivo_evidencia) == jsonable_encoder(archivo_evidencia_2)

def test_update_archivo_evidencia(db: Session) -> None:
    nombre = "Example"
    ubicacion = "example_location"
    archivo_evidencia_in = ArchivoEvidenciaCreate(nombre=nombre, ubicacion=ubicacion, registro_semanal_id=1)
    archivo_evidencia = crud.archivo_evidencia.create(db, obj_in=archivo_evidencia_in)
    new_nombre = "New Example"
    new_ubicacion = "new_example_location"
    archivo_evidencia_in_update = ArchivoEvidenciaUpdate(nombre=new_nombre, ubicacion=new_ubicacion)
    crud.archivo_evidencia.update(db, db_obj=archivo_evidencia, obj_in=archivo_evidencia_in_update)
    archivo_evidencia_2 = crud.archivo_evidencia.get(db, id=archivo_evidencia.id)
    assert archivo_evidencia_2.nombre == new_nombre
    assert archivo_evidencia_2.ubicacion == new_ubicacion

def test_delete_archivo_evidencia(db: Session) -> None:
    nombre = "Example"
    ubicacion = "example_location"
    archivo_evidencia_in = ArchivoEvidenciaCreate(nombre=nombre, ubicacion=ubicacion, registro_semanal_id=1)
    archivo_evidencia = crud.archivo_evidencia.create(db, obj_in=archivo_evidencia_in)
    archivo_evidencia_2 = crud.archivo_evidencia.remove(db, id=archivo_evidencia.id)
    archivo_evidencia_3 = crud.archivo_evidencia.get(db, id=archivo_evidencia.id)
    assert archivo_evidencia_3 is None
    assert archivo_evidencia_2.id == archivo_evidencia.id
    assert archivo_evidencia_2.nombre == nombre
