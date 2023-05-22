from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from core.security import get_password_hash, verify_password
from crud.base import CRUDBase
from models.user import User
from schemas.user import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_by_rol_id(self, db: Session, *, rol_id: int) -> Optional[User]:
        return db.query(User).filter(User.rol_id == rol_id).all()

    def get_by_contratos_id(self, db: Session, *, contratos_id: int) -> Optional[User]:
        return db.query(User).filter(User.contratos_id.contains(contratos_id)).all()

    def get_by_vinculaciones_id(
        self, db: Session, *, vinculaciones_id: int
    ) -> Optional[User]:
        return (
            db.query(User)
            .filter(User.vinculaciones_id.contains(vinculaciones_id))
            .all()
        )

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_admin(self, user: User) -> bool:
        return user.rol_id == 1
    
    #Es responsable de la funcion sustantiva
    def is_rfs(self, user: User) -> bool:
        return user.rol_id == 2
    
    def is_docente(self, user: User) -> bool:
        return user.rol_id == 3
    
    def is_predeterminado(self, user: User) -> bool:
        return user.rol_id == 4

    def create(self, db: Session, *, obj_in: UserCreate) -> User:
        db_obj = User(
            nombre=obj_in.nombre,
            apellido=obj_in.apellido,
            cargo=obj_in.cargo,
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            rol_id=obj_in.rol_id,
            contratos_id=obj_in.contratos_id,
            vinculaciones_id=obj_in.vinculaciones_id,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]
    ) -> User:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        if update_data["password"]:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def remove(self, db: Session, *, id: int) -> User:
        obj = db.query(User).get(id)
        db.delete(obj)
        db.commit()
        return obj

    def get_multi(self, db: Session) -> List[User]:
        return db.query(User).all()
    

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user



user = CRUDUser(User)
