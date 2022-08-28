class Endereco:
    def __init__(self, rua:str, numero:int, complemento:str, bairro:str, cidade:str, estado:str, cep:str) -> None:
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def __str__(self) -> str:
        return f'{self.rua};{self.numero};{self.complemento};{self.bairro};{self.cidade};{self.estado};{self.cep}'
        