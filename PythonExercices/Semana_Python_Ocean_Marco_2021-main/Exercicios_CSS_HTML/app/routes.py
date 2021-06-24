#Rotas
#   Pasta       App Criado
from app import app
#Arquivos Html
from flask import render_template


#Call de APP de Rota do site
@app.route('/')
@app.route('/index')

def index():
    user = {'username':'Rw'}
    posts = [
        {'author' : {'username': 'R_W'},
            'body' : "Texto de User R_W" 
        },
        { 'author' : {'username': ' User Number 2'},
            'body' : "Texto de User Number 2"
        }
    ]
    return render_template("index.html", user=user, posts=posts)