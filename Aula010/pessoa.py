class Pessoa: #classe mae ou classe base
    def __init__(self,nome:str, sobrenome:str, cpf:str, idade:int) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.idade = idade

    def __str__(self) -> str:
        return f'{self.nome};{self.sobrenome};{self.cpf};{self.idade}'