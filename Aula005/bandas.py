# arquivo = open('bandas.txt', 'a')
# arquivo.write('dejavu;para')
# arquivo.close()

with open('Aula005/bandas.txt', 'a') as arquivo:
    arquivo.write('dejavu;Belem/PA\n')

with open('Aula005/bandas.txt', 'r') as arquivo:
    for l in arquivo:
        dados = l.strip().split(';') 
        print(f"Nome:{dados[0]} Localizacao:{dados[1]}")
