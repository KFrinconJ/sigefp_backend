from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.funcion_sustantiva import FuncionSustantiva
from schemas.funcion_sustantiva import FuncionSustantivaCreate, FuncionSustantivaUpdate


class CRUDFuncionSustantiva(CRUDBase[FuncionSustantiva, FuncionSustantivaCreate, FuncionSustantivaUpdate]):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[FuncionSustantiva]:
        return db.query(FuncionSustantiva).filter(FuncionSustantiva.nombre == nombre).first()

    def get_by_programa_academico_id(self, db: Session, *, programa_academico_id: int) -> Optional[FuncionSustantiva]:
        return db.query(FuncionSustantiva).filter(FuncionSustantiva.programa_academico_id == programa_academico_id).first()

    def get_by_oficina_id(self, db: Session, *, oficina_id: int) -> Optional[FuncionSustantiva]:
        return db.query(FuncionSustantiva).filter(FuncionSustantiva.oficina_id == oficina_id).first()

    def create(self, db: Session, *, obj_in: FuncionSustantivaCreate) -> FuncionSustantiva:
        db_obj = FuncionSustantiva(
            nombre=obj_in.nombre,
            programa_academico_id=obj_in.programa_academico_id,
            oficina_id=obj_in.oficina_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: FuncionSustantiva, obj_in: Union[FuncionSustantivaUpdate, Dict[str, Any]]
    ) -> FuncionSustantiva:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def remove(self, db: Session, *, id: int) -> FuncionSustantiva:
        obj = db.query(FuncionSustantiva).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_all(self, db: Session) -> List[FuncionSustantiva]:
        return db.query(FuncionSustantiva).all()


funcion_sustantiva = CRUDFuncionSustantiva(FuncionSustantiva)
