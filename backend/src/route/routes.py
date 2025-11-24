from src.config import * 
from src.model import *
from src.service.common_service import *
from flask import Flask, request, jsonify

# --- Rota padrão ---
@app.route('/')
def index():
    return "API de Esportes. Use /atletas, /treinadores, /times, /treinos e /fotos"


# --- Funções auxiliares ---
def create_simple_object(mclass, data):
    try:
        myjson = {"result": "ok"}
        obj_json = create_object_return_json(mclass, **data)
        myjson.update({"details": obj_json})
        return myjson
    except Exception as ex:
        print(f"Erro ao criar {mclass.__name__}: {ex}")
        return {"result": "error", "details": str(ex)}


def get_objects_helper(mclass):
    try:
        myjson = {"result": "ok"}   
        objs = get_objects_json(mclass)
        serialized = []

        for obj in objs:
            obj_dict = dict(obj)  # converte objeto para dict simples

            # Se for Atleta, adiciona os times e a foto
            if isinstance(obj, Atleta):
                obj_dict["times"] = [{"id": t.id, "nome": t.nome, "esporte": t.esporte} for t in obj.times]
                obj_dict["ft_perfil"] = obj.ft_perfil.id if obj.ft_perfil else None

            serialized.append(obj_dict)

        myjson.update({"details": serialized})
        return myjson
    except Exception as ex:
        print(f"Erro ao listar {mclass.__name__}: {ex}")
        return {"result": "error", "details": str(ex)}


# --- CRUD Atleta ---
@app.route('/atletas', methods=['POST'])
def create_atleta():
    data = request.json
    try:
        with db_session:
            atleta = Atleta(
                nome=data["nome"],
                dt_nasc=data["dt_nasc"],
                email=data["email"],
                cpf=data["cpf"],
            )

            # Foto opcional
            if "foto_url" in data and data["foto_url"]:
                Foto(url=data["foto_url"], atleta=atleta)

            # Relaciona o atleta aos times (lista de IDs)
            if "times_ids" in data and isinstance(data["times_ids"], list):
                for tid in data["times_ids"]:
                    time = Time.get(id=tid)
                    if time:
                        atleta.times.add(time)

            commit()
            return jsonify({"result": "ok", "id": atleta.id}), 201

    except Exception as e:
        print("Erro ao criar Atleta:", e)
        return jsonify({"result": "error", "details": str(e)}), 500


@app.route('/atletas', methods=['GET'])
def list_atletas():
    myjson = get_objects_helper(Atleta)
    return jsonify(myjson), 200 if myjson["result"] == "ok" else 500


@app.route('/atletas/<int:obj_id>', methods=['DELETE'])
def delete_atleta(obj_id):
    myjson = delete_object_by_id(Atleta, obj_id)
    return jsonify(myjson), 204 if myjson["result"] == "ok" else 500


# --- CRUD Treinador ---
@app.route('/treinadores', methods=['POST'])
def create_treinador():
    data = request.json
    answer = create_simple_object(Treinador, data)
    return jsonify(answer), 201 if answer["result"] == "ok" else 500


@app.route('/treinadores', methods=['GET'])
def list_treinadores():
    myjson = get_objects_helper(Treinador)
    return jsonify(myjson), 200 if myjson["result"] == "ok" else 500


@app.route('/treinadores/<int:obj_id>', methods=['DELETE'])
def delete_treinador(obj_id):
    myjson = delete_object_by_id(Treinador, obj_id)
    return jsonify(myjson), 204 if myjson["result"] == "ok" else 500


# --- CRUD Time ---
@app.route('/times', methods=['POST'])
def create_time():
    data = request.json
    answer = create_simple_object(Time, data)
    return jsonify(answer), 201 if answer["result"] == "ok" else 500

@app.route('/times', methods=['GET'])
def list_times():
    myjson = get_objects_helper(Time)
    return jsonify(myjson), 200 if myjson["result"] == "ok" else 500

@app.route('/times/<int:obj_id>', methods=['DELETE'])
def delete_time(obj_id):
    myjson = delete_object_by_id(Time, obj_id)
    return jsonify(myjson), 204 if myjson["result"] == "ok" else 500


# --- CRUD Treino ---
@app.route('/treinos', methods=['POST'])
def create_treino():
    data = request.json
    answer = create_simple_object(Treino, data)
    return jsonify(answer), 201 if answer["result"] == "ok" else 500

@app.route('/treinos', methods=['GET'])
def list_treinos():
    myjson = get_objects_helper(Treino)
    return jsonify(myjson), 200 if myjson["result"] == "ok" else 500

@app.route('/treinos/<int:obj_id>', methods=['DELETE'])
def delete_treino(obj_id):
    myjson = delete_object_by_id(Treino, obj_id)
    return jsonify(myjson), 204 if myjson["result"] == "ok" else 500


# --- CRUD Foto ---
@app.route('/fotos', methods=['POST'])
def create_foto():
    data = request.json
    answer = create_simple_object(Foto, data)
    return jsonify(answer), 201 if answer["result"] == "ok" else 500

@app.route('/fotos', methods=['GET'])
def list_fotos():
    myjson = get_objects_helper(Foto)
    return jsonify(myjson), 200 if myjson["result"] == "ok" else 500

@app.route('/fotos/<int:obj_id>', methods=['DELETE'])
def delete_foto(obj_id):
    myjson = delete_object_by_id(Foto, obj_id)
    return jsonify(myjson), 204 if myjson["result"] == "ok" else 500


print("Rotas de Esportes carregadas com sucesso.")
