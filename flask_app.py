from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Flask busca automáticamente este archivo dentro de la carpeta 'templates'
    return render_template('index.html')