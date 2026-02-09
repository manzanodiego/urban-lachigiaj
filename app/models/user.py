from app.utils.extensions import db
from sqlalchemy import Enum
import enum

class TipoUsuario(enum.Enum):
    cliente = "cliente"
    admin = "admin"

class User(db.Model):
    __tablename__ = "usuarios"
    
    iduser = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(100))
    numero_telefono = db.Column(db.String(12))
    contrasena = db.Column(db.String(255))
    tipo = db.Column(Enum(TipoUsuario), nullable = False)