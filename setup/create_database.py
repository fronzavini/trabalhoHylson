from src.config import *
from model import *
from pony.orm import db_session

# optando por criar as tabelas
db.generate_mapping(create_tables=True)
db.create_tables()
   
print("Database created")