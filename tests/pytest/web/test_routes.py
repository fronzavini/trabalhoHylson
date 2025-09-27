import pytest
import json
from config import app, db
from model import *

# -------------------------
# Fixture para o client Flask
# -------------------------
@pytest.fixture
def client():
    # Configura banco em memória para testes
    db.drop_all_tables(with_all_data=True)
    db.create_tables()
    with app.test_client() as client:
        yield client

# -------------------------
# Testes Atleta
# -------------------------
def test_atleta_crud(client):
    # POST
    res = client.post('/atletas', json={
        "nome": "Joao",
        "dt_nasc": "2000-05-01",
        "email": "joao@gmail.com",
        "cpf": "12345678901"
    })
    assert res.status_code == 201
    a = res.get_json()["details"]["Atleta"]
    atleta_id = list(a.keys())[0]
    print(f"Created Atleta with ID: {atleta_id}")

    # GET LIST
    res = client.get('/atletas')
    assert res.status_code == 200
    json_data = res.get_json()
    assert json_data["result"] == "ok"
    print(f"Atletas found: {len(json_data['details'])}")

    # DELETE
    res = client.delete(f"/atletas/{atleta_id}")
    assert res.status_code == 204
    print(f"Atleta with ID {atleta_id} deleted successfully.")

# -------------------------
# Testes Treinador
# -------------------------
def test_treinador_crud(client):
    # POST
    res = client.post('/treinadores', json={
        "nome": "Carlos",
        "dt_nasc": "1980-01-01",
        "email": "carlos@gmail.com",
        "cpf": "98765432100",
        "cref": "CREF123"
    })
    assert res.status_code == 201
    t = res.get_json()["details"]["Treinador"]
    treinador_id = list(t.keys())[0]
    print(f"Created Treinador with ID: {treinador_id}")

    # GET LIST
    res = client.get('/treinadores')
    assert res.status_code == 200
    json_data = res.get_json()
    assert json_data["result"] == "ok"
    print(f"Treinadores found: {len(json_data['details'])}")

    # DELETE
    res = client.delete(f"/treinadores/{treinador_id}")
    assert res.status_code == 204
    print(f"Treinador with ID {treinador_id} deleted successfully.")

# -------------------------
# Testes Time
# -------------------------
def test_time_crud(client):
    # POST
    res = client.post('/times', json={"esporte": "Futebol"})
    assert res.status_code == 201
    tm = res.get_json()["details"]["Time"]
    time_id = list(tm.keys())[0]
    print(f"Created Time with ID: {time_id}")

    # GET LIST
    res = client.get('/times')
    assert res.status_code == 200
    json_data = res.get_json()
    assert json_data["result"] == "ok"
    print(f"Times found: {len(json_data['details'])}")

    # DELETE
    res = client.delete(f"/times/{time_id}")
    assert res.status_code == 204
    print(f"Time with ID {time_id} deleted successfully.")

# -------------------------
# Testes Treino
# -------------------------
def test_treino_crud(client):
    # Criar Treinador e Time antes
    client.post('/treinadores', json={
        "nome": "Ana",
        "dt_nasc": "1975-07-20",
        "email": "ana@gmail.com",
        "cpf": "12312312300",
        "cref": "CREF456"
    })
    client.post('/times', json={"esporte": "Basquete"})

    # POST Treino
    res = client.post('/treinos', json={
        "data": "2025-09-27",
        "horario": "10:00",
        "time": 1,
        "local": "Quadra Central",
        "treinador": 1
    })
    assert res.status_code == 201
    tr = res.get_json()["details"]["Treino"]
    treino_id = list(tr.keys())[0]
    print(f"Created Treino with ID: {treino_id}")

    # GET LIST
    res = client.get('/treinos')
    assert res.status_code == 200
    json_data = res.get_json()
    assert json_data["result"] == "ok"
    print(f"Treinos found: {len(json_data['details'])}")

    # DELETE
    res = client.delete(f"/treinos/{treino_id}")
    assert res.status_code == 204
    print(f"Treino with ID {treino_id} deleted successfully.")

# -------------------------
# Testes Foto
# -------------------------
def test_foto_crud(client):
    # Criar Atleta antes
    client.post('/atletas', json={
        "nome": "Pedro",
        "dt_nasc": "1998-08-08",
        "email": "pedro@gmail.com",
        "cpf": "11122233344"
    })

    # POST Foto
    res = client.post('/fotos', json={
        "url": "https://a.espncdn.com/combiner/i?img=/i/headshots/nba/players/full/1966.png",
        "atleta": 1
    })
    assert res.status_code == 201
    ft = res.get_json()["details"]["Foto"]
    foto_id = list(ft.keys())[0]
    print(f"Created Foto with ID: {foto_id}")

    # GET LIST
    res = client.get('/fotos')
    assert res.status_code == 200
    json_data = res.get_json()
    assert json_data["result"] == "ok"
    print(f"Fotos found: {len(json_data['details'])}")

    # DELETE
    res = client.delete(f"/fotos/{foto_id}")
    assert res.status_code == 204
    print(f"Foto with ID {foto_id} deleted successfully.")
