import numpy as np
from typing import Tuple, Set, Optional
from dataclasses import dataclass

@dataclass
class PercepcoesJogador(): 
      
    tabuleiro: np.array
    dimensoes: Tuple[int, int] = (8,8)
    mensagem_jogo: Optional[str] = None   
   