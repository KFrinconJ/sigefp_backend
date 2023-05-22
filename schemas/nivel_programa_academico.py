from pydantic import BaseModel


class NivelProgramaAcademicoBase(BaseModel):
    nombre: str
    nivel_id: int


class NivelProgramaAcademicoUpdate(NivelProgramaAcademicoBase):
    pass


class NivelProgramaAcademico(NivelProgramaAcademicoBase):
    id: int

    class Config:
        orm_mode = True
