from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.registro import Registro
from schemas.registro import RegistroCreate, RegistroUpdate


class CRUDRegistro(CRUDBase[Registro, RegistroCreate, RegistroUpdate]):
    def get_by_cantidad_semanas(self, db: Session, *, cantidad_semanas: int) -> Optional[Registro]:
        return db.query(Registro).filter(Registro.cantidad_semanas == cantidad_semanas).first()

    def get_by_periodo_academico_id(self, db: Session, *, periodo_academico_id: int) -> Optional[Registro]:
        return db.query(Registro).filter(Registro.periodo_academico_id == periodo_academico_id).first()

    def create(self, db: Session, *, obj_in: RegistroCreate) -> Registro:
        db_obj = Registro(
            cantidad_semanas=obj_in.cantidad_semanas,
            periodo_academico_id=obj_in.periodo_academico_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Registro, obj_in: Union[RegistroUpdate, Dict[str, Any]]
    ) -> Registro:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def remove(self, db: Session, *, id: int) -> Registro:
        obj = db.query(Registro).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_all(self, db: Session) -> List[Registro]:
        return db.query(Registro).all()


registro = CRUDRegistro(Registro)
