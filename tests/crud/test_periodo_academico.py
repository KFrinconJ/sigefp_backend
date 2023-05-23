from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import crud
from schemas.periodo_academico import PeriodoAcademicoCreate, PeriodoAcademicoUpdate
from tests.utils.utils import random_lower_string, random_integer, random_date


def test_create_periodo_academico(db: Session) -> None:
    fechaInicio = random_date()
    fechaFinal = random_date()
    estado = True
    cantidad_semanas = random_integer()
    nombre = random_lower_string()
    horas = random_integer()
    periodo_academico_in = PeriodoAcademicoCreate(
        fechaInicio=fechaInicio,
        fechaFinal=fechaFinal,
        estado=estado,
        cantidad_semanas=cantidad_semanas,
        nombre=nombre,
        horas=horas,
    )
    periodo_academico = crud.periodo_academico.create(db, obj_in=periodo_academico_in)
    assert periodo_academico.fechaInicio == fechaInicio
    assert periodo_academico.fechaFinal == fechaFinal
    assert periodo_academico.estado == estado
    assert periodo_academico.cantidad_semanas == cantidad_semanas
    assert periodo_academico.nombre == nombre
    assert periodo_academico.horas == horas


def test_get_periodo_academico(db: Session) -> None:
    fechaInicio = random_date()
    fechaFinal = random_date()
    estado = True
    cantidad_semanas = random_integer()
    nombre = random_lower_string()
    horas = random_integer()
    periodo_academico_in = PeriodoAcademicoCreate(
        fechaInicio=fechaInicio,
        fechaFinal=fechaFinal,
        estado=estado,
        cantidad_semanas=cantidad_semanas,
        nombre=nombre,
        horas=horas,
    )
    periodo_academico = crud.periodo_academico.create(db, obj_in=periodo_academico_in)
    periodo_academico_2 = crud.periodo_academico.get(db, id=periodo_academico.id)
    assert periodo_academico_2
    assert periodo_academico.fechaInicio == periodo_academico_2.fechaInicio
    assert periodo_academico.fechaFinal == periodo_academico_2.fechaFinal
    assert periodo_academico.estado == periodo_academico_2.estado
    assert periodo_academico.cantidad_semanas == periodo_academico_2.cantidad_semanas
    assert periodo_academico.nombre == periodo_academico_2.nombre
    assert periodo_academico.horas == periodo_academico_2.horas
    assert jsonable_encoder(periodo_academico) == jsonable_encoder(periodo_academico_2)


def test_get_by_nombre(db: Session) -> None:
    # Crear algunos periodos académicos con diferentes nombres
    nombre_1 = random_lower_string()
    nombre_2 = random_lower_string()
    nombre_3 = random_lower_string()
    while nombre_2 == nombre_1:
        nombre_2 = random_lower_string()
    while nombre_3 in [nombre_1, nombre_2]:
        nombre_3 = random_lower_string()

    periodo_academico_in_1 = PeriodoAcademicoCreate(
        fechaInicio=random_date(),
        fechaFinal=random_date(),
        estado=True,
        cantidad_semanas=random_integer(),
        nombre=nombre_1,
        horas=random_integer(),
    )
    periodo_academico_in_2 = PeriodoAcademicoCreate(
        fechaInicio=random_date(),
        fechaFinal=random_date(),
        estado=True,
        cantidad_semanas=random_integer(),
        nombre=nombre_2,
        horas=random_integer(),
    )
    periodo_academico_in_3 = PeriodoAcademicoCreate(
        fechaInicio=random_date(),
        fechaFinal=random_date(),
        estado=True,
        cantidad_semanas=random_integer(),
        nombre=nombre_3,
        horas=random_integer(),
    )
    crud.periodo_academico.create(db, obj_in=periodo_academico_in_1)
    periodo_academico_2 = crud.periodo_academico.create(
        db, obj_in=periodo_academico_in_2
    )
    crud.periodo_academico.create(db, obj_in=periodo_academico_in_3)
    # Obtener el periodo académico con el nombre 2
    periodo_academico = crud.periodo_academico.get_by_nombre(db, nombre=nombre_2)
    # Verificar que solo se devuelva el periodo académico 2
    assert periodo_academico
    assert periodo_academico.id == periodo_academico_2.id
    assert periodo_academico.nombre == nombre_2


