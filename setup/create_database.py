from src.config import *
from src.model.atleta import *
from src.model.treino import *
from src.model.treinador import *
from src.model.time import *
from src.model.foto import *
from pony.orm import db_session

# optando por criar as tabelas
db.generate_mapping(create_tables=True)
db.create_tables()
   
print("Database created")