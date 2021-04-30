import numpy as np
from typing import Sequence, Set
from dataclasses import dataclass


@dataclass
class jogador:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash(self.x) + hash(self.y)

    def __str__(self) -> str:
        return f'B({self.x},{self.y})'


@dataclass
class EstadoSokoban:
    tabuleiro: np.array


@dataclass
class Mover:
    jogador: jogador
    direcao: str

    def __str__(self) -> str:
        return f'Mover({self.direcao})'


class ProblemaSokoban:
    @staticmethod
    def estado_inicial(*args, **kwargs) -> EstadoSokoban:
        niveis = {
            'completo':
            EstadoSokoban[[1, 1, 1, 1, 1, 1, 1, 1], 
                          [1, 0, 0, 0, 1, 1, 1, 1],
                          [1, 0, 3, 0, 0, 0, 0, 1],
                          [1, 0, 1, 0, 1, 1, 0, 1],
                          [1, 0, 1, 0, 4, 1, 0, 1], 
                          [1, 0, 0, 0, 2, 1, 0, 1],
                          [1, 1, 1, 1, 0, 0, 0, 1], 
                          [1, 1, 1, 1, 1, 1, 1, 1]]
        }
        return niveis[kwargs.get('nivel', 'completo')]

    @staticmethod
    #açoes possiveis da maquina.
    def acoes(estado: EstadoSokoban) -> Sequence[Mover]:
        acoes_possiveis = list()
        jogador = 4
        caixa = 3

        for jogador in estado.tabuleiro:
          posicao = np.where(estado.tabuleiro == jogador)
          coordenadas = list(zip(posicao[0], posicao[1]))
          for cord in coordenadas:
            x, y = cord
            posicao_jogador

          #direita
          proxima_casa = (x,y+1)
          conteudo = self.get_EstadoSokoban(proxima_casa)
          if jogada_valida(conteudo,jogador) is True:
            if conteudo == caixa:
              casa_adjacente = (proxima_casa.x,proxima_casa.y +1)
              conteudo_adjacente = self.get_EstadoSokoban(casa_adjacente)
              if jogada_valida(conteudo_adjacente, caixa) is True:
                 acoes_possiveis.append(Mover(posicao_jogador, 'direita'))
            else:
              acoes_possiveis.append(Mover(posicao_jogador, 'direita'))


          #esquerda
          proxima_casa = (x,y-1)
          conteudo = self.get_EstadoSokoban(proxima_casa)
          if jogada_valida(conteudo,jogador) is True:
            if conteudo == caixa:
              casa_adjacente = (proxima_casa.x,proxima_casa.y-1)
              conteudo_adjacente = self.get_EstadoSokoban(casa_adjacente)
              if jogada_valida(conteudo_adjacente, caixa) is True:
                 acoes_possiveis.append(Mover(posicao_jogador, 'esquerda'))
            else:
              acoes_possiveis.append(Mover(posicao_jogador, 'esquerda'))

          #cima
          proxima_casa = (x-1,y)
          conteudo = self.get_EstadoSokoban(proxima_casa)
          if jogada_valida(conteudo,jogador) is True:
            if conteudo == caixa:
              casa_adjacente = (proxima_casa.x-1,proxima_casa.y)
              conteudo_adjacente = self.get_EstadoSokoban(casa_adjacente)
              if jogada_valida(conteudo_adjacente, caixa) is True:
                 acoes_possiveis.append(Mover(posicao_jogador, 'cima'))
            else:
              acoes_possiveis.append(Mover(posicao_jogador, 'cima'))

          #baixo
          proxima_casa = (x+1,y)
          conteudo = self.get_EstadoSokoban(proxima_casa)
          if jogada_valida(conteudo,jogador) is True:
            if conteudo == caixa:
              casa_adjacente = (proxima_casa.x+1,proxima_casa.y)
              conteudo_adjacente = self.get_EstadoSokoban(casa_adjacente)
              if jogada_valida(conteudo_adjacente, caixa) is True:
                 acoes_possiveis.append(Mover(posicao_jogador, 'baixo'))
            else:
              acoes_possiveis.append(Mover(posicao_jogador, 'baixo'))
    return acoes_possiveis()
          
          
        
    def jogada_valida(conteudo: int, peca: int) -> bool:
      if conteudo == 0: #vazio
          return True
      elif conteudo == 3: #caixa
          return True
      elif conteudo == 2: #buraco  
       if peca == 3:
          return True   
      else:
        return False    
    
    
    def get_EstadoSokoban(self, tab: Tuple[int,int]) -> int:
      x, y = tab
      espaco = self.tabuleiro[x][y]
      return espaco 

    @staticmethod
    def resultado(estado: EstadoSokoban, acao: Mover) -> EstadoSokoban:
        estado_resultante = EstadoSokoban(set(estado.tabuleiro))
        x, y = acao.jogador.x, acao.jogador.y

        estado_resultante.tabuleiro.discard(acao.jogador)
        if acao.direcao == 'cima':
            estado_resultante.tabuleiro.add(jogador(x - 1, y))

        elif acao.direcao == 'baixo':
            estado_resultante.tabuleiro.add(jogador(x + 1, y ))

        elif acao.direcao == 'direita':
            estado_resultante.tabuleiro.add(jogador(x, y + 1))

        elif acao.direcao == 'esquerda':
            estado_resultante.tabuleiro.add(jogador(x, y - 1))

        else:
            raise ValueError("Movimento especificado inválido, cheater!")

        return estado_resultante

    @staticmethod
    def teste_objetivo(estado: EstadoSokoban) -> bool:
         if 2 not in estado.tabuleiro
           return True
        return False

    @staticmethod
    def custo(inicial: EstadoSokoban, acao: Mover,
              resultante: EstadoSokoban) -> int:
        """Custo em quantidade de jogadas"""
        return 1
