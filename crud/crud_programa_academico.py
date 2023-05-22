from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.programa_academico import ProgramaAcademico
from schemas.programa_academico import ProgramaAcademicoCreate, ProgramaAcademicoUpdate


class CRUDProgramaAcademico(CRUDBase[ProgramaAcademico, ProgramaAcademicoCreate, ProgramaAcademicoUpdate]):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[ProgramaAcademico]:
        return db.query(ProgramaAcademico).filter(ProgramaAcademico.nombre == nombre).first()

    def get_by_adscripcion_id(self, db: Session, *, adscripcion_id: int) -> Optional[ProgramaAcademico]:
        return db.query(ProgramaAcademico).filter(ProgramaAcademico.adscripcion_id == adscripcion_id).first()

    def get_by_nivel_id(self, db: Session, *, nivel_id: int) -> Optional[ProgramaAcademico]:
        return db.query(ProgramaAcademico).filter(ProgramaAcademico.nivel_id == nivel_id).first()

    def get_by_modalidad_id(self, db: Session, *, modalidad_id: int) -> Optional[ProgramaAcademico]:
        return db.query(ProgramaAcademico).filter(ProgramaAcademico.modalidad_id == modalidad_id).first()

    def get_by_area_id(self, db: Session, *, area_id: int) -> Optional[ProgramaAcademico]:
        return db.query(ProgramaAcademico).filter(ProgramaAcademico.area_id == area_id).first()

    def create(self, db: Session, *, obj_in: ProgramaAcademicoCreate) -> ProgramaAcademico:
        db_obj = ProgramaAcademico(
            nombre=obj_in.nombre,
            adscripcion_id=obj_in.adscripcion_id,
            nivel_id=obj_in.nivel_id,
            modalidad_id=obj_in.modalidad_id,
            area_id=obj_in.area_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: ProgramaAcademico, obj_in: Union[ProgramaAcademicoUpdate, Dict[str, Any]]
    ) -> ProgramaAcademico:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def remove(self, db: Session, *, id: int) -> ProgramaAcademico:
        obj = db.query(ProgramaAcademico).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_all(self, db: Session) -> List[ProgramaAcademico]:
        return db.query(ProgramaAcademico).all()


programa_academico = CRUDProgramaAcademico(ProgramaAcademico)
