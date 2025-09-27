import pytest
from src.config import *
from src.service.common_service import *

from src.model.treinador import Treinador
from src.model.treino import Treino
from src.model.time import Time

def test_treino_creation():
    with app.app_context():
        with db_session:
            treinador = create_object(Treinador,
                nome="Ana",
                dt_nasc="1975-07-20",
                email="ana@gmail.com",
                cpf="12312312300",
                cref="CREF456"
            )
            time = create_object(Time,
                esporte="Basquete"
            )
            treino = create_object(Treino,
                data="2025-09-27",
                horario="10:00",
                time=time,
                local="Quadra A",
                treinador=treinador
            )
            assert treino.id is not None
            assert isinstance(treino.id, int)
            assert treino.local == "Quadra A"
            assert treino.time.id == time.id
            assert treino.treinador.id == treinador.id

def test_treino_delete():
    with app.app_context():
        with db_session:
            treino = get_object_by_attribute(Treino, "local", "Quadra A")
            assert treino is not None
            ok = delete_object(treino)
            assert ok == "ok"
