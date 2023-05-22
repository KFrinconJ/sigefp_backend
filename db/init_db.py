from sqlalchemy.orm import Session

import crud
import schemas
from core.config import settings
from db.session import engine
from db.base_class import Base


# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    Base.metadata.create_all(bind=engine)

    RolList = ["A", "R", "D", "P"]

    for rol_nombre in RolList:
        rol = crud.rol.get_by_nombre(db, nombre=rol_nombre)
        if not rol:
            rol_in = schemas.RolBase(nombre=rol_nombre)
            rol = crud.rol.create(db, obj_in=rol_in)

    ModalidadList = ["Presencial", "Distancia tradicional", "Distancia virtual"]

    for modalidad_nombre in ModalidadList:
        modalidad = crud.modalidad.get_by_nombre(db, nombre=modalidad_nombre)
        if not modalidad:
            modalidad_in = schemas.ModalidadBase(nombre=modalidad_nombre)
            modalidad = crud.modalidad.create(db, obj_in=modalidad_in)

    NivelList = ["Pregrado", "Posgrado"]

    for nivel_nombre in NivelList:
        nivel = crud.nivel.get_by_nombre(db, nombre=nivel_nombre)
        if not nivel:
            nivel_in = schemas.NivelBase(nombre=nivel_nombre)
            nivel = crud.nivel.create(db, obj_in=nivel_in)

    TipoContratoList = [
        "Obra o Labor",
        "Trabajo a termino fijo",
        "Trabajo a termino indefinido",
        "Aprendizaje",
        "Temporal, Ocasional o Accidental",
    ]

    for tipo_contrato_nombre in TipoContratoList:
        tipo_contrato = crud.tipo_contrato.get_by_nombre(
            db, nombre=tipo_contrato_nombre
        )
        if not tipo_contrato:
            tipo_contrato_in = schemas.TipoContratoBase(nombre=tipo_contrato_nombre)
            tipo_contrato = crud.tipo_contrato.create(db, obj_in=tipo_contrato_in)

    AreaList = [
        "Agronomía, Veterinaria y afines",
        "Bellas Artes",
        "Ciencias de la Educación",
        "Ciencias de la Salud",
        "Ciencias Sociales y Humanas",
        "Economía, Administración, Contaduría y afines",
        "Ingeniería, Arquitectura, Urbanismo y afines",
        "Matemáticas y Ciencias Naturales",
    ]

    for area_nombre in AreaList:
        area = crud.area.get_by_nombre(db, nombre=area_nombre)
        if not area:
            area_in = schemas.AreaBase(nombre=area_nombre)
            area = crud.area.create(db, obj_in=area_in)

    EstadoSemanalList = [
        "Aprobado",
        "Pendiente",
        "Rechazado",
        "Dispobible",
        "No disponible",
    ]

    for estado_semanal_nombre in EstadoSemanalList:
        estado_semanal = crud.estado_semanal.get_by_nombre(
            db, nombre=estado_semanal_nombre
        )
        if not estado_semanal:
            estado_semanal_in = schemas.EstadoSemanalBase(nombre=estado_semanal_nombre)
            estado_semanal = crud.estado_semanal.create(db, obj_in=estado_semanal_in)

    Niveles_dict = {
        1: ["Tecnico", "Tecnologico", "Profesional"],
        2: ["Especializacion", "Maestria", "Doctorado"],
    }

    for nivel_id, niveles_programa_academico in Niveles_dict.items():
        for nivel_programa_academico_nombre in niveles_programa_academico:
            nivel_programa_academico = crud.nivel_programa_academico.get_by_nombre(
                db, nombre=nivel_programa_academico_nombre
            )
            if not nivel_programa_academico:
                nivel_programa_academico_in = schemas.NivelProgramaAcademicoBase(
                    nombre=nivel_programa_academico_nombre, nivel_id=nivel_id
                )
                nivel_programa_academico = crud.nivel_programa_academico.create(
                    db, obj_in=nivel_programa_academico_in
                )

    VinculacionList = [
        "Medio Tiempo",
        "Planta",
        "Tiempo Completo",
        "Hora catedra",
        "Ocasional",
    ]

    for vinculacion_nombre in VinculacionList:
        vinculacion = crud.vinculacion.get_by_nombre(db, nombre=vinculacion_nombre)
        if not vinculacion:
            vinculacion_in = schemas.VinculacionBase(nombre=vinculacion_nombre)
            vinculacion = crud.vinculacion.create(db, obj_in=vinculacion_in)

    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            rol_id=1,
        )
        user = crud.user.create(db, obj_in=user_in)
