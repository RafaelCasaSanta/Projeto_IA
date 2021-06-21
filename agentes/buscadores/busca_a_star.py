import queue
import time
from typing import Tuple
from agentes.problemas.sokoban import *

from percepcoes import PercepcoesJogador
from acoes import AcaoJogador, DirecaoMoverJogador

from agentes.abstrato import AgenteAbstrato
from agentes.problemas.sokoban import ProblemaSokoban
from agentes.buscadores.heuristicas import busca_heuristica
import numpy as np
from typing import Tuple

# Implementar agente com busca A*
#

class AgenteAStar(AgenteAbstrato):
    def __init__(self) -> None:
        super().__init__()
        self.tabuleiro: np.array
        self.lista = list = ('e','c','c','c','e','e','b','d','c','d','b','b','b','c','c','e','e','b','b','b','d','d')

    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        AgenteAStar.desenhar_tabuleiro(percepcao_mundo)
        self.tabuleiro = percepcao_mundo.tabuleiro

            

    def escolherProximaAcao(self,ind:int):
      
      posicao = np.where(self.tabuleiro == 4)
      coordenadas = list(zip(posicao[0], posicao[1]))
      
      self.solucao = busca_heuristica.fila_de_acoes(busca_heuristica, coordenadas[0], self.lista[ind])
      acao = self.solucao[0]
      direcoes = AgenteAStar.traduzir_acao_jogo(acao[0])

      print('Direção')
      print(direcoes)
      print('Custo')
      print(acao[1] + acao[2])   
      print('  ')   
      print('  ') 
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
        """Escreve na tela para o usuário saber o que seu agente está percebendo.
        """
        
        print("Tabuleiro")
        print(percepcao_mundo.tabuleiro)

        if percepcao_mundo.mensagem_jogo:
            print(f'Mensagem do jogo: {percepcao_mundo.mensagem_jogo}')
    
    def get_melhorAcao(solucao: np.array):
        melhorAcao = solucao[0,0]
        beneficio = solucao[0,1] + solucao[0,2]

        if (solucao[1,1] + solucao[1,2]) < beneficio :
          melhorAcao = solucao[1,0]
          beneficio = solucao[1,1] + solucao[1,2]

        if (solucao[2,1] + solucao[2,2]) < beneficio :
          melhorAcao = solucao[2,0]
          beneficio = solucao[2,1] + solucao[2,2]
        
        if (solucao[3,1] + solucao[3,2]) < beneficio :
          melhorAcao = solucao[3,0]
          beneficio = solucao[3,1] + solucao[3,2]
        
        return melhorAcao