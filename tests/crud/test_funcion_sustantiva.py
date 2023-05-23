from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import crud
from schemas.funcion_sustantiva import FuncionSustantivaCreate, FuncionSustantivaUpdate
from tests.utils.utils import random_lower_string, random_integer


def test_create_funcion_sustantiva(db: Session) -> None:
    nombre = random_lower_string()
    programa_academico_id = 10
    oficina_id = 2
    funcion_sustantiva_in = FuncionSustantivaCreate(
        nombre=nombre,
        programa_academico_id=programa_academico_id,
        oficina_id=oficina_id,
    )
    funcion_sustantiva = crud.funcion_sustantiva.create(
        db, obj_in=funcion_sustantiva_in
    )
    assert funcion_sustantiva.nombre == nombre
    assert funcion_sustantiva.programa_academico_id == programa_academico_id
    assert funcion_sustantiva.oficina_id == oficina_id


def test_get_funcion_sustantiva(db: Session) -> None:
    nombre = random_lower_string()
    programa_academico_id = 10
    oficina_id = 2
    funcion_sustantiva_in = FuncionSustantivaCreate(
        nombre=nombre,
        programa_academico_id=programa_academico_id,
        oficina_id=oficina_id,
    )
    funcion_sustantiva = crud.funcion_sustantiva.create(
        db, obj_in=funcion_sustantiva_in
    )
    funcion_sustantiva_2 = crud.funcion_sustantiva.get(db, id=funcion_sustantiva.id)
    assert funcion_sustantiva_2
    assert funcion_sustantiva.nombre == funcion_sustantiva_2.nombre
    assert (
        funcion_sustantiva.programa_academico_id
        == funcion_sustantiva_2.programa_academico_id
    )
    assert funcion_sustantiva.oficina_id == funcion_sustantiva_2.oficina_id
    assert jsonable_encoder(funcion_sustantiva) == jsonable_encoder(
        funcion_sustantiva_2
    )


def test_get_by_nombre(db: Session) -> None:
    # Crear algunas funciones sustantivas con diferentes nombres
    nombre_1 = random_lower_string()
    nombre_2 = random_lower_string()
    nombre_3 = random_lower_string()

    funcion_sustantiva_in_1 = FuncionSustantivaCreate(
        nombre=nombre_1, programa_academico_id=7, oficina_id=2
    )
    funcion_sustantiva_in_2 = FuncionSustantivaCreate(
        nombre=nombre_2, programa_academico_id=10, oficina_id=2
    )
    funcion_sustantiva_in_3 = FuncionSustantivaCreate(
        nombre=nombre_3, programa_academico_id=13, oficina_id=2
    )
    crud.funcion_sustantiva.create(db, obj_in=funcion_sustantiva_in_1)
    funcion_sustantiva_2 = crud.funcion_sustantiva.create(
        db, obj_in=funcion_sustantiva_in_2
    )
    crud.funcion_sustantiva.create(db, obj_in=funcion_sustantiva_in_3)
    # Obtener la función sustantiva con el nombre 2
    funcion_sustantiva = crud.funcion_sustantiva.get_by_nombre(db, nombre=nombre_2)
    # Verificar que solo se devuelva la función sustantiva 2
    assert funcion_sustantiva
    assert funcion_sustantiva.id == funcion_sustantiva_2.id
    assert funcion_sustantiva.nombre == nombre_2
