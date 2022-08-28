class Pessoa:
    def __init__(self, nome, sobrenome):
       self.nome = nome
       self.sobrenome = sobrenome

pessoa1 = Pessoa('chimba', 'das guitarras')

print(pessoa1.nome)
print(pessoa1.sobrenome)