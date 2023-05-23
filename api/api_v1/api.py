from fastapi import APIRouter

from api.api_v1.endpoints import login, users, contratos, adscripcion, arvhivo_evidencia

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(contratos.router, prefix="/contratos", tags=["contratos"])
api_router.include_router(adscripcion.router, prefix="/adscripcion", tags=["adscripcion"])
api_router.include_router(arvhivo_evidencia.router, prefix="/arvhivo_evidencia", tags=["arvhivo_evidencia"])
