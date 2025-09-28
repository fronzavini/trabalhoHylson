import pytest
import uuid

from src.config import *
from src.service.common_service import *
from src.model.atleta import Atleta
from src.app import app


# db.generate_mapping(create_tables=False)
# -------------------------
# Teste de criação de Atleta
# -------------------------
def test_atleta_creation():
    with app.app_context():
        with db_session:
            atleta = create_object(Atleta,
                nome="Joao Silva",
                dt_nasc="2000-05-01",
                email=f"joao{uuid.uuid4()}@gmail.com",
                cpf=str(uuid.uuid4().int)[:11]
            )
            assert atleta.id is not None
            assert isinstance(atleta.id, int)
            assert atleta.nome == "Joao Silva"
# -------------------------
# Teste de exclusão de Atleta
# -------------------------
def test_atleta_delete():
    with app.app_context():
        with db_session:
            atleta = get_object_by_attribute(Atleta, "email", "joao@gmail.com")
            assert atleta is not None
            ok = delete_object(atleta)
            assert ok == "ok"

