from pessoa import Pessoa
from endereco import Endereco

class Cliente(Pessoa): # classes filhas ou classes derivadas
    def __init__(self, nome:str, sobrenome:str, cpf:str, idade:int, endereco:Endereco): #composicao classe endereco na classe Cliente
        super().__init__(nome, sobrenome, cpf, idade)
        self.endereco = endereco

    def __str__(self) -> str:
        return f'{super().__str__()};{self.endereco}'


# testes
end1 = Endereco('Rua j', 45, '', 'Centro', 'Belem', 'Pará', '456254-654') 
cliente1 = Cliente('jojo', 'do calipso', '454645556', 15, end1)

print(cliente1.endereco.numero)

