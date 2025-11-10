import pytest
from src.config import *
from src.service.common_service import *
from src.model import Time

def test_time_creation():
    with app.app_context():
        with db_session:
            time = create_object(Time,
                esporte="Futebol"
            )
            assert time.id is not None
            assert isinstance(time.id, int)
            assert time.esporte == "Futebol"

def test_time_delete():
    with app.app_context():
        with db_session:
            time = get_object_by_attribute(Time, "esporte", "Futebol")
            assert time is not None
            ok = delete_object(time)
            assert ok == "ok"