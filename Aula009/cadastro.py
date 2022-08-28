from pessoa import Pessoa

def cadastrar_nomes(pessoa:Pessoa):
    arquivo = open('Aula009/nomes.txt', 'a')
    arquivo.write(f'{pessoa}\n')
    arquivo.close()

def listar_nomes():
    nomes = []
    arquivo = open('Aula009/nomes.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        linha_nome = linha.split(';')
        pessoa = Pessoa(linha_nome[0],linha_nome[1])
        nomes.append(pessoa)
    return nomes