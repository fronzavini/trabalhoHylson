from pony.orm import Database, Required, PrimaryKey, Optional, LongStr, Set, db_session, commit, rollback, select
from datetime import date
from flask import Flask, jsonify, request, abort, render_template, redirect, flash, session, url_for
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import os
from model.py import *


DATABASE_URL = ""

# persistency of classes were tested in 
# sqlite and mysql, in 17/07/2025
# default configuration: sqlite
MY_DB = "SQLITE"

# Accessing an environment variable directly
try:
    db_env = os.environ['MY_DB']
    if db_env == "MYSQL":
      MY_DB = "MYSQL"
except KeyError:
    print("MY_DB environment variable is not set, considering default database: SQLITE.")

# create the app
app = Flask(__name__)
CORS(app)

# database configuration
db = Database()

if MY_DB == "SQLITE":
    # some commands to make the database be created
    # at this folder
    import os
    this_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(this_path, 'database.db')
    db.bind(provider='sqlite', filename=file_path, create_db=True)
elif MY_DB == "MYSQL":
    db.bind(
        provider='mysql',
        host='localhost',
        user='sira',
        password='minhasenha',
        database='database'
    )

print("Configuration loaded successfully.")
