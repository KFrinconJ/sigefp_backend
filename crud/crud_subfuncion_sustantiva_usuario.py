from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from models.subfuncion_sustantiva_usuario import SubfuncionSustantivaUsuario
from schemas.subfuncion_sustantiva_usuario import SubfuncionSustantivaUsuarioCreate, SubfuncionSustantivaUsuarioUpdate


class CRUDSubfuncionSustantivaUsuario(CRUDBase[SubfuncionSustantivaUsuario, SubfuncionSustantivaUsuarioCreate, SubfuncionSustantivaUsuarioUpdate]):
    def get_by_user_id(self, db: Session, *, user_id: int) -> Optional[SubfuncionSustantivaUsuario]:
        return db.query(SubfuncionSustantivaUsuario).filter(SubfuncionSustantivaUsuario.user_id == user_id).first()

    def get_by_subfuncion_sustantiva_id(self, db: Session, *, subfuncion_sustantiva_id: int) -> Optional[SubfuncionSustantivaUsuario]:
        return db.query(SubfuncionSustantivaUsuario).filter(SubfuncionSustantivaUsuario.subfuncion_sustantiva_id == subfuncion_sustantiva_id).first()

    def get_by_registro_id(self, db: Session, *, registro_id: int) -> Optional[SubfuncionSustantivaUsuario]:
        return db.query(SubfuncionSustantivaUsuario).filter(SubfuncionSustantivaUsuario.registro_id == registro_id).first()

    def create(self, db: Session, *, obj_in: SubfuncionSustantivaUsuarioCreate) -> SubfuncionSustantivaUsuario:
        db_obj = SubfuncionSustantivaUsuario(
            user_id=obj_in.user_id,
            subfuncion_sustantiva_id=obj_in.subfuncion_sustantiva_id,
            registro_id=obj_in.registro_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: SubfuncionSustantivaUsuario, obj_in: Union[SubfuncionSustantivaUsuarioUpdate, Dict[str, Any]]
    ) -> SubfuncionSustantivaUsuario:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def remove(self, db: Session, *, id: int) -> SubfuncionSustantivaUsuario:
        obj = db.query(SubfuncionSustantivaUsuario).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_all(self, db: Session) -> List[SubfuncionSustantivaUsuario]:
        return db.query(SubfuncionSustantivaUsuario).all()


subfuncion_sustantiva_usuario = CRUDSubfuncionSustantivaUsuario(SubfuncionSustantivaUsuario)
