from typing import Optional
from sqlalchemy.orm import Session
from models.vinculacion import Vinculacion
from schemas.vinculacion import VinculacionBase, VinculacionUpdate
from crud.base import CRUDBase


class CRUDVinculacion(CRUDBase[Vinculacion, VinculacionBase, VinculacionUpdate]):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[Vinculacion]:
        return db.query(Vinculacion).filter(Vinculacion.nombre == nombre).first()

    def create(self, db: Session, *, obj_in: VinculacionBase) -> Vinculacion:
        db_obj = Vinculacion(nombre=obj_in.nombre)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Vinculacion, obj_in: VinculacionUpdate
    ) -> Vinculacion:
        db_obj.nombre = obj_in.nombre
        db.commit()
        db.refresh(db_obj)
        return db_obj


vinculacion = CRUDVinculacion(Vinculacion)
