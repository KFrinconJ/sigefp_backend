from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.estado_semanal import EstadoSemanal
from schemas.estado_semanal import EstadoSemanalBase, EstadoSemanalUpdate

class CRUDEstadoSemanal(CRUDBase[EstadoSemanal, EstadoSemanalBase, EstadoSemanalUpdate]):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[EstadoSemanal]:
        return db.query(EstadoSemanal).filter(EstadoSemanal.nombre == nombre).first()

    def create(self, db: Session, *, obj_in: EstadoSemanalBase) -> EstadoSemanal:
        db_obj = EstadoSemanal(nombre=obj_in.nombre)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: EstadoSemanal, obj_in: Union[EstadoSemanalUpdate, Dict[str, Any]]
    ) -> EstadoSemanal:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)


estado_semanal = CRUDEstadoSemanal(EstadoSemanal)
