import numpy as np
from typing import Tuple
from .regras_abstratas import AbstractRegrasJogo
from .personagens import Personagens
from percepcoes import PercepcoesJogador
from acoes import AcoesJogador, DirecaoMoverJogador


class sokoban(AbstractRegrasJogo):
    def __init__(self) -> None:
        super().__init__()
        tabuleiro_completo = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 3, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 4, 1, 0, 1],
            [1, 0, 0, 0, 2, 1, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
          ]

        self.tabuleiro = np.array(tabuleiro_completo)
        self.id_personagens = {Personagens.JOGADOR_SOKOBAN: 4}
        self.acoes_personagens = {0: None}
        self.msg_jogador = None

    @property
    def get_buraco(self) -> bool:
        # retorna se há buracos no tabuleiro
        if 2 not in self.tabuleiro:
            return True

    def get_caixa(self) -> tuple():
      # retorna se existir caixas no tabuleiro.
      posicao = np.where(self.tabuleiro == 3)
      coordenadas = zip(posicao[0], posicao[1])
      x, y = coordenadas
      return x,y 
      
    def get_jogador(self) -> tuple() :
      # Retorna posição do jogador
      posicao = np.where(self.tabuleiro == 4)
      coordenadas = list(zip(posicao[0], posicao[1]))
      for cord in coordenadas:
       x, y = cord
      return x,y 
      

    def registrarAgentePersonagem(self, personagem):
        return self.id_personagens[personagem]

    def isFim(self):
        return self.get_buraco

    def gerarCampoVisao(self, id_agente):
        percepcoes_jogador = PercepcoesJogador(tabuleiro=self.tabuleiro,
                                               dimensoes=(8, 8),
                                               mensagem_jogo=self.msg_jogador)

        self.msg_jogador = None
        return percepcoes_jogador

    def registrarProximaAcao(self, id_agente, acao) -> None:
        self.acoes_personagens[id_agente] = acao

    def atualizarEstado(self, diferencial_tempo):
        acao_jogador = self.acoes_personagens[self.id_personagens[
            Personagens.JOGADOR_SOKOBAN]]
        if acao_jogador.tipo == AcoesJogador.MOVER_JOGADOR:
            direcao = acao_jogador.parametros
            
            x_jog, y_jog = self.get_jogador()
          
            x_mov, y_mov = self.decodificar_direcao(direcao)
            
            espaco_pos_adjacente = (x_jog + x_mov,y_jog + y_mov)
            movimentacao = x_mov, y_mov
            if self.is_jogada_valida(espaco_pos_adjacente, movimentacao):
                self.tabuleiro[x_jog][y_jog] = 0
                if self.isFim() == True:
                  self.terminarJogo()
            else:
                self.msg_jogador = f'Direção especificada para movimento não é possível.'    
        else:
            self.msg_jogador = f'Ação especificada inválida.' 
    

    def terminarJogo(self) -> bool:
        print("Venceu!")
        return True


    def is_jogada_valida(self, espaco_pos_adjacente: Tuple[int, int], direcao: Tuple[int,int]) -> bool:
        proxima_casa = self.get_espaco_tabuleiro(espaco_pos_adjacente)
        xp, yp = espaco_pos_adjacente
        xd, yd = direcao
        if proxima_casa < 1:
          #vazio
          self.tabuleiro[xp][yp] = 4
          return True
        elif proxima_casa == 3:
          #se  caixa
          proxima_pos_caixa = (xp+xd,yp+yd)
          if self.get_espaco_tabuleiro(proxima_pos_caixa) == 0:
            self.tabuleiro[xp][yp] = 4
            self.tabuleiro[xp+xd][yp+yd] = 3
            return True
          elif self.get_espaco_tabuleiro(proxima_pos_caixa) == 2:
            self.tabuleiro[xp][yp] = 4
            self.tabuleiro[xp+xd][yp+yd] = 3
            return True
          return False  
        elif proxima_casa == 2:
          # buraco
          return False
        else:
          return False
    
    
    def get_espaco_tabuleiro(self, tab: Tuple[int,int]) -> int:
      x, y = tab
      espaco = self.tabuleiro[x][y]
      return espaco 
        

    @staticmethod
    def decodificar_direcao(direcao) -> Tuple[int, int]:
        if direcao == DirecaoMoverJogador.BAIXO:
            return (1, 0)
        elif direcao == DirecaoMoverJogador.CIMA:
            return (-1, 0)
        elif direcao == DirecaoMoverJogador.DIREITA:
            return (0, 1)
        elif direcao == DirecaoMoverJogador.ESQUERDA:
            return (0, -1)
        else:
            raise ValueError(f"Direção {direcao} é inválida.")


def construir_jogo(*args, **kwargs):
    return sokoban()
