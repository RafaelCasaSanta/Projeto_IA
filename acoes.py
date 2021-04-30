from enum import Enum
from dataclasses import dataclass

class AcoesJogador(Enum):
    MOVER_JOGADOR = 'MoverJogador'

class DirecaoMoverJogador(Enum):
    DIREITA = 'Direita'
    ESQUERDA = 'Esquerda'
    CIMA = 'Cima'
    BAIXO = 'Baixo'

@dataclass
class AcaoJogador():
    tipo: str
    parametros: str   
     
        
    @classmethod
    def MOVER_JOGADOR(cls, direcao: DirecaoMoverJogador) -> 'AcaoJogador':
        return cls(AcoesJogador.MOVER_JOGADOR, (direcao))
    