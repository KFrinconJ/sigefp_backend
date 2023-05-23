from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

import crud, models, schemas
from api import deps
from core.config import settings


router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_users(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Retrieve users.
    """
    users = crud.user.get_multi(db)
    return users


@router.post("/", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    return user


@router.put("/me", response_model=schemas.User)
def update_user_me(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(None),
    full_name: str = Body(None),
    email: EmailStr = Body(None),
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if full_name is not None:
        user_in.full_name = full_name
    if email is not None:
        user_in.email = email
    user = crud.user.update(db, db_obj=current_user, obj_in=user_in)
    return user


@router.get("/by_contratos_id/{contratos_id}", response_model=schemas.User)
def get_users_by_contratos_id(
    contratos_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Get users by contratos_id.
    """
    user = crud.user.get_by_contratos_id(db, contratos_id=contratos_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="No user with this contratos_id exists in the system",
        )
    return user


@router.get("/me", response_model=schemas.User)
def read_user_me(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.current_active_admin_or_rfs_or_docente),
) -> Any:
    """
    Get current user (accessible to admin docente and rfs).
    """
    return current_user


@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    user = crud.user.get(db, id=user_id)
    if user == current_user:
        return user
    if not crud.user.is_admin(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return user


# Nuevo


@router.get("/by_role/{role}", response_model=List[schemas.User])
def get_users_by_role(
    rol: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Get users by role.
    """
    users = crud.user.get_multi_by_role(db, rol_id=rol)
    if not users or len(users) == 0:
        raise HTTPException(
            status_code=404,
            detail="The users with this role does not exist in the system",
        )
    return users


@router.get("/by_vinculacion/{vinculacion}", response_model=List[schemas.User])
def get_users_by_vinculacion(
    vinculacion: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Get users by vinculacion.
    """
    users = crud.user.get_multi_by_vinculacion(db, vinculacion_id=vinculacion)
    if not users or len(users) == 0:
        raise HTTPException(
            status_code=404,
            detail="The users with this vinculation does not exist in the system",
        )
    return users


@router.put("/{user_id}", response_model=schemas.User)
def update_user(
    *,
    db: Session = Depends(deps.get_db),
    user_id: int,
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Update a user.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    user = crud.user.update(db, db_obj=user, obj_in=user_in)
    return user
