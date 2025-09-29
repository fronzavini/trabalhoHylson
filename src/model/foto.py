from config import db
from pony.orm import Database, Required, PrimaryKey, Optional, LongStr, Set, db_session, commit, rollback, select
from datetime import date
from flask import Flask, jsonify, request, abort, render_template, redirect, flash, session, url_for
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import os
from model.treinador import Treinador
from model.atleta import Atleta

class Foto(db.Entity):
    id = PrimaryKey(int, auto=True)
    url = Required(str)
    treinador = Optional(Treinador)
    atleta = Optional(Atleta)
