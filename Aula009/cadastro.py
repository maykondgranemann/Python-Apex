def cadastrar_nomes(nome, sobrenome):
    arquivo = open('Aula009/nomes.txt', 'a')
    arquivo.write(f'{nome};{sobrenome}\n')
    arquivo.close()

def listar_nomes():
    nomes = []
    arquivo = open('Aula009/nomes.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        linha_nome = linha.split(';')
        nome_dict = {'nome': linha_nome[0], 'sobrenome':linha_nome[1]}
        nomes.append(nome_dict)
    return nomes