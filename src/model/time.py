from src.config import db
from pony.orm import Database, Required, PrimaryKey, Optional, LongStr, Set, db_session, commit, rollback, select
from datetime import date
from flask import Flask, jsonify, request, abort, render_template, redirect, flash, session, url_for
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import os
from src.model.atleta import Atleta

class Time(db.Entity):
    id = PrimaryKey(int, auto=True)
    esporte = Required(str)  # Ex: "Futebol", "Basquete"
    atletas = Set(Atleta)
    treinos = Set("Treino") 