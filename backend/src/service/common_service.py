from src.config import *
from src.model import *
<<<<<<< HEAD:backend/src/service/common_service.py
from pony.orm import db_session, select#, query
=======
from pony.orm import db_session, select
>>>>>>> 08fd2efc0ade51fc8b0c7ecfdd1253f95de9ac28:src/service/common_service.py
from src.utils import serialize_model
# --- CREATE ---

@db_session
def create_object(m_class, **kwargs):
    obj = m_class(**kwargs)
    db.commit()
    return obj


@db_session
def create_object_return_json(m_class, **kwargs):
    obj = m_class(**kwargs)
    db.commit()
    db.flush()
    response = serialize_model(obj)
    return response


# --- GET ---

@db_session
def get_objects(m_class):
    #return query(m_class).all()
    lista= list(m_class.select()) # [:]
    return lista
    #return select(o for o in m_class)[:]


@db_session
def get_objects_json(m_class):
    objs = list(m_class.select())
    serialized = []

    for o in objs:
        data = o.to_dict()

        # Caso seja um atleta, adiciona as relações
        if isinstance(o, Atleta):
            data["times"] = [
                {"id": t.id, "esporte": t.esporte} for t in o.times
            ]
            data["ft_perfil"] = o.ft_perfil.id if o.ft_perfil else None

        serialized.append(data)

    return serialized



@db_session
def get_object_by_attribute(m_class, attribute, value):
    return select(o for o in m_class if getattr(o, attribute) == value).first()


# Exemplos de funções específicas, caso queira buscar por nome
@db_session
def get_atleta_by_name(value):
    atletas = Atleta.select(nome=value)
    for a in atletas:
        return a
    return None


@db_session
def get_treinador_by_name(value):
    treinadores = Treinador.select(nome=value)
    for t in treinadores:
        return t
    return None


# --- DELETE ---

@db_session
def delete_object_by_id(model, obj_id):
    with db_session:
        obj = model.get(id=obj_id)
        if obj:
            obj.delete()
            return {"result": "ok"}
        return {"result": "error", "message": f"{model.__name__} not found"}


@db_session
def delete_object(obj):
    try:
        obj.delete()
        return "ok"
    except Exception as ex:
        return str(ex)