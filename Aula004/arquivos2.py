arquivo = open('Aula004/produtos.txt', 'a')
arquivo.write('smartphone;preto;R$1999.00\n') # formato CSV
arquivo.close()

arquivo = open('Aula004/produtos.txt','r')
for linha in arquivo:
    linha = linha.strip()
    dados = linha.split(';') # forma uma lista, cria um elemento para cada caracter encontrado 
    print(f'Nome: {dados[0]} cor: {dados[1]} valor: {dados[2]} ') # fstrings, interpolacao de string
arquivo.close()

arquivo = open('Aula004/produtos.txt','r')
for linha in arquivo:
    dados = linha.strip().split(';')
    print(f'Nome: {dados[0]} cor: {dados[1]} valor: {dados[2]} ')
arquivo.close()