
class Crud:
    def __init__(self, nome_arquivo) -> None:
        self.nome = nome_arquivo

    def salvar(self, dado):
        arquivo = open(self.nome, 'a')
        arquivo.write(f'{dado}\n')
        arquivo.close()

    def listar(self) -> list:
        linhas = []
        arquivo = open(self.nome, 'r')
        for l in arquivo:
            l = l.strip()
            linhas.append(l)
        return linhas