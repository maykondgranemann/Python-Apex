from flask import Flask, render_template
from pessoas import listar

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/listar')
def listar_pessoas():
    return render_template('listar.html', pessoas = listar())

app.run(debug=True)