class Pessoa:
    def __init__(self, nome, sobrenome):
       self.nome = nome
       self.sobrenome = sobrenome
    
    def __str__(self):
        return f'{self.nome};{self.sobrenome}'

pessoa1 = Pessoa('chimba', 'das guitarras')
print(pessoa1)