# Configuração do banco de dados
# Para configurar o banco de dados, é necessário instalar o pacote Flask-SQLAlchemy.
# importando bibliotecas necessárias
import os
basedir = os.path.abspath(os.path.dirname(__file__))# define o diretório base da aplicação
#criando a classe Config:
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')# define a URI do banco de dados
    SQLALCHEMY_TRACK_MODIFICATIONS = False# desativa o rastreamento de modificações