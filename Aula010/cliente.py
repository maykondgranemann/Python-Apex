from pessoa import Pessoa

class Cliente(Pessoa): # classes filhas ou classes derivadas
    def __init__(self, nome:str, sobrenome:str, cpf:str, idade:int, endereco:str) -> None:
        super().__init__(nome, sobrenome, cpf, idade)
        self.endereco = endereco

    def __str__(self) -> str:
        return f'{super().__str__()};{self.endereco}'