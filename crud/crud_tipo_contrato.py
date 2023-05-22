from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from crud.base import CRUDBase
from models.tipo_contrato import TipoContrato
from schemas.tipo_contrato import TipoContratoBase, TipoContratoUpdate

class CRUDTipoContrato(CRUDBase[TipoContrato, TipoContratoBase, TipoContratoUpdate]):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[TipoContrato]:
        return db.query(TipoContrato).filter(TipoContrato.nombre == nombre).first()

    def create(self, db: Session, *, obj_in: TipoContratoBase) -> TipoContrato:
        db_obj = TipoContrato(nombre=obj_in.nombre)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: TipoContrato, obj_in: Union[TipoContratoUpdate, Dict[str, Any]]
    ) -> TipoContrato:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)


tipo_contrato = CRUDTipoContrato(TipoContrato)
