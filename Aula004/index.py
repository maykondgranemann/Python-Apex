from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Olá"

@app.route('/pessoas')
def pessoas():
    return 'olá, pessoas'

app.run(debug=True)