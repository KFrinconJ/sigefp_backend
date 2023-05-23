from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.adscripcion import Adscripcion
from schemas.adscripcion import AdscripcionCreate, AdscripcionUpdate


class CRUDAdscripcion(CRUDBase[Adscripcion, AdscripcionCreate, AdscripcionUpdate]):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[Adscripcion]:
        return db.query(Adscripcion).filter(Adscripcion.nombre == nombre).first()

    def get_by_user_id(self, db: Session, *, user_id: int) -> Optional[Adscripcion]:
        return db.query(Adscripcion).filter(Adscripcion.user_id == user_id).first()

    def create(self, db: Session, *, obj_in: AdscripcionCreate) -> Adscripcion:
        db_obj = Adscripcion(
            nombre=obj_in.nombre,
            user_id=obj_in.user_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: Adscripcion,
        obj_in: Union[AdscripcionUpdate, Dict[str, Any]]
    ) -> Adscripcion:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def remove(self, db: Session, *, id: int) -> Adscripcion:
        obj = db.query(Adscripcion).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_by_id_usuario(self, db: Session, user_id: int) -> List[Adscripcion]:
        return db.query(Adscripcion).filter(Adscripcion.user_id == user_id).all()

    def get_all(self, db: Session) -> List[Adscripcion]:
        return db.query(Adscripcion).all()


adscripcion = CRUDAdscripcion(Adscripcion)
