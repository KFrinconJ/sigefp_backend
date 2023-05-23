from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import crud
from schemas.registro import RegistroCreate, RegistroUpdate

def test_create_registro(db: Session) -> None:
    cantidad_semanas = 3
    registro_in = RegistroCreate(cantidad_semanas=cantidad_semanas, periodo_academico_id=1)
    registro = crud.registro.create(db, obj_in=registro_in)
    assert registro.cantidad_semanas == cantidad_semanas

def test_get_registro(db: Session) -> None:
    cantidad_semanas = 3
    registro_in = RegistroCreate(cantidad_semanas=cantidad_semanas, periodo_academico_id=1)
    registro = crud.registro.create(db, obj_in=registro_in)
    registro_2 = crud.registro.get(db, id=registro.id)
    assert registro_2
    assert jsonable_encoder(registro) == jsonable_encoder(registro_2)

def test_update_registro(db: Session) -> None:
    cantidad_semanas = 3
    registro_in = RegistroCreate(cantidad_semanas=cantidad_semanas, periodo_academico_id=1)
    registro = crud.registro.create(db, obj_in=registro_in)
    new_cantidad_semanas = 3
    registro_in_update = RegistroUpdate(cantidad_semanas=new_cantidad_semanas)
    crud.registro.update(db, db_obj=registro, obj_in=registro_in_update)
    registro_2 = crud.registro.get(db, id=registro.id)
    assert registro_2.cantidad_semanas == new_cantidad_semanas

def test_delete_registro(db: Session) -> None:
    cantidad_semanas = 3
    registro_in = RegistroCreate(cantidad_semanas=cantidad_semanas, periodo_academico_id=1)
    registro = crud.registro.create(db, obj_in=registro_in)
    registro_2 = crud.registro.remove(db, id=registro.id)
    registro_3 = crud.registro.get(db, id=registro.id)
    assert registro_3 is None
    assert registro_2.id == registro.id
    assert registro_2.cantidad_semanas == cantidad_semanas
