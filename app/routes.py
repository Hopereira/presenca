# definindo as rotas da aplicação
#importa a função app da aplicação
from app import app
# importa a classe Flask da biblioteca flask
from flask import Flask
# importa a função render_template da biblioteca flask
from flask import render_template
# importa a função request da biblioteca flask
from flask import request
# importa a função redirect da biblioteca flask
from flask import redirect
# importa a função url_for da biblioteca flask
from flask import url_for
# configuração da rota raiz
@app.route('/')
def home():
    return "Hello, World!"