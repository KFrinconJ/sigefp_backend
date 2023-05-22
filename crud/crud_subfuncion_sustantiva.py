from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.subfuncion_sustantiva import SubfuncionSustantiva
from schemas.subfuncion_sustantiva import SubfuncionSustantivaCreate, SubfuncionSustantivaUpdate


class CRUDSubfuncionSustantiva(CRUDBase[SubfuncionSustantiva, SubfuncionSustantivaCreate, SubfuncionSustantivaUpdate]):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[SubfuncionSustantiva]:
        return db.query(SubfuncionSustantiva).filter(SubfuncionSustantiva.nombre == nombre).first()

    def get_by_horas(self, db: Session, *, horas: int) -> Optional[SubfuncionSustantiva]:
        return db.query(SubfuncionSustantiva).filter(SubfuncionSustantiva.horas == horas).first()

    def get_by_periodo_academico_id(self, db: Session, *, periodo_academico_id: int) -> Optional[SubfuncionSustantiva]:
        return db.query(SubfuncionSustantiva).filter(SubfuncionSustantiva.periodo_academico_id == periodo_academico_id).first()

    def get_by_funcion_sustantiva_id(self, db: Session, *, funcion_sustantiva_id: int) -> Optional[SubfuncionSustantiva]:
        return db.query(SubfuncionSustantiva).filter(SubfuncionSustantiva.funcion_sustantiva_id == funcion_sustantiva_id).first()

    def create(self, db: Session, *, obj_in: SubfuncionSustantivaCreate) -> SubfuncionSustantiva:
        db_obj = SubfuncionSustantiva(
            nombre=obj_in.nombre,
            horas=obj_in.horas,
            periodo_academico_id=obj_in.periodo_academico_id,
            funcion_sustantiva_id=obj_in.funcion_sustantiva_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: SubfuncionSustantiva, obj_in: Union[SubfuncionSustantivaUpdate, Dict[str, Any]]
    ) -> SubfuncionSustantiva:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def remove(self, db: Session, *, id: int) -> SubfuncionSustantiva:
        obj = db.query(SubfuncionSustantiva).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_all(self, db: Session) -> List[SubfuncionSustantiva]:
        return db.query(SubfuncionSustantiva).all()


subfuncion_sustantiva = CRUDSubfuncionSustantiva(SubfuncionSustantiva)
