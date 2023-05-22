from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.area import Area
from schemas.area import AreaBase, AreaUpdate

class CRUDArea(CRUDBase[Area, AreaBase, AreaUpdate]):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[Area]:
        return db.query(Area).filter(Area.nombre == nombre).first()

    def create(self, db: Session, *, obj_in: AreaBase) -> Area:
        db_obj = Area(nombre=obj_in.nombre)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Area, obj_in: Union[AreaUpdate, Dict[str, Any]]
    ) -> Area:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)


area = CRUDArea(Area)
