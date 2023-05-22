from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.modalidad import Modalidad
from schemas.modalidad import ModalidadBase, ModalidadUpdate

class CRUDModalidad(CRUDBase[Modalidad, ModalidadBase, ModalidadUpdate]):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[Modalidad]:
        return db.query(Modalidad).filter(Modalidad.nombre == nombre).first()

    def create(self, db: Session, *, obj_in: ModalidadBase) -> Modalidad:
        db_obj = Modalidad(nombre=obj_in.nombre)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Modalidad, obj_in: Union[ModalidadUpdate, Dict[str, Any]]
    ) -> Modalidad:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)


modalidad = CRUDModalidad(Modalidad)
