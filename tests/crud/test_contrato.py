from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import crud
from schemas.contrato import ContratoCreate, ContratoUpdate
from tests.utils.utils import random_integer, random_date
import datetime

def test_create_contrato(db: Session) -> None:
    fechaInicio = random_date()
    fechaFinal = random_date()
    numero = random_integer()
    tipo_contrato_id = 3
    contrato_in = ContratoCreate(
        fechaInicio=fechaInicio,
        fechaFinal=fechaFinal,
        numero=numero,
        tipo_contrato_id=tipo_contrato_id,
    )
    contrato = crud.contrato.create(db, obj_in=contrato_in)
    assert contrato.fechaInicio == fechaInicio
    assert contrato.fechaFinal == fechaFinal
    assert contrato.numero == numero
    assert contrato.tipo_contrato_id == tipo_contrato_id


def test_get_contrato(db: Session) -> None:
    fechaInicio = random_date()
    fechaFinal = random_date()
    numero = random_integer()
    tipo_contrato_id = 3
    contrato_in = ContratoCreate(
        fechaInicio=fechaInicio,
        fechaFinal=fechaFinal,
        numero=numero,
        tipo_contrato_id=tipo_contrato_id,
    )
    contrato = crud.contrato.create(db, obj_in=contrato_in)
    contrato_2 = crud.contrato.get(db, id=contrato.id)
    assert contrato_2
    assert contrato.fechaInicio == contrato_2.fechaInicio
    assert contrato.fechaFinal == contrato_2.fechaFinal
    assert contrato.numero == contrato_2.numero
    assert contrato.tipo_contrato_id == contrato_2.tipo_contrato_id
    assert jsonable_encoder(contrato) == jsonable_encoder(contrato_2)


def test_get_by_fechaInicio(db: Session) -> None:
    # Crear algunos contratos con diferentes fechas de inicio
    contrato_in_1 = ContratoCreate(
        fechaInicio="2021-01-01",
        fechaFinal=random_date(),
        numero=random_integer(),
        tipo_contrato_id=1,
    )
    contrato_in_2 = ContratoCreate(
        fechaInicio="2021-02-01",
        fechaFinal=random_date(),
        numero=random_integer(),
        tipo_contrato_id=4,
    )
    contrato_in_3 = ContratoCreate(
        fechaInicio="2021-03-01",
        fechaFinal=random_date(),
        numero=random_integer(),
        tipo_contrato_id=5,
    )
    contrato_1 = crud.contrato.create(db, obj_in=contrato_in_1)
    contrato_2 = crud.contrato.create(db, obj_in=contrato_in_2)
    contrato_3 = crud.contrato.create(db, obj_in=contrato_in_3)
    # Obtener el contrato con fecha de inicio 2021-02-01
    contrato = crud.contrato.get_by_fechaInicio(db, fechaInicio="2021-02-01")
    # Verificar que solo se devuelva el contrato 2
    assert contrato
    assert contrato.fechaInicio == datetime.date(2021, 2, 1)


def test_get_by_fechaFinal(db: Session) -> None:
    # Crear algunos contratos con diferentes fechas de finalización
    contrato_in_1 = ContratoCreate(
        fechaInicio=random_date(),
        fechaFinal="2021-12-31",
        numero=random_integer(),
        tipo_contrato_id=1,
    )
    contrato_in_2 = ContratoCreate(
        fechaInicio=random_date(),
        fechaFinal="2021-11-30",
        numero=random_integer(),
        tipo_contrato_id=3,
    )
    contrato_in_3 = ContratoCreate(
        fechaInicio=random_date(),
        fechaFinal="2021-10-31",
        numero=random_integer(),
        tipo_contrato_id=4,
    )
    crud.contrato.create(db, obj_in=contrato_in_1)
    crud.contrato.create(db, obj_in=contrato_in_2)
    contrato_3 = crud.contrato.create(db, obj_in=contrato_in_3)
    # Obtener el contrato con fecha de finalización 2021-10-31
    contrato = crud.contrato.get_by_fechaFinal(db, fechaFinal="2021-10-31")
    # Verificar que solo se devuelva el contrato 3
    assert contrato
    assert contrato.fechaFinal == datetime.date(2021, 10, 31)


def test_get_by_numero(db: Session) -> None:
    # Crear algunos contratos con diferentes números
    contrato_in_1 = ContratoCreate(
        fechaInicio=random_date(),
        fechaFinal=random_date(),
        numero=1000,
        tipo_contrato_id=2,
    )
    contrato_in_2 = ContratoCreate(
        fechaInicio=random_date(),
        fechaFinal=random_date(),
        numero=2000,
        tipo_contrato_id=2,
    )
    contrato_in_3 = ContratoCreate(
        fechaInicio=random_date(),
        fechaFinal=random_date(),
        numero=3000,
        tipo_contrato_id=2,
    )
    crud.contrato.create(db, obj_in=contrato_in_1)
    crud.contrato.create(db, obj_in=contrato_in_2)
    contrato_3 = crud.contrato.create(db, obj_in=contrato_in_3)
    # Obtener el contrato con número 3000
    contrato = crud.contrato.get_by_numero(db, numero=3000)
    # Verificar que solo se devuelva el contrato 3
    assert contrato
    assert contrato.numero == 3000


def test_update_contrato(db: Session) -> None:
    fechaInicio = random_date()
    fechaFinal = random_date()
    numero = random_integer()
    tipo_contrato_id = 3
    contrato_in = ContratoCreate(
        fechaInicio=fechaInicio,
        fechaFinal=fechaFinal,
        numero=numero,
        tipo_contrato_id=tipo_contrato_id,
    )
    contrato = crud.contrato.create(db, obj_in=contrato_in)
    fechaInicio_actualizada = random_date()
    contrato_update = ContratoUpdate(fechaInicio=fechaInicio_actualizada)
    contrato_actualizado = crud.contrato.update(
        db, db_obj=contrato, obj_in=contrato_update
    )
    assert contrato_actualizado.fechaInicio == fechaInicio_actualizada
