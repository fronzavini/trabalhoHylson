from src.config import *
from src.route.routes import *

db.generate_mapping(create_tables=False)

print('Aplicação iniciada com sucesso')