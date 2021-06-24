#importar a classe FLASK
#   modulo      Classe FLASK
from flask import Flask

#Criar App
# Programa que fica "Online" e responde perguntas feitas a ele
app = Flask(__name__)

from app import routes