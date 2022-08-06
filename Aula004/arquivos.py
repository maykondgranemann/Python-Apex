arquivo = open('Aula004/pessoas.txt', 'a') #abre o arquivo no formato de escrita, colocando o conteudo no final do arquivo
arquivo.write('Davi\n') # insere um texto com quebra de linha
arquivo.close() # fecha o arquivo

arquivo = open('Aula004/pessoas.txt', 'r') # abre no formato de leitura
for linha in arquivo:
    linha = linha.strip() # retira espaços e quebras de linhas do comeco e final da string
    print(linha) # print contem quebra de linha
arquivo.close()