from app import db
from datetime import datetime

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    presencas = db.relationship('Presenca', backref='aluno', lazy='dynamic')

class Presenca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_hora = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'))