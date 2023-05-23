from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.periodo_academico import PeriodoAcademico
from schemas.periodo_academico import PeriodoAcademicoCreate, PeriodoAcademicoUpdate


class CRUDPeriodoAcademico(CRUDBase[PeriodoAcademico, PeriodoAcademicoCreate, PeriodoAcademicoUpdate]):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[PeriodoAcademico]:
        return db.query(PeriodoAcademico).filter(PeriodoAcademico.nombre == nombre).first()

    def get_by_estado(self, db: Session, *, estado: bool) -> Optional[PeriodoAcademico]:
        return db.query(PeriodoAcademico).filter(PeriodoAcademico.estado == estado).first()

    def create(self, db: Session, *, obj_in: PeriodoAcademicoCreate) -> PeriodoAcademico:
        db_obj = PeriodoAcademico(
            fechaInicio=obj_in.fechaInicio,
            fechaFinal=obj_in.fechaFinal,
            cantidad_semanas=obj_in.cantidad_semanas,
            nombre=obj_in.nombre,
            horas=obj_in.horas,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: PeriodoAcademico, obj_in: Union[PeriodoAcademicoUpdate, Dict[str, Any]]
    ) -> PeriodoAcademico:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def remove(self, db: Session, *, id: int) -> PeriodoAcademico:
        obj = db.query(PeriodoAcademico).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_all(self, db: Session) -> List[PeriodoAcademico]:
        return db.query(PeriodoAcademico).all()


periodo_academico = CRUDPeriodoAcademico(PeriodoAcademico)
