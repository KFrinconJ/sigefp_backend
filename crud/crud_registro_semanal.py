from typing import Any, Dict, Optional, Union, List
from datetime import date as Date
from datetime import datetime as DateTime

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.registro_semanal import RegistroSemanal
from schemas.registro_semanal import RegistroSemanalCreate, RegistroSemanalUpdate


class CRUDRegistroSemanal(CRUDBase[RegistroSemanal, RegistroSemanalCreate, RegistroSemanalUpdate]):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[RegistroSemanal]:
        return db.query(RegistroSemanal).filter(RegistroSemanal.nombre == nombre).first()

    def get_by_fechaInicio(self, db: Session, *, fechaInicio: Date) -> Optional[RegistroSemanal]:
        return db.query(RegistroSemanal).filter(RegistroSemanal.fechaInicio == fechaInicio).first()

    def get_by_fechaFinal(self, db: Session, *, fechaFinal: Date) -> Optional[RegistroSemanal]:
        return db.query(RegistroSemanal).filter(RegistroSemanal.fechaFinal == fechaFinal).first()

    def get_by_descripcion(self, db: Session, *, descripcion: str) -> Optional[RegistroSemanal]:
        return db.query(RegistroSemanal).filter(RegistroSemanal.descripcion == descripcion).first()

    def get_by_horaEnvio(self, db: Session, *, horaEnvio: DateTime) -> Optional[RegistroSemanal]:
        return db.query(RegistroSemanal).filter(RegistroSemanal.horaEnvio == horaEnvio).first()

    def get_by_estado_id(self, db: Session, *, estado_id: int) -> Optional[RegistroSemanal]:
        return db.query(RegistroSemanal).filter(RegistroSemanal.estado_id == estado_id).first()

    def get_by_registro_id(self, db: Session, *, registro_id: int) -> Optional[RegistroSemanal]:
        return db.query(RegistroSemanal).filter(RegistroSemanal.registro_id == registro_id).first()

    def create(self, db: Session, *, obj_in: RegistroSemanalCreate) -> RegistroSemanal:
        db_obj = RegistroSemanal(
            nombre=obj_in.nombre,
            fechaInicio=obj_in.fechaInicio,
            fechaFinal=obj_in.fechaFinal,
            descripcion=obj_in.descripcion,
            estado_id=obj_in.estado_id,
            registro_id=obj_in.registro_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: RegistroSemanal, obj_in: Union[RegistroSemanalUpdate, Dict[str, Any]]
    ) -> RegistroSemanal:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def remove(self, db: Session, *, id: int) -> RegistroSemanal:
        obj = db.query(RegistroSemanal).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_all(self, db: Session) -> List[RegistroSemanal]:
        return db.query(RegistroSemanal).all()


registro_semanal = CRUDRegistroSemanal(RegistroSemanal)
