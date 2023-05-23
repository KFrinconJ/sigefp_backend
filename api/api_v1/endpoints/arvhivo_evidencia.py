from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.ArchivoEvidenciaInDB])
def read_archivos_evidencia(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve archivos de evidencia.
    """
    archivos_evidencia = crud.archivo_evidencia.get_all(db)
    return archivos_evidencia


@router.post("/", response_model=schemas.ArchivoEvidenciaInDB)
def create_archivo_evidencia(
    *,
    db: Session = Depends(deps.get_db),
    archivo_evidencia_in: schemas.ArchivoEvidenciaCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new archivo de evidencia.
    """
    archivo_evidencia = crud.archivo_evidencia.create(db, obj_in=archivo_evidencia_in)
    return archivo_evidencia


@router.put("/{id}", response_model=schemas.ArchivoEvidenciaInDB)
def update_archivo_evidencia(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    archivo_evidencia_in: schemas.ArchivoEvidenciaUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an archivo de evidencia.
    """
    archivo_evidencia = crud.archivo_evidencia.get(db, id=id)
    if not archivo_evidencia:
        raise HTTPException(
            status_code=404,
            detail="The archivo de evidencia with this id does not exist in the system",
        )
    archivo_evidencia = crud.archivo_evidencia.update(
        db, db_obj=archivo_evidencia, obj_in=archivo_evidencia_in
    )
    return archivo_evidencia


@router.delete("/{id}", response_model=schemas.ArchivoEvidenciaInDB)
def delete_archivo_evidencia(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an archivo de evidencia.
    """
    archivo_evidencia = crud.archivo_evidencia.get(db, id=id)
    if not archivo_evidencia:
        raise HTTPException(
            status_code=404,
            detail="The archivo de evidencia with this id does not exist in the system",
        )
    archivo_evidencia = crud.archivo_evidencia.remove(db, id=id)
    return archivo_evidencia


@router.get("/{id}", response_model=schemas.ArchivoEvidenciaInDB)
def get_archivo_evidencia(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get an archivo de evidencia by ID.
    """
    archivo_evidencia = crud.archivo_evidencia.get(db, id=id)
    if not archivo_evidencia:
        raise HTTPException(
            status_code=404,
            detail="The archivo de evidencia with this id does not exist in the system",
        )
    return archivo_evidencia


@router.get(
    "/registro-semanal/{registro_semanal_id}",
    response_model=schemas.ArchivoEvidenciaInDB,
)
def get_archivo_evidencia_by_registro_semanal_id(
    registro_semanal_id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get an archivo de evidencia by registro_semanal_id.
    """
    archivo_evidencia = crud.archivo_evidencia.get_by_registro_semanal_id(
        db, registro_semanal_id=registro_semanal_id
    )
    if not archivo_evidencia:
        raise HTTPException(
            status_code=404,
            detail="No archivo de evidencia found for this registro_semanal_id",
        )
    return archivo_evidencia


@router.get(
    "/registro-semanal/{id_registro_semanal}/archivos",
    response_model=List[schemas.ArchivoEvidenciaInDB],
)
def get_archivos_evidencia_by_id_registro_semanal(
    id_registro_semanal: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get archivos de evidencia by id_registro_semanal.
    """
    archivos_evidencia = crud.archivo_evidencia.get_by_id_registro_semanal(
        db, id_registro_semanal=id_registro_semanal
    )
    if not archivos_evidencia:
        raise HTTPException(
            status_code=404,
            detail="No archivos de evidencia found for this id_registro_semanal",
        )
    return archivos_evidencia