def test_get_by_estado(db: Session) -> None:
    # Crear algunos periodos académicos con diferentes estados
    estado_1 = True
    estado_2 = False

    periodo_academico_in_1 = PeriodoAcademicoCreate(
        fechaInicio=random_date(),
        fechaFinal=random_date(),
        estado=estado_1,
        cantidad_semanas=random_integer(),
        nombre=random_lower_string(),
        horas=random_integer(),
    )
    periodo_academico_in_2 = PeriodoAcademicoCreate(
        fechaInicio=random_date(),
        fechaFinal=random_date(),
        estado=estado_2,
        cantidad_semanas=random_integer(),
        nombre=random_lower_string(),
        horas=random_integer(),
    )
    crud.periodo_academico.create(db, obj_in=periodo_academico_in_1)
    periodo_academico_in_2 = crud.periodo_academico.create(
        db, obj_in=periodo_academico_in_2
    )

    # Obtener el periodo académico con el estado 1
    periodo_academico = crud.periodo_academico.get_by_estado(db, estado=estado_1)

    # Verificar que solo se devuelva el periodo académico 1
    assert periodo_academico
    assert periodo_academico.estado == estado_1


def test_update_periodo_academico(db: Session) -> None:
    # Crear un periodo académico inicial
    fechaInicio = random_date()
    fechaFinal = random_date()
    estado = True
    cantidad_semanas = random_integer()
    nombre = random_lower_string()
    horas = random_integer()
    periodo_academico_in = PeriodoAcademicoCreate(
        fechaInicio=fechaInicio,
        fechaFinal=fechaFinal,
        estado=estado,
        cantidad_semanas=cantidad_semanas,
        nombre=nombre,
        horas=horas,
    )
    periodo_academico = crud.periodo_academico.create(db, obj_in=periodo_academico_in)

    # Actualizar el periodo académico con nuevos datos
    new_fechaInicio = random_date()
    new_fechaFinal = random_date()
    new_estado = False
    new_cantidad_semanas = random_integer()
    new_nombre = random_lower_string()
    new_horas = random_integer()

    while new_fechaInicio == fechaInicio:
        new_fechaInicio = random_date()
    while new_fechaFinal == fechaFinal:
        new_fechaFinal = random_date()
    while new_cantidad_semanas == cantidad_semanas:
        new_cantidad_semanas = random_integer()
    while new_nombre == nombre:
        new_nombre = random_lower_string()
    while new_horas == horas:
        new_horas = random_integer()

    periodo_academico_update = PeriodoAcademicoUpdate(
        fechaInicio=new_fechaInicio,
        fechaFinal=new_fechaFinal,
        estado=new_estado,
        cantidad_semanas=new_cantidad_semanas,
        nombre=new_nombre,
        horas=new_horas,
    )
    updated_periodo_academico = crud.periodo_academico.update(
        db, db_obj=periodo_academico, obj_in=periodo_academico_update
    )

    # Verificar que se hayan aplicado los cambios
    assert updated_periodo_academico.id == periodo_academico.id
    assert updated_periodo_academico.fechaInicio == new_fechaInicio
    assert updated_periodo_academico.fechaFinal == new_fechaFinal
    assert updated_periodo_academico.estado == new_estado
    assert updated_periodo_academico.cantidad_semanas == new_cantidad_semanas
    assert updated_periodo_academico.nombre == new_nombre
    assert updated_periodo_academico.horas == new_horas


def test_delete_periodo_academico(db: Session) -> None:
    # Crear un periodo académico inicial
    fechaInicio = random_date()
    fechaFinal = random_date()
    estado = True
    cantidad_semanas = random_integer()
    nombre = random_lower_string()
    horas = random_integer()
    periodo_academico_in = PeriodoAcademicoCreate(
        fechaInicio=fechaInicio,
        fechaFinal=fechaFinal,
        estado=estado,
        cantidad_semanas=cantidad_semanas,
        nombre=nombre,
        horas=horas,
    )
    periodo_academico = crud.periodo_academico.create(db, obj_in=periodo_academico_in)

    # Eliminar el periodo académico
    crud.periodo_academico.remove(db, id=periodo_academico.id)

    # Verificar que el periodo académico se haya eliminado correctamente
    deleted_periodo_academico = crud.periodo_academico.get(db, id=periodo_academico.id)
    assert deleted_periodo_academico is None
