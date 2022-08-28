# type hints -> indicacao de tipos / sugestao de tipos
from tkinter.messagebox import RETRY


def soma(n1:int, n2:int) -> int:
    return n1 + n2

def multiplicacao(n1:float, n2:float) -> float:
    return n1 * n2

r = soma('a', 'b') # o tipo é apenas sugestao, nao obrigatorio
r2 = multiplicacao(10.1, 5.8)
print(r, r2)