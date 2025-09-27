from src.config import db
from pony.orm import Database, Required, PrimaryKey, Optional, LongStr, Set, db_session, commit, rollback, select
from datetime import date
from flask import Flask, jsonify, request, abort, render_template, redirect, flash, session, url_for
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import os
  
class Treinador(db.Entity):
    id = PrimaryKey(int, auto=True)
    nome = Required(str)
    dt_nasc = Required(date)
    email = Required(str, unique=True)
    cpf = Required(str, unique=True)
    cref = Required(str, unique=True)
    treinos = Set("Treino")
    ft_perfil = Optional("Foto", cascade_delete=True)
