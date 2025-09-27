from config import *
from model import *
from pony.orm import db_session, select
from utils import serialize_model
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
    return select(o for o in m_class)[:]


@db_session
def get_objects_json(m_class):
    objs = select(o for o in m_class)[:]
    return [o.to_dict() for o in objs]


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
def delete_object_by_id(m_class, object_id):
    try:
        obj = m_class.get(id=object_id)
        if obj:
            obj.delete()
            return "ok"
        return f"{m_class.__name__} with id {object_id} not found"
    except Exception as ex:
        return str(ex)


@db_session
def delete_object(obj):
    try:
        obj.delete()
        return "ok"
    except Exception as ex:
        return str(ex)
