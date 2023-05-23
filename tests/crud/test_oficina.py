from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import crud
from schemas.oficina import OficinaCreate, OficinaUpdate
from tests.utils.utils import random_lower_string, random_integer


def test_create_oficina(db: Session) -> None:
    nombre = random_lower_string()
    user_id = 2
    oficina_in = OficinaCreate(nombre=nombre, user_id=user_id)
    oficina = crud.oficina.create(db, obj_in=oficina_in)
    assert oficina.nombre == nombre
    assert oficina.user_id == user_id


def test_get_oficina(db: Session) -> None:
    nombre = random_lower_string()
    user_id = 2
    oficina_in = OficinaCreate(nombre=nombre, user_id=user_id)
    oficina = crud.oficina.create(db, obj_in=oficina_in)
    oficina_2 = crud.oficina.get(db, id=oficina.id)
    assert oficina_2
    assert oficina.nombre == oficina_2.nombre
    assert oficina.user_id == oficina_2.user_id
    assert jsonable_encoder(oficina) == jsonable_encoder(oficina_2)


def test_get_by_nombre(db: Session) -> None:
    # Crear algunas oficinas con diferentes nombres
    nombre_1 = random_lower_string()
    nombre_2 = random_lower_string()
    nombre_3 = random_lower_string()

    oficina_in_1 = OficinaCreate(nombre=nombre_1, user_id=2)
    oficina_in_2 = OficinaCreate(nombre=nombre_2, user_id=2)
    oficina_in_3 = OficinaCreate(nombre=nombre_3, user_id=2)
    crud.oficina.create(db, obj_in=oficina_in_1)
    oficina_2 = crud.oficina.create(db, obj_in=oficina_in_2)
    crud.oficina.create(db, obj_in=oficina_in_3)
    # Obtener la oficina con el nombre 2
    oficina = crud.oficina.get_by_nombre(db, nombre=nombre_2)
    # Verificar que solo se devuelva la oficina 2
    assert oficina
    assert oficina.id == oficina_2.id
    assert oficina.nombre == nombre_2


def test_get_by_user_id(db: Session) -> None:
    # Crear algunas oficinas con diferentes usuarios
    user_id_1 = 2
    user_id_2 = 2
    user_id_3 = 2


    oficina_in_1 = OficinaCreate(nombre=random_lower_string(), user_id=user_id_1)
    oficina_in_2 = OficinaCreate(nombre=random_lower_string(), user_id=user_id_2)
    oficina_in_3 = OficinaCreate(nombre=random_lower_string(), user_id=user_id_3)
    crud.oficina.create(db, obj_in=oficina_in_1)
    oficina_2 = crud.oficina.create(db, obj_in=oficina_in_2)
    crud.oficina.create(db, obj_in=oficina_in_3)
    # Obtener la oficina con el usuario 2
    oficina = crud.oficina.get_by_user_id(db, user_id=user_id_2)
    # Verificar que solo se devuelva la oficina 2
    assert oficina
    assert oficina.user_id == user_id_2


def test_update_oficina(db: Session) -> None:
    # Crear una oficina inicial
    nombre = random_lower_string()
    user_id = 2
    oficina_in = OficinaCreate(nombre=nombre, user_id=user_id)
    oficina = crud.oficina.create(db, obj_in=oficina_in)

    # Actualizar la oficina con nuevos datos
    new_nombre = random_lower_string()
    new_user_id = 2

    oficina_update = OficinaUpdate(nombre=new_nombre, user_id=new_user_id)
    updated_oficina = crud.oficina.update(db, db_obj=oficina, obj_in=oficina_update)

    # Verificar que se hayan aplicado los cambios
    assert updated_oficina.id == oficina.id
    assert updated_oficina.nombre == new_nombre
    assert updated_oficina.user_id == new_user_id


def test_delete_oficina(db: Session) -> None:
    # Crear una oficina inicial
    nombre = random_lower_string()
    user_id = 2
    oficina_in = OficinaCreate(nombre=nombre, user_id=user_id)
    oficina = crud.oficina.create(db, obj_in=oficina_in)

    # Eliminar la oficina
    crud.oficina.remove(db, id=oficina.id)

    # Verificar que no exista la oficina
    deleted_oficina = crud.oficina.get(db, id=oficina.id)
    assert not deleted_oficina
