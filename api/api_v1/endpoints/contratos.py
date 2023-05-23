from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import date as Date

import crud, models, schemas
from api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.ContratoInDB])
def read_contratos(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Retrieve contratos.
    """
    contratos = crud.contrato.get_all(db)
    return contratos


@router.post("/", response_model=schemas.ContratoInDB)
def create_contrato(
    *,
    db: Session = Depends(deps.get_db),
    contrato_in: schemas.ContratoCreate,
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Create new contrato.
    """
    contrato = crud.contrato.create(db, obj_in=contrato_in)
    return contrato


@router.put("/{id}", response_model=schemas.ContratoInDB)
def update_contrato(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    contrato_in: schemas.ContratoUpdate,
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Update a contrato.
    """
    contrato = crud.contrato.get(db, id=id)
    if not contrato:
        raise HTTPException(
            status_code=404,
            detail="The contrato with this id does not exist in the system",
        )
    contrato = crud.contrato.update(db, db_obj=contrato, obj_in=contrato_in)
    return contrato


@router.delete("/{id}", response_model=schemas.ContratoInDB)
def delete_contrato(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Delete a contrato.
    """
    contrato = crud.contrato.get(db, id=id)
    if not contrato:
        raise HTTPException(
            status_code=404,
            detail="The contrato with this id does not exist in the system",
        )
    contrato = crud.contrato.remove(db, id=id)
    return contrato


@router.get("/{id}", response_model=schemas.ContratoInDB)
def get_contrato(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Get a contrato by ID.
    """
    contrato = crud.contrato.get(db, id=id)
    if not contrato:
        raise HTTPException(
            status_code=404,
            detail="The contrato with this id does not exist in the system",
        )
    return contrato


@router.get(
    "/by_tipo_contrato/{tipo_contrato}", response_model=List[schemas.ContratoInDB]
)
def get_contratos_by_tipo_contrato(
    tipo_contrato: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.current_user_active_admin),
) -> Any:
    """
    Get contratos by tipo_contrato.
    """
    contratos = crud.contrato.get_by_tipo_contrato(db, tipo_contrato)
    if not contratos:
        raise HTTPException(
            status_code=404,
            detail="No contracts with this tipo_contrato exist in the system",
        )
    return contratos
