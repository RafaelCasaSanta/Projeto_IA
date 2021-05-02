import queue
import time
from typing import Tuple
from agentes.problemas.sokoban import *

from percepcoes import PercepcoesJogador
from acoes import AcaoJogador, DirecaoMoverJogador

from agentes.abstrato import AgenteAbstrato
from agentes.problemas.sokoban import ProblemaSokoban
from agentes.buscadores.busca import busca_arvore_bfs


class AgenteAutomaticoBfs(AgenteAbstrato):
    def __init__(self) -> None:
        super().__init__()

        self.problema: ProblemaSokoban = None
        self.solucao: list = ('e','c','c','c','e','e','b','d','c','d','b','b','b','c','c','e','e','b','b','b','d','d')

    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        """ Inspeciona a disposicao dos elementos no objeto de visao."""
        AgenteAutomaticoBfs.desenhar_tabuleiro(percepcao_mundo)
            

    def escolherProximaAcao(self,ind:int):

      if not self.solucao:
          no_solucao = busca_arvore_bfs(self.problema)
          self.solucao = no_solucao.caminho_acoes()
          print(len(self.solucao), self.solucao)
          if not self.solucao:
              raise Exception("Agente BFS não encontrou solução.")

          acao = self.solucao.pop(0)
          print(f"Próxima ação é {acao}.")
          time.sleep(2)

          direcoes= AgenteAutomaticoBfs.traduzir_acao_jogo(acao)

      if  self.solucao:
            acao = self.solucao[ind]
            direcoes=AgenteAutomaticoBfs.traduzir_acao_jogo(acao)
            
      return AcaoJogador.MOVER_JOGADOR(direcoes)

   
    @staticmethod
    def traduzir_acao_jogo(acao):
         direcoes = {
            'd': DirecaoMoverJogador.DIREITA,
            'e': DirecaoMoverJogador.ESQUERDA,
            'c': DirecaoMoverJogador.CIMA,
            'b': DirecaoMoverJogador.BAIXO
        }

         raw_d = acao
         direcao =  direcoes.get(raw_d.lower())
         if not direcao:
              raise ValueError() 
         return direcao


    @staticmethod
    def desenhar_tabuleiro(percepcao_mundo: PercepcoesJogador):
        """Escreve na tela para o usuário saber o que seu agente 
        está percebendo.
        """
        
        print("Tabuleiro")
        print(percepcao_mundo.tabuleiro)

        if percepcao_mundo.mensagem_jogo:
            print(f'Mensagem do jogo: {percepcao_mundo.mensagem_jogo}')

         

       