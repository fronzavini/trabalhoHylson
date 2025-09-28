import pytest
from src.config import *
from src.service.common_service import *
from src.model.treinador import Treinador



def test_treinador_creation():
    with app.app_context():
        with db_session:
            treinador = create_object(Treinador,
                nome="Carlos Mendes",
                dt_nasc="1980-01-01",
                email="carlos@gmail.com",
                cpf="98765432100",
                cref="CREF123"
            )
            assert treinador.id is not None
            assert isinstance(treinador.id, int)
            assert treinador.nome == "Carlos Mendes"
            assert treinador.cref == "CREF123"

def test_treinador_delete():
    with app.app_context():
        with db_session:
            treinador = get_object_by_attribute(Treinador, "cref", "CREF123")
            assert treinador is not None
            ok = delete_object(treinador)
            assert ok == "ok"
