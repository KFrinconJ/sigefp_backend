from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.oficina import Oficina
from schemas.oficina import OficinaCreate, OficinaUpdate


class CRUDOficina(CRUDBase[Oficina, OficinaCreate, OficinaUpdate]):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[Oficina]:
        return db.query(Oficina).filter(Oficina.nombre == nombre).first()

    def get_by_user_id(self, db: Session, *, user_id: int) -> Optional[Oficina]:
        return db.query(Oficina).filter(Oficina.user_id == user_id).first()

    def create(self, db: Session, *, obj_in: OficinaCreate) -> Oficina:
        db_obj = Oficina(
            nombre=obj_in.nombre,
            user_id=obj_in.user_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Oficina, obj_in: Union[OficinaUpdate, Dict[str, Any]]
    ) -> Oficina:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def remove(self, db: Session, *, id: int) -> Oficina:
        obj = db.query(Oficina).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_all(self, db: Session) -> List[Oficina]:
        return db.query(Oficina).all()


oficina = CRUDOficina(Oficina)
