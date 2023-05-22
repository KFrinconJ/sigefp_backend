from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.nivel import Nivel
from schemas.nivel import NivelBase, NivelUpdate

class CRUDNivel(CRUDBase[Nivel, NivelBase, NivelUpdate]):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[Nivel]:
        return db.query(Nivel).filter(Nivel.nombre == nombre).first()

    def create(self, db: Session, *, obj_in: NivelBase) -> Nivel:
        db_obj = Nivel(nombre=obj_in.nombre)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Nivel, obj_in: Union[NivelUpdate, Dict[str, Any]]
    ) -> Nivel:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)


nivel = CRUDNivel(Nivel)
