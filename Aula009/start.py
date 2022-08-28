from flask import Flask, render_template, request, redirect
from cadastro import listar_nomes, cadastrar_nomes

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    cadastrar_nomes(nome, sobrenome)
    return  redirect('/listar')

@app.route('/listar')
def listar():
    lista_nomes = listar_nomes()
    return render_template('listar.html', nomes=lista_nomes)

app.run(debug=True)