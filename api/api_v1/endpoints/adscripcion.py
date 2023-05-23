from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.AdscripcionInDB])
def read_adscripciones(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.current_active_admin_or_rfs_or_docente),
) -> Any:
    """
    Retrieve adscripciones.
    """
    adscripciones = crud.adscripcion.get_all(db)
    return adscripciones


@router.get("/{adscripcion_id}", response_model=schemas.AdscripcionInDB)
def read_adscripcion_by_id(
    adscripcion_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.current_active_admin_or_rfs_or_docente),
) -> Any:
    """
    Retrieve adscripcion by ID.
    """
    adscripcion = crud.adscripcion.get(db, id=adscripcion_id)
    if not adscripcion:
        raise HTTPException(
            status_code=404,
            detail="The adscripcion with this id does not exist in the system",
        )
    return adscripcion


@router.post("/", response_model=schemas.AdscripcionInDB)
def create_adscripcion(
    *,
    db: Session = Depends(deps.get_db),
    adscripcion_in: schemas.AdscripcionCreate,
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Create new adscripcion.
    """
    adscripcion = crud.adscripcion.create(db, obj_in=adscripcion_in)
    return adscripcion


@router.put("/{adscripcion_id}", response_model=schemas.AdscripcionInDB)
def update_adscripcion(
    *,
    db: Session = Depends(deps.get_db),
    adscripcion_id: int,
    adscripcion_in: schemas.AdscripcionUpdate,
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Update an adscripcion.
    """
    adscripcion = crud.adscripcion.get(db, id=adscripcion_id)
    if not adscripcion:
        raise HTTPException(
            status_code=404,
            detail="The adscripcion with this id does not exist in the system",
        )
    adscripcion = crud.adscripcion.update(db, db_obj=adscripcion, obj_in=adscripcion_in)
    return adscripcion


@router.delete("/{adscripcion_id}", response_model=schemas.AdscripcionInDB)
def delete_adscripcion(
    *,
    db: Session = Depends(deps.get_db),
    adscripcion_id: int,
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Delete an adscripcion.
    """
    adscripcion = crud.adscripcion.get(db, id=adscripcion_id)
    if not adscripcion:
        raise HTTPException(
            status_code=404,
            detail="The adscripcion with this id does not exist in the system",
        )
    adscripcion = crud.adscripcion.remove(db, id=adscripcion_id)
    return adscripcion


# @router.get("/by_id_usuario/{user_id}", response_model=List[schemas.AdscripcionInDB])
# def read_adscripciones_by_user_id(
#     user_id: int,
#     db: Session = Depends(deps.get_db),
#     current_user: models.User = Depends(deps.current_user_active_admin),
# ) -> Any:
#     """
#     Retrieve adscripciones by user ID.
#     """
#     adscripciones = crud.adscripcion.get_by_id_usuario(db, user_id)
#     if not adscripciones:
#         raise HTTPException(
#             status_code=404,
#             detail="No adscripciones found for this user ID",
#         )
