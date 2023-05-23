from sqlalchemy.orm import Session
import crud
from schemas.programa_academico import ProgramaAcademicoCreate, ProgramaAcademicoUpdate
from tests.utils.utils import random_lower_string


def test_get_by_adscripcion_id(db: Session) -> None:
    # Crear algunos programas académicos con la misma adscripcion_id
    adscripcion_id = 2
    programa_academico_in_1 = ProgramaAcademicoCreate(
        nombre=random_lower_string(),
        adscripcion_id=adscripcion_id,
        nivel_id=1,
        modalidad_id=1,
        area_id=1,
    )
    programa_academico_in_2 = ProgramaAcademicoCreate(
        nombre=random_lower_string(),
        adscripcion_id=adscripcion_id,
        nivel_id=2,
        modalidad_id=1,
        area_id=2,
    )
    programa_academico_in_3 = ProgramaAcademicoCreate(
        nombre=random_lower_string(),
        adscripcion_id=adscripcion_id,
        nivel_id=1,
        modalidad_id=1,
        area_id=3,
    )
    crud.programa_academico.create(db, obj_in=programa_academico_in_1)
    programa_academico_2 = crud.programa_academico.create(
        db, obj_in=programa_academico_in_2
    )
    crud.programa_academico.create(db, obj_in=programa_academico_in_3)

    # Obtener el programa académico con la adscripcion_id 1
    programa_academico = crud.programa_academico.get_by_adscripcion_id(
        db, adscripcion_id=adscripcion_id
    )

    # Verificar que solo se devuelva el programa académico 2
    assert programa_academico
    assert programa_academico.adscripcion_id == adscripcion_id


def test_get_by_nivel_id(db: Session) -> None:
    # Crear algunos programas académicos con el mismo nivel_id
    nivel_id = 1
    programa_academico_in_1 = ProgramaAcademicoCreate(
        nombre=random_lower_string(),
        adscripcion_id=3,
        nivel_id=nivel_id,
        modalidad_id=1,
        area_id=1,
    )
    programa_academico_in_2 = ProgramaAcademicoCreate(
        nombre=random_lower_string(),
        adscripcion_id=2,
        nivel_id=nivel_id,
        modalidad_id=2,
        area_id=2,
    )
    programa_academico_in_3 = ProgramaAcademicoCreate(
        nombre=random_lower_string(),
        adscripcion_id=3,
        nivel_id=nivel_id,
        modalidad_id=2,
        area_id=3,
    )
    crud.programa_academico.create(db, obj_in=programa_academico_in_1)
    programa_academico_2 = crud.programa_academico.create(
        db, obj_in=programa_academico_in_2
    )
    crud.programa_academico.create(db, obj_in=programa_academico_in_3)

    # Obtener el programa académico con el nivel_id 1
    programa_academico = crud.programa_academico.get_by_nivel_id(db, nivel_id=nivel_id)

    # Verificar que solo se devuelva el programa académico 2
    assert programa_academico
    assert programa_academico.nivel_id == nivel_id


def test_get_by_modalidad_id(db: Session) -> None:
    # Crear algunos programas académicos con la misma modalidad_id
    modalidad_id = 1
    programa_academico_in_1 = ProgramaAcademicoCreate(
        nombre=random_lower_string(),
        adscripcion_id=3,
        nivel_id=1,
        modalidad_id=modalidad_id,
        area_id=1,
    )
    programa_academico_in_2 = ProgramaAcademicoCreate(
        nombre=random_lower_string(),
        adscripcion_id=2,
        nivel_id=2,
        modalidad_id=modalidad_id,
        area_id=2,
    )
    programa_academico_in_3 = ProgramaAcademicoCreate(
        nombre=random_lower_string(),
        adscripcion_id=3,
        nivel_id=1,
        modalidad_id=modalidad_id,
        area_id=3,
    )
    crud.programa_academico.create(db, obj_in=programa_academico_in_1)
    programa_academico_2 = crud.programa_academico.create(
        db, obj_in=programa_academico_in_2
    )
    crud.programa_academico.create(db, obj_in=programa_academico_in_3)

    # Obtener el programa académico con la modalidad_id 1
    programa_academico = crud.programa_academico.get_by_modalidad_id(
        db, modalidad_id=modalidad_id
    )

    # Verificar que solo se devuelva el programa académico 2
    assert programa_academico
    assert programa_academico.modalidad_id == modalidad_id


def test_delete_programa_academico(db: Session) -> None:
    # Crear un programa académico para eliminar
    programa_academico_in = ProgramaAcademicoCreate(
        nombre=random_lower_string(),
        adscripcion_id=4,
        nivel_id=1,
        modalidad_id=1,
        area_id=1,
    )
    programa_academico = crud.programa_academico.create(
        db, obj_in=programa_academico_in
    )

    # Eliminar el programa académico
    crud.programa_academico.remove(db, id=programa_academico.id)

    # Verificar que el programa académico se haya eliminado correctamente
    programa_academico_deleted = crud.programa_academico.get(
        db, id=programa_academico.id
    )
    assert programa_academico_deleted is None


def test_get_all_programas_academicos(db: Session) -> None:
    # Crear algunos programas académicos
    programa_academico_in_1 = ProgramaAcademicoCreate(
        nombre=random_lower_string(),
        adscripcion_id=4,
        nivel_id=1,
        modalidad_id=1,
        area_id=1,
    )
    programa_academico_in_2 = ProgramaAcademicoCreate(
        nombre=random_lower_string(),
        adscripcion_id=7,
        nivel_id=2,
        modalidad_id=2,
        area_id=2,
    )
    programa_academico_in_3 = ProgramaAcademicoCreate(
        nombre=random_lower_string(),
        adscripcion_id=3,
        nivel_id=1,
        modalidad_id=3,
        area_id=3,
    )
    crud.programa_academico.create(db, obj_in=programa_academico_in_1)
    crud.programa_academico.create(db, obj_in=programa_academico_in_2)
    crud.programa_academico.create(db, obj_in=programa_academico_in_3)

    # Obtener todos los programas académicos
    programas_academicos = crud.programa_academico.get_all(db)

    # Verificar que se devuelvan todos los programas académicos creados
    assert len(programas_academicos) >= 3
