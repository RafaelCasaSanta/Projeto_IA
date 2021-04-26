from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
    MOVER_CAIXA = 'MoverCaixa'
    MOVER_PERSONAGEM = 'MoverPersonagem'

class DirecaoMoverCaixa(Enum):
    DIREITA = 'Direita'
    ESQUERDA = 'Esquerda'
    CIMA = 'Cima'
    BAIXO = 'Baixo'

class DirecaoMoverPersonagem(Enum):
    DIREITA = 'Direita'
    ESQUERDA = 'Esquerda'
    CIMA = 'Cima'
    BAIXO = 'Baixo'

@dataclass
class AcaoJogador():
    tipo: str
    parametros: tuple = tuple()     
     
    @classmethod
    def mover_caixa(cls, x: int, y: int, direcao: DirecaoMoverCaixa) -> 'AcaoJogador':
        return cls(AcoesJogador.MOVER_CAIXA, (x, y, direcao))

    @classmethod
    def andar(cls, x: int, y: int, direcao: DirecaoMoverPersonagem) -> 'AcaoJogador':
        return cls(AcoesJogador.MOVER_PERSONAGEM, (x, y, direcao))