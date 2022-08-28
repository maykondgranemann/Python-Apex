from pessoa import Pessoa

class Funcionario(Pessoa): # classes filhas ou classes derivadas
    def __init__(self, nome:str, sobrenome:str, cpf:str, idade:int, cod_funcionario:int) -> None:
        super().__init__(nome, sobrenome, cpf, idade)
        self.cod_funcionario = cod_funcionario
    
    def __str__(self) -> str:
        return f'{super().__str__()};{self.cod_funcionario}'