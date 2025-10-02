import pytest

from src.config import *

from src.service.common_service import *
from src.model import Atleta
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
                email="joao@gmail.com",
                cpf="12345678901"
            )
            assert atleta.id is not None
            assert isinstance(atleta.id, int)
            assert atleta.nome == "Joao Silva"
            assert atleta.email == "joao@gmail.com"

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

