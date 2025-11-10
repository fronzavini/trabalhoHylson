from datetime import datetime, date, time
from pony.orm.serialization import to_dict
import json

def current_time():
    return datetime.now().time()

def serialize_model(obj):
    return to_dict(obj)