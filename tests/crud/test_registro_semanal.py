from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import crud
import datetime
from schemas.registro_semanal import RegistroSemanalCreate, RegistroSemanalUpdate


def test_create_registro_semanal(db: Session) -> None:
    nombre = "Example"
    fechaInicio = "2023-05-01"
    fechaFinal = "2023-05-07"
    descripcion = "Example description"
    registro_semanal_in = RegistroSemanalCreate(
        nombre=nombre,
        fechaInicio=fechaInicio,
        fechaFinal=fechaFinal,
        descripcion=descripcion,
        estado_id=1,
        registro_id=1,
    )
    registro_semanal = crud.registro_semanal.create(db, obj_in=registro_semanal_in)
    assert registro_semanal.nombre == nombre



def test_get_registro_semanal(db: Session) -> None:
    nombre = "Example"
    fechaInicio = "2023-05-01"
    fechaFinal = "2023-05-07"
    descripcion = "Example description"
    registro_semanal_in = RegistroSemanalCreate(
        nombre=nombre,
        fechaInicio=fechaInicio,
        fechaFinal=fechaFinal,
        descripcion=descripcion,
        estado_id=1,
        registro_id=1,
    )
    registro_semanal = crud.registro_semanal.create(db, obj_in=registro_semanal_in)
    registro_semanal_2 = crud.registro_semanal.get(db, id=registro_semanal.id)
    assert registro_semanal_2
    assert jsonable_encoder(registro_semanal) == jsonable_encoder(registro_semanal_2)


def test_update_registro_semanal(db: Session) -> None:
    nombre = "Example"
    fechaInicio = "2023-05-01"
    fechaFinal = "2023-05-07"
    descripcion = "Example description"
    registro_semanal_in = RegistroSemanalCreate(
        nombre=nombre,
        fechaInicio=fechaInicio,
        fechaFinal=fechaFinal,
        descripcion=descripcion,
        estado_id=1,
        registro_id=1,
    )
    registro_semanal = crud.registro_semanal.create(db, obj_in=registro_semanal_in)
    new_nombre = "New Example"
    new_fechaInicio = "2023-05-08"
    new_fechaFinal = "2023-05-14"
    new_descripcion = "New example description"
    registro_semanal_in_update = RegistroSemanalUpdate(
        nombre=new_nombre,
        fechaInicio=new_fechaInicio,
        fechaFinal=new_fechaFinal,
        descripcion=new_descripcion,
    )
    crud.registro_semanal.update(
        db, db_obj=registro_semanal, obj_in=registro_semanal_in_update
    )
    registro_semanal_2 = crud.registro_semanal.get(db, id=registro_semanal.id)
    assert registro_semanal_2.nombre == new_nombre



def test_delete_registro_semanal(db: Session) -> None:
    nombre = "Example"
    fechaInicio = "2023-05-01"
    fechaFinal = "2023-05-07"
    descripcion = "Example description"
    registro_semanal_in = RegistroSemanalCreate(
        nombre=nombre,
        fechaInicio=fechaInicio,
        fechaFinal=fechaFinal,
        descripcion=descripcion,
        estado_id=1,
        registro_id=1,
    )
    registro_semanal = crud.registro_semanal.create(db, obj_in=registro_semanal_in)
    registro_semanal_2 = crud.registro_semanal.remove(db, id=registro_semanal.id)
    registro_semanal_3 = crud.registro_semanal.get(db, id=registro_semanal.id)
    assert registro_semanal_3 is None
    assert registro_semanal_2.id == registro_semanal.id
    assert registro_semanal_2.nombre == nombre
