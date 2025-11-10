from src.config import *

db = Database()

class Atleta(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    dt_nasc = Required(date)
    email = Required(str, unique=True)
    cpf = Required(str, unique=True)
    times = Set("Time")
    ft_perfil = Optional("Foto", cascade_delete=True)
    
class Treinador(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    dt_nasc = Required(date)
    email = Required(str, unique=True)
    cpf = Required(str, unique=True)
    cref = Required(str, unique=True)
    treinos = Set("Treino")
    ft_perfil = Optional("Foto", cascade_delete=True)

class Time(db.Entity):
    id = PrimaryKey(int, auto=True)
    esporte = Required(str)  # Ex: "Futebol", "Basquete"
    atletas = Set(Atleta)
    treinos = Set('Treino')

class Treino(db.Entity):
    id = PrimaryKey(int, auto=True)
    data = Required(date)
    horario = Required(str)
    time = Required(Time) # Time que fará o treino
    local = Required(str)  # Ex: quadra, pista, gramado
    treinador = Required(Treinador)

class Foto(db.Entity):
    id = PrimaryKey(int, auto=True)
    url = Required(str)
    treinador = Optional(Treinador)
    atleta = Optional(Atleta)

db.bind(provider='sqlite', filename="esportes.db", create_db=True)
db.generate_mapping(create_tables=True)