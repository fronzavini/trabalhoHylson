import pytest
from src.config import *
from src.service.common_service import *
from src.model.atleta import Atleta
from src.model.foto import Foto



def test_foto_creation():
    with app.app_context():
        with db_session:
            # Criar atleta para associar a foto
            atleta = create_object(Atleta,
                nome="Pedro",
                dt_nasc="1998-08-08",
                email="pedro@gmail.com",
                cpf="11122233344"
            )
            foto = create_object(Foto,
                url="https://upload.wikimedia.org/wikipedia/commons/1/18/Lionel-Messi-Argentina-2022-FIFA-World-Cup_sharpness.jpg",
                atleta=atleta
            )
            assert foto.id is not None
            assert isinstance(foto.id, int)
            assert foto.url == "https://upload.wikimedia.org/wikipedia/commons/1/18/Lionel-Messi-Argentina-2022-FIFA-World-Cup_sharpness.jpg"
            assert foto.atleta.id == atleta.id

def test_foto_delete():
    with app.app_context():
        with db_session:
            foto = get_object_by_attribute(Foto, "url", "https://upload.wikimedia.org/wikipedia/commons/1/18/Lionel-Messi-Argentina-2022-FIFA-World-Cup_sharpness.jpg")
            assert foto is not None
            ok = delete_object(foto)
            assert ok == "ok"