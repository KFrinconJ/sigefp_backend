from typing import Any, Dict, Optional, Union, List
from datetime import date as Date

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.contrato import Contrato
from schemas.contrato import ContratoCreate, ContratoUpdate


class CRUDContrato(CRUDBase[Contrato, ContratoCreate, ContratoUpdate]):
    def get_by_fechaInicio(self, db: Session, *, fechaInicio: Date) -> Optional[Contrato]:
        return db.query(Contrato).filter(Contrato.fechaInicio == fechaInicio).first()

    def get_by_fechaFinal(self, db: Session, *, fechaFinal: Date) -> Optional[Contrato]:
        return db.query(Contrato).filter(Contrato.fechaFinal == fechaFinal).first()

    def get_by_numero(self, db: Session, *, numero: int) -> Optional[Contrato]:
        return db.query(Contrato).filter(Contrato.numero == numero).first()

    def get_by_tipo_contrato_id(self, db: Session, *, tipo_contrato_id: int) -> Optional[Contrato]:
        return db.query(Contrato).filter(Contrato.tipo_contrato_id == tipo_contrato_id).first()

    def create(self, db: Session, *, obj_in: ContratoCreate) -> Contrato:
        db_obj = Contrato(
            fechaInicio=obj_in.fechaInicio,
            fechaFinal=obj_in.fechaFinal,
            numero=obj_in.numero,
            tipo_contrato_id=obj_in.tipo_contrato_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Contrato, obj_in: Union[ContratoUpdate, Dict[str, Any]]
    ) -> Contrato:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def remove(self, db: Session, *, id: int) -> Contrato:
        obj = db.query(Contrato).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_all(self, db: Session) -> List[Contrato]:
        return db.query(Contrato).all()


contrato = CRUDContrato(Contrato)
