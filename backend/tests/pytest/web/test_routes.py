import pytest
from src.config import app, db
from src.route.routes import *

# --- Gera mapeamento Pony ORM uma única vez ---
db.generate_mapping(create_tables=True)

# --- Fixture para o client Flask ---
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# --- Fixtures para criar dependências ---

@pytest.fixture
def atleta(client):
    res = client.post('/atletas', json={
        "nome": "Joao",
        "dt_nasc": "2000-05-01",
        "email": "joao@gmail.com",
        "cpf": "12345678901"
    })
    atleta_id = list(res.get_json()["details"]["Atleta"].keys())[0]
    yield atleta_id
    client.delete(f"/atletas/{atleta_id}")

@pytest.fixture
def treinador(client):
    res = client.post('/treinadores', json={
        "nome": "Carlos",
        "dt_nasc": "1980-01-01",
        "email": "carlos@gmail.com",
        "cpf": "98765432100",
        "cref": "CREF123"
    })
    treinador_id = list(res.get_json()["details"]["Treinador"].keys())[0]
    yield treinador_id
    client.delete(f"/treinadores/{treinador_id}")

@pytest.fixture
def time(client):
    res = client.post('/times', json={"esporte": "Futebol"})
    time_id = list(res.get_json()["details"]["Time"].keys())[0]
    yield time_id
    client.delete(f"/times/{time_id}")

@pytest.fixture
def treino(client, time, treinador):
    res = client.post('/treinos', json={
        "data": "2025-09-27",
        "horario": "10:00",
        "time": int(time),
        "local": "Quadra Central",
        "treinador": int(treinador)
    })
    treino_id = list(res.get_json()["details"]["Treino"].keys())[0]
    yield treino_id
    client.delete(f"/treinos/{treino_id}")

@pytest.fixture
def foto(client, atleta):
    res = client.post('/fotos', json={
        "url": "http://image.com/foto1.png",
        "atleta": int(atleta)
    })
    foto_id = list(res.get_json()["details"]["Foto"].keys())[0]
    yield foto_id
    client.delete(f"/fotos/{foto_id}")

# --- Testes CRUD ---

def test_crud_atleta(client):
    # POST
    res = client.post('/atletas', json={
        "nome": "Ana",
        "dt_nasc": "1995-03-10",
        "email": "ana@gmail.com",
        "cpf": "11122233344"
    })
    assert res.status_code == 201
    atleta_id = list(res.get_json()["details"]["Atleta"].keys())[0]

    # GET
    res = client.get('/atletas')
    assert res.status_code == 200
    assert any(atleta_id in item for item in str(res.get_json()["details"]))

    # DELETE
    res = client.delete(f"/atletas/{atleta_id}")
    assert res.status_code == 204

def test_crud_treinador(client):
    # POST
    res = client.post('/treinadores', json={
        "nome": "Miguel",
        "dt_nasc": "1975-07-20",
        "email": "miguel@gmail.com",
        "cpf": "55566677788",
        "cref": "CREF999"
    })
    assert res.status_code == 201
    treinador_id = list(res.get_json()["details"]["Treinador"].keys())[0]

    # GET
    res = client.get('/treinadores')
    assert res.status_code == 200
    assert any(treinador_id in item for item in str(res.get_json()["details"]))

    # DELETE
    res = client.delete(f"/treinadores/{treinador_id}")
    assert res.status_code == 204

def test_crud_time(client):
    # POST
    res = client.post('/times', json={"esporte": "Vôlei"})
    assert res.status_code == 201
    time_id = list(res.get_json()["details"]["Time"].keys())[0]

    # GET
    res = client.get('/times')
    assert res.status_code == 200
    assert any(time_id in item for item in str(res.get_json()["details"]))

    # DELETE
    res = client.delete(f"/times/{time_id}")
    assert res.status_code == 204

def test_crud_treino(client, time, treinador):
    # POST
    res = client.post('/treinos', json={
        "data": "2025-09-28",
        "horario": "15:00",
        "time": int(time),
        "local": "Quadra Leste",
        "treinador": int(treinador)
    })
    assert res.status_code == 201
    treino_id = list(res.get_json()["details"]["Treino"].keys())[0]

    # GET
    res = client.get('/treinos')
    assert res.status_code == 200
    assert any(treino_id in item for item in str(res.get_json()["details"]))

    # DELETE
    res = client.delete(f"/treinos/{treino_id}")
    assert res.status_code == 204

def test_crud_foto(client, atleta):
    # POST
    res = client.post('/fotos', json={
        "url": "http://image.com/foto2.png",
        "atleta": int(atleta)
    })
    assert res.status_code == 201
    foto_id = list(res.get_json()["details"]["Foto"].keys())[0]

    # GET
    res = client.get('/fotos')
    assert res.status_code == 200
    assert any(foto_id in item for item in str(res.get_json()["details"]))

    # DELETE
    res = client.delete(f"/fotos/{foto_id}")
    assert res.status_code == 204
