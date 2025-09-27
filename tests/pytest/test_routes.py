import pytest
import json
from src.config import app, db
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
def test_create_atleta(client):
    data = {
        "nome": "Joao",
        "dt_nasc": "2000-05-01",
        "email": "joao@gmail.com",
        "cpf": "12345678901"
    }
    response = client.post("/atletas", data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    resp_json = response.get_json()
    assert resp_json["result"] == "ok"
    assert resp_json["details"]["Atleta"][1]["nome"] == "Joao"

def test_list_atletas(client):
    # Criar um atleta antes
    data = {
        "nome": "Maria",
        "dt_nasc": "1999-03-15",
        "email": "maria@gmail.com",
        "cpf": "98765432100"
    }
    client.post("/atletas", data=json.dumps(data), content_type='application/json')

    response = client.get("/atletas")
    assert response.status_code == 200
    resp_json = response.get_json()
    assert resp_json["result"] == "ok"
    assert len(resp_json["details"]) == 1

def test_delete_atleta(client):
    data = {
        "nome": "Pedro",
        "dt_nasc": "1998-08-08",
        "email": "pedro@gmail.com",
        "cpf": "11122233344"
    }
    client.post("/atletas", data=json.dumps(data), content_type='application/json')

    response = client.delete("/atletas/1")
    assert response.status_code == 204

# -------------------------
# Testes Treinador
# -------------------------
def test_create_treinador(client):
    data = {
        "nome": "Carlos",
        "dt_nasc": "1980-01-01",
        "email": "carlos@gmail.com",
        "cpf": "98765432100",
        "cref": "CREF123"
    }
    response = client.post("/treinadores", data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201
    resp_json = response.get_json()
    assert resp_json["result"] == "ok"

def test_list_treinadores(client):
    data = {
        "nome": "Ana",
        "dt_nasc": "1975-07-20",
        "email": "ana@gmail.com",
        "cpf": "12312312300",
        "cref": "CREF456"
    }
    client.post("/treinadores", data=json.dumps(data), content_type='application/json')

    response = client.get("/treinadores")
    assert response.status_code == 200
    resp_json = response.get_json()
    assert resp_json["result"] == "ok"
    assert len(resp_json["details"]) == 1

def test_delete_treinador(client):
    data = {
        "nome": "Luiz",
        "dt_nasc": "1970-02-10",
        "email": "luiz@gmail.com",
        "cpf": "32132132100",
        "cref": "CREF789"
    }
    client.post("/treinadores", data=json.dumps(data), content_type='application/json')

    response = client.delete("/treinadores/1")
    assert response.status_code == 204

# -------------------------
# Testes Time
# -------------------------
def test_create_time(client):
    data = {"esporte": "Futebol"}
    response = client.post("/times", data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201

def test_list_times(client):
    data = {"esporte": "Basquete"}
    client.post("/times", data=json.dumps(data), content_type='application/json')

    response = client.get("/times")
    assert response.status_code == 200
    resp_json = response.get_json()
    assert resp_json["result"] == "ok"

def test_delete_time(client):
    data = {"esporte": "Vôlei"}
    client.post("/times", data=json.dumps(data), content_type='application/json')

    response = client.delete("/times/1")
    assert response.status_code == 204

# -------------------------
# Testes Treino
# -------------------------
def test_create_treino(client):
    # Primeiro criar treinador e time
    client.post("/treinadores", data=json.dumps({
        "nome": "Carlos",
        "dt_nasc": "1980-01-01",
        "email": "carlos@gmail.com",
        "cpf": "98765432100",
        "cref": "CREF123"
    }), content_type='application/json')

    client.post("/times", data=json.dumps({"esporte": "Futebol"}), content_type='application/json')

    data = {
        "data": "2025-09-27",
        "horario": "10:00",
        "time": 1,
        "local": "Quadra Central",
        "treinador": 1
    }
    response = client.post("/treinos", data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201

def test_list_treinos(client):
    # Criar treinador e time
    client.post("/treinadores", data=json.dumps({
        "nome": "Ana",
        "dt_nasc": "1975-07-20",
        "email": "ana@gmail.com",
        "cpf": "12312312300",
        "cref": "CREF456"
    }), content_type='application/json')
    client.post("/times", data=json.dumps({"esporte": "Basquete"}), content_type='application/json')

    data = {
        "data": "2025-09-27",
        "horario": "15:00",
        "time": 1,
        "local": "Quadra B",
        "treinador": 1
    }
    client.post("/treinos", data=json.dumps(data), content_type='application/json')

    response = client.get("/treinos")
    assert response.status_code == 200
    resp_json = response.get_json()
    assert resp_json["result"] == "ok"

def test_delete_treino(client):
    client.post("/treinadores", data=json.dumps({
        "nome": "Luiz",
        "dt_nasc": "1970-02-10",
        "email": "luiz@gmail.com",
        "cpf": "32132132100",
        "cref": "CREF789"
    }), content_type='application/json')
    client.post("/times", data=json.dumps({"esporte": "Vôlei"}), content_type='application/json')

    client.post("/treinos", data=json.dumps({
        "data": "2025-09-27",
        "horario": "08:00",
        "time": 1,
        "local": "Quadra C",
        "treinador": 1
    }), content_type='application/json')

    response = client.delete("/treinos/1")
    assert response.status_code == 204

# -------------------------
# Testes Foto
# -------------------------
def test_create_foto(client):
    # Criar atleta
    client.post("/atletas", data=json.dumps({
        "nome": "Joao",
        "dt_nasc": "2000-05-01",
        "email": "joao@gmail.com",
        "cpf": "12345678901"
    }), content_type='application/json')

    data = {
        "url": "http://image.com/foto1.png",
        "atleta": 1
    }
    response = client.post("/fotos", data=json.dumps(data), content_type='application/json')
    assert response.status_code == 201

def test_list_fotos(client):
    client.post("/atletas", data=json.dumps({
        "nome": "Maria",
        "dt_nasc": "1999-03-15",
        "email": "maria@gmail.com",
        "cpf": "98765432100"
    }), content_type='application/json')

    client.post("/fotos", data=json.dumps({
        "url": "http://image.com/foto2.png",
        "atleta": 1
    }), content_type='application/json')

    response = client.get("/fotos")
    assert response.status_code == 200
    resp_json = response.get_json()
    assert resp_json["result"] == "ok"

def test_delete_foto(client):
    client.post("/atletas", data=json.dumps({
        "nome": "Pedro",
        "dt_nasc": "1998-08-08",
        "email": "pedro@gmail.com",
        "cpf": "11122233344"
    }), content_type='application/json')

    client.post("/fotos", data=json.dumps({
        "url": "http://image.com/foto3.png",
        "atleta": 1
    }), content_type='application/json')

    response = client.delete("/fotos/1")
    assert response.status_code == 204
