from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.rol import Rol
from schemas.rol import RolBase,RolUpdate

class CRUDRol(CRUDBase[Rol,RolBase,RolUpdate]):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[Rol]:
        return db.query(Rol).filter(Rol.nombre == nombre).first()

    def create(self, db: Session, *, obj_in: RolBase) -> Rol:
        db_obj = Rol(
            nombre=obj_in.nombre,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Rol, obj_in: Union[RolUpdate, Dict[str, Any]]
    ) -> Rol:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)
    

rol = CRUDRol(Rol)