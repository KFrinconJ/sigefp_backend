from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.nivel_programa_academico import NivelProgramaAcademico
from schemas.nivel_programa_academico import (
    NivelProgramaAcademicoBase,
    NivelProgramaAcademicoUpdate,
)


class CRUDNivelProgramaAcademico(
    CRUDBase[
        NivelProgramaAcademico, NivelProgramaAcademicoBase, NivelProgramaAcademicoUpdate
    ]
):
    
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[NivelProgramaAcademico]:
        return db.query(NivelProgramaAcademico).filter(NivelProgramaAcademico.nombre == nombre).first()
    def create(
        self, db: Session, *, obj_in: NivelProgramaAcademicoBase
    ) -> NivelProgramaAcademico:
        db_obj = NivelProgramaAcademico(**obj_in.dict())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: NivelProgramaAcademico,
        obj_in: Union[NivelProgramaAcademicoUpdate, Dict[str, Any]]
    ) -> NivelProgramaAcademico:
        update_data = obj_in.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def delete(self, db: Session, *, id: int) -> NivelProgramaAcademico:
        obj = db.query(NivelProgramaAcademico).get(id)
        db.delete(obj)
        db.commit()
        return obj


nivel_programa_academico = CRUDNivelProgramaAcademico(NivelProgramaAcademico)
