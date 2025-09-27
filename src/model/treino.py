from src.config import db
from pony.orm import Database, Required, PrimaryKey, Optional, LongStr, Set, db_session, commit, rollback, select
from datetime import date
from flask import Flask, jsonify, request, abort, render_template, redirect, flash, session, url_for
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import os
from src.model.time import Time
from src.model.treinador import Treinador

class Treino(db.Entity):
    id = PrimaryKey(int, auto=True)
    data = Required(date)
    horario = Required(str)
    time = Required(Time)       # atributo reverso: Time.treinos
    local = Required(str)       # Ex: quadra, pista, gramado
    treinador = Required(Treinador)  # atributo reverso: Treinador.treinos
    atleta = Optional("Atleta")      # se quiser vincular um atleta específico
