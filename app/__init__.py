# inicializa a aplicação e importa as rotas
from flask import Flask # importa a classe Flask do pacote flask
from flask_sqlalchemy import SQLAlchemy# importa a classe SQLAlchemy do pacote flask_sqlalchemy
app = Flask(__name__)# cria uma instância da classe Flask
from app import routes# importa o módulo routes do pacote app para que as rotas sejam registradas
from config import Config# importa o módulo config do pacote app para que a configuração da aplicação seja carregada
from flask_migrate import Migrate# importa a classe Migrate do pacote flask_migrate

app = Flask(__name__)# cria uma instância da classe Flask
app.config.from_object(Config)# carrega a configuração da aplicação
db = SQLAlchemy(app)# cria uma instância da classe SQLAlchemy
migrate = Migrate(app, db)# cria uma instância da classe Migrate

from app import routes, models# importa os módulos routes e models do pacote app para que as rotas e os modelos sejam registrados