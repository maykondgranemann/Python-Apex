def salvar(nome):
    with open('Aula005/pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{nome}\n')

def listar():
    nomes = []
    with open('Aula005/pessoas.txt', 'r') as arquivo:
        for l in arquivo:
            l = l.strip()
            nomes.append(l)            
    return nomes

# salvar('Maykon')
# print(listar())    