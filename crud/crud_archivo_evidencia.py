from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.archivo_evidencia import ArchivoEvidencia
from schemas.archivo_evidencia import ArchivoEvidenciaCreate, ArchivoEvidenciaUpdate


class CRUDArchivoEvidencia(
    CRUDBase[ArchivoEvidencia, ArchivoEvidenciaCreate, ArchivoEvidenciaUpdate]
):
    def get_by_nombre(self, db: Session, *, nombre: str) -> Optional[ArchivoEvidencia]:
        return (
            db.query(ArchivoEvidencia).filter(ArchivoEvidencia.nombre == nombre).first()
        )

    def get_by_ubicacion(
        self, db: Session, *, ubicacion: str
    ) -> Optional[ArchivoEvidencia]:
        return (
            db.query(ArchivoEvidencia)
            .filter(ArchivoEvidencia.ubicacion == ubicacion)
            .first()
        )

    def get_by_registro_semanal_id(
        self, db: Session, *, registro_semanal_id: int
    ) -> Optional[ArchivoEvidencia]:
        return (
            db.query(ArchivoEvidencia)
            .filter(ArchivoEvidencia.registro_semanal_id == registro_semanal_id)
            .first()
        )

    def create(
        self, db: Session, *, obj_in: ArchivoEvidenciaCreate
    ) -> ArchivoEvidencia:
        db_obj = ArchivoEvidencia(
            nombre=obj_in.nombre,
            ubicacion=obj_in.ubicacion,
            registro_semanal_id=obj_in.registro_semanal_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ArchivoEvidencia,
        obj_in: Union[ArchivoEvidenciaUpdate, Dict[str, Any]]
    ) -> ArchivoEvidencia:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def remove(self, db: Session, *, id: int) -> ArchivoEvidencia:
        obj = db.query(ArchivoEvidencia).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_by_id_registro_semanal(
        self, db: Session, id_registro_semanal: int
    ) -> List[ArchivoEvidencia]:
        return (
            db.query(ArchivoEvidencia)
            .filter(ArchivoEvidencia.registro_semanal_id == id_registro_semanal)
            .all()
        )

    def get_all(self, db: Session) -> List[ArchivoEvidencia]:
        return db.query(ArchivoEvidencia).all()


archivo_evidencia = CRUDArchivoEvidencia(ArchivoEvidencia)
