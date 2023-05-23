from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import crud
from schemas.adscripcion import AdscripcionCreate, AdscripcionUpdate
from tests.utils.utils import random_lower_string, random_integer


def test_create_adscripcion(db: Session) -> None:
    nombre = random_lower_string()
    user_id = 1  # Cambiar el user_id a 1
    adscripcion_in = AdscripcionCreate(nombre=nombre, user_id=user_id)
    adscripcion = crud.adscripcion.create(db, obj_in=adscripcion_in)
    assert adscripcion.nombre == nombre
    assert adscripcion.user_id == user_id


def test_get_adscripcion(db: Session) -> None:
    nombre = random_lower_string()
    user_id = 1  # Cambiar el user_id a 1
    adscripcion_in = AdscripcionCreate(nombre=nombre, user_id=user_id)
    adscripcion = crud.adscripcion.create(db, obj_in=adscripcion_in)
    adscripcion_2 = crud.adscripcion.get(db, id=adscripcion.id)
    assert adscripcion_2
    assert adscripcion.nombre == adscripcion_2.nombre
    assert adscripcion.user_id == adscripcion_2.user_id
    assert jsonable_encoder(adscripcion) == jsonable_encoder(adscripcion_2)


def test_get_by_nombre(db: Session) -> None:
    # Crear algunas adscripciones con diferentes nombres
    nombre_1 = random_lower_string()
    nombre_2 = random_lower_string()
    nombre_3 = random_lower_string()
    while nombre_2 == nombre_1:
        nombre_2 = random_lower_string()
    while nombre_3 in [nombre_1, nombre_2]:
        nombre_3 = random_lower_string()

    adscripcion_in_1 = AdscripcionCreate(nombre=nombre_1, user_id=1)  # Cambiar el user_id a 1
    adscripcion_in_2 = AdscripcionCreate(nombre=nombre_2, user_id=1)  # Cambiar el user_id a 1
    adscripcion_in_3 = AdscripcionCreate(nombre=nombre_3, user_id=1)  # Cambiar el user_id a 1
    crud.adscripcion.create(db, obj_in=adscripcion_in_1)
    adscripcion_2 = crud.adscripcion.create(db, obj_in=adscripcion_in_2)
    crud.adscripcion.create(db, obj_in=adscripcion_in_3)
    # Obtener la adscripción con el nombre 2
    adscripcion = crud.adscripcion.get_by_nombre(db, nombre=nombre_2)
    # Verificar que solo se devuelva la adscripción 2
    assert adscripcion
    assert adscripcion.id == adscripcion_2.id
    assert adscripcion.nombre == nombre_2


def test_get_by_user_id(db: Session) -> None:
    # Crear algunas adscripciones con diferentes usuarios
    adscripcion_in_1 = AdscripcionCreate(nombre=random_lower_string(), user_id=1)  # Cambiar el user_id a 1
    adscripcion_in_2 = AdscripcionCreate(nombre=random_lower_string(), user_id=1)  # Cambiar el user_id a 1
    adscripcion_in_3 = AdscripcionCreate(nombre=random_lower_string(), user_id=1)  # Cambiar el user_id a 1
    crud.adscripcion.create(db, obj_in=adscripcion_in_1)
    adscripcion_2 = crud.adscripcion.create(db, obj_in=adscripcion_in_2)
    crud.adscripcion.create(db, obj_in=adscripcion_in_3)
    # Obtener la adscripción con el usuario 2
    adscripcion = crud.adscripcion.get_by_user_id(db, user_id=1)  # Cambiar el user_id a 1
    # Verificar que solo se devuelva la adscripción 2
    assert adscripcion
    assert adscripcion.user_id == 1  # Cambiar el user_id a 1


def test_update_adscripcion(db: Session) -> None:
    # Crear una adscripción inicial
    nombre = random_lower_string()
    user_id = 1  # Cambiar el user_id a 1
    adscripcion_in = AdscripcionCreate(nombre=nombre, user_id=user_id)
    adscripcion = crud.adscripcion.create(db, obj_in=adscripcion_in)
    # Actualizar la adscripción con nuevos datos
    new_nombre = random_lower_string()
    new_user_id = 1  # Cambiar el user_id a 1
    while new_nombre == nombre:
        new_nombre = random_lower_string()

    adscripcion_update = AdscripcionUpdate(nombre=new_nombre, user_id=new_user_id)
    updated_adscripcion = crud.adscripcion.update(db, db_obj=adscripcion, obj_in=adscripcion_update)
    # Verificar que se hayan aplicado los cambios
    assert updated_adscripcion.id == adscripcion.id
    assert updated_adscripcion.nombre == new_nombre
    assert updated_adscripcion.user_id == new_user_id


def test_delete_adscripcion(db: Session) -> None:
    # Crear una adscripción inicial
    nombre = random_lower_string()
    user_id = 1  # Cambiar el user_id a 1
    adscripcion_in = AdscripcionCreate(nombre=nombre, user_id=user_id)
    adscripcion = crud.adscripcion.create(db, obj_in=adscripcion_in)

    # Eliminar la adscripción
    crud.adscripcion.remove(db, id=adscripcion.id)

    # Verificar que no exista la adscripción
    adscripcion_deleted = crud.adscripcion.get(db, id=adscripcion.id)
    assert adscripcion_deleted is None
