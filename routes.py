from config import *  # arquivo onde estão Atleta, Treinador, Time, Treino e Foto
from model import *
from common_service import *

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
        objs_json = get_objects_json(mclass)
        myjson.update({"details": objs_json})
        return myjson
    except Exception as ex:
        print(f"Erro ao listar {mclass.__name__}: {ex}")
        return {"result": "error", "details": str(ex)}


# --- CRUD Atleta ---

# curl -X POST -H "Content-Type: application/json" -d '{"nome":"Joao", "dt_nasc":"2000-05-01", "email":"joao@gmail.com", "cpf":"12345678901"}' localhost:5000/atletas
# curl -X GET localhost:5000/atletas
# curl -X DELETE localhost:5000/atletas/1
@app.route('/atletas', methods=['POST'])
def create_atleta():
    data = request.json
    answer = create_simple_object(Atleta, data)
    return jsonify(answer), 201 if answer["result"] == "ok" else 500


@app.route('/atletas', methods=['GET'])
def list_atletas():
    myjson = get_objects_helper(Atleta)
    return jsonify(myjson), 200 if myjson["result"] == "ok" else 500


@app.route('/atletas/<int:obj_id>', methods=['DELETE'])
def delete_atleta(obj_id):
    myjson = delete_object_by_id(Atleta, obj_id)
    return jsonify(myjson), 204 if myjson["result"] == "ok" else 500


# --- CRUD Treinador ---

# curl -X POST -H "Content-Type: application/json" -d '{"nome":"Carlos", "dt_nasc":"1980-01-01", "email":"carlos@gmail.com", "cpf":"98765432100", "cref":"CREF123"}' localhost:5000/treinadores
# curl -X GET localhost:5000/treinadores
# curl -X DELETE localhost:5000/treinadores/1   
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

# curl -X POST -H "Content-Type: application/json" -d '{"esporte":"Futebol"}' localhost:5000/times
# curl -X GET localhost:5000/times
# curl -X DELETE localhost:5000/times/1
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

# curl -X POST -H "Content-Type: application/json" -d '{"data":"2025-09-27", "horario":"10:00", "time":1, "local":"Quadra Central", "treinador":1}' localhost:5000/treinos
# curl -X GET localhost:5000/treinos
# curl -X DELETE localhost:5000/treinos/1
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

# curl -X POST -H "Content-Type: application/json" -d '{"url":"http://image.com/foto1.png", "atleta":1}' localhost:5000/fotos
# curl -X GET localhost:5000/fotos
# curl -X DELETE localhost:5000/fotos/1
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
