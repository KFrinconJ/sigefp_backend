from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import crud
from schemas.subfuncion_sustantiva_usuario import SubfuncionSustantivaUsuarioCreate, SubfuncionSustantivaUsuarioUpdate

def test_create_subfuncion_sustantiva_usuario(db: Session) -> None:
    user_id = 3
    subfuncion_sustantiva_id = 3
    registro_id = 3
    subfuncion_sustantiva_usuario_in = SubfuncionSustantivaUsuarioCreate(user_id=user_id, subfuncion_sustantiva_id=subfuncion_sustantiva_id, registro_id=registro_id)
    subfuncion_sustantiva_usuario = crud.subfuncion_sustantiva_usuario.create(db, obj_in=subfuncion_sustantiva_usuario_in)
    assert subfuncion_sustantiva_usuario.user_id == user_id
    assert subfuncion_sustantiva_usuario.subfuncion_sustantiva_id == subfuncion_sustantiva_id
    assert subfuncion_sustantiva_usuario.registro_id == registro_id

def test_get_subfuncion_sustantiva_usuario(db: Session) -> None:
    user_id = 3
    subfuncion_sustantiva_id = 3
    registro_id = 3
    subfuncion_sustantiva_usuario_in = SubfuncionSustantivaUsuarioCreate(user_id=user_id, subfuncion_sustantiva_id=subfuncion_sustantiva_id, registro_id=registro_id)
    subfuncion_sustantiva_usuario = crud.subfuncion_sustantiva_usuario.create(db, obj_in=subfuncion_sustantiva_usuario_in)
    subfuncion_sustantiva_usuario_2 = crud.subfuncion_sustantiva_usuario.get(db, id=subfuncion_sustantiva_usuario.id)
    assert subfuncion_sustantiva_usuario_2
    assert jsonable_encoder(subfuncion_sustantiva_usuario) == jsonable_encoder(subfuncion_sustantiva_usuario_2)

def test_update_subfuncion_sustantiva_usuario(db: Session) -> None:
    user_id = 3
    subfuncion_sustantiva_id = 3
    registro_id = 3
    subfuncion_sustantiva_usuario_in = SubfuncionSustantivaUsuarioCreate(user_id=user_id, subfuncion_sustantiva_id=subfuncion_sustantiva_id, registro_id=registro_id)
    subfuncion_sustantiva_usuario = crud.subfuncion_sustantiva_usuario.create(db, obj_in=subfuncion_sustantiva_usuario_in)
    new_user_id = 3
    new_subfuncion_sustantiva_id = 3
    new_registro_id = 3
    subfuncion_sustantiva_usuario_in_update = SubfuncionSustantivaUsuarioUpdate(user_id=new_user_id, subfuncion_sustantiva_id=new_subfuncion_sustantiva_id, registro_id=new_registro_id)
    crud.subfuncion_sustantiva_usuario.update(db, db_obj=subfuncion_sustantiva_usuario, obj_in=subfuncion_sustantiva_usuario_in_update)
    subfuncion_sustantiva_usuario_2 = crud.subfuncion_sustantiva_usuario.get(db, id=subfuncion_sustantiva_usuario.id)
    assert subfuncion_sustantiva_usuario_2.user_id == new_user_id
    assert subfuncion_sustantiva_usuario_2.subfuncion_sustantiva_id == new_subfuncion_sustantiva_id
    assert subfuncion_sustantiva_usuario_2.registro_id == new_registro_id

def test_delete_subfuncion_sustantiva_usuario(db: Session) -> None:
    user_id = 3
    subfuncion_sustantiva_id = 3
    registro_id = 3
    subfuncion_sustantiva_usuario_in = SubfuncionSustantivaUsuarioCreate(user_id=user_id, subfuncion_sustantiva_id=subfuncion_sustantiva_id, registro_id=registro_id)
    subfuncion_sustantiva_usuario = crud.subfuncion_sustantiva_usuario.create(db, obj_in=subfuncion_sustantiva_usuario_in)
    subfuncion_sustantiva_usuario_2 = crud.subfuncion_sustantiva_usuario.remove(db, id=subfuncion_sustantiva_usuario.id)
    subfuncion_sustantiva_usuario_3 = crud.subfuncion_sustantiva_usuario.get(db, id=subfuncion_sustantiva_usuario.id)
    assert subfuncion_sustantiva_usuario_3 is None
    assert subfuncion_sustantiva_usuario_2.id == subfuncion_sustantiva_usuario.id
    assert subfuncion_sustantiva_usuario_2.user_id == user_id
