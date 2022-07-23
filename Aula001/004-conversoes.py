cabecalho = '-'*10
print(cabecalho,'Sistema de cadastro de produtos',cabecalho)
nome = input('Digite o nome do produto:')
descricao = input('Digite a descrição do produto:')
valor = input('Digite o valor do produto:') # str
valor = float(valor) # float
quantidade = int(input('Digite a quantidade do produto:'))
perecivel = bool(input('Perecivel?(True/False):'))

print('O produto\n\t', nome,'-', descricao, 'de valor: R$', valor,
     'e quantidade', quantidade, '(percível:', perecivel, ')',
     '\nfoi cadastrado com sucesso!')

print(type(valor))
