from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import crud
from schemas.subfuncion_sustantiva import (
    SubfuncionSustantivaCreate,
    SubfuncionSustantivaUpdate,
)
from tests.utils.utils import random_lower_string


def test_create_subfuncion_sustantiva(db: Session) -> None:
    nombre = random_lower_string()
    horas = 10
    subfuncion_sustantiva_in = SubfuncionSustantivaCreate(
        nombre=nombre, horas=horas, periodo_academico_id=1, funcion_sustantiva_id=7
    )
    subfuncion_sustantiva = crud.subfuncion_sustantiva.create(
        db, obj_in=subfuncion_sustantiva_in
    )
    assert subfuncion_sustantiva.nombre == nombre
    assert subfuncion_sustantiva.horas == horas


def test_get_subfuncion_sustantiva(db: Session) -> None:
    nombre = random_lower_string()
    horas = 10
    subfuncion_sustantiva_in = SubfuncionSustantivaCreate(
        nombre=nombre, horas=horas, periodo_academico_id=1, funcion_sustantiva_id=9
    )
    subfuncion_sustantiva = crud.subfuncion_sustantiva.create(
        db, obj_in=subfuncion_sustantiva_in
    )
    subfuncion_sustantiva_2 = crud.subfuncion_sustantiva.get(
        db, id=subfuncion_sustantiva.id
    )
    assert subfuncion_sustantiva_2
    assert jsonable_encoder(subfuncion_sustantiva) == jsonable_encoder(
        subfuncion_sustantiva_2
    )


def test_update_subfuncion_sustantiva(db: Session) -> None:
    nombre = random_lower_string()
    horas = 10
    subfuncion_sustantiva_in = SubfuncionSustantivaCreate(
        nombre=nombre, horas=horas, periodo_academico_id=1, funcion_sustantiva_id=10
    )
    subfuncion_sustantiva = crud.subfuncion_sustantiva.create(
        db, obj_in=subfuncion_sustantiva_in
    )
    new_nombre = random_lower_string()
    new_horas = 20
    subfuncion_sustantiva_in_update = SubfuncionSustantivaUpdate(
        nombre=new_nombre, horas=new_horas
    )
    crud.subfuncion_sustantiva.update(
        db, db_obj=subfuncion_sustantiva, obj_in=subfuncion_sustantiva_in_update
    )
    subfuncion_sustantiva_2 = crud.subfuncion_sustantiva.get(
        db, id=subfuncion_sustantiva.id
    )
    assert subfuncion_sustantiva_2.nombre == new_nombre
    assert subfuncion_sustantiva_2.horas == new_horas


def test_delete_subfuncion_sustantiva(db: Session) -> None:
    nombre = random_lower_string()
    horas = 10
    subfuncion_sustantiva_in = SubfuncionSustantivaCreate(
        nombre=nombre, horas=horas, periodo_academico_id=1, funcion_sustantiva_id=11
    )
    subfuncion_sustantiva = crud.subfuncion_sustantiva.create(
        db, obj_in=subfuncion_sustantiva_in
    )
    subfuncion_sustantiva_2 = crud.subfuncion_sustantiva.remove(
        db, id=subfuncion_sustantiva.id
    )
    subfuncion_sustantiva_3 = crud.subfuncion_sustantiva.get(
        db, id=subfuncion_sustantiva.id
    )
    assert subfuncion_sustantiva_3 is None
    assert subfuncion_sustantiva_2.id == subfuncion_sustantiva.id
    assert subfuncion_sustantiva_2.nombre == nombre
