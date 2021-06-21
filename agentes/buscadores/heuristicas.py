from typing import Any, Optional
from dataclasses import dataclass
import heapq
import numpy as np
from typing import Tuple
from percepcoes import PercepcoesJogador
from regras.regras_skb import construir_jogo


class busca_heuristica():
    fila_de_prioridade: np.array
    estado_inicial = [
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 3, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 4, 1, 0, 1],
            [1, 0, 0, 0, 2, 1, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]
          ]
    tabuleiro = np.array(estado_inicial)
    caixa = np.where(tabuleiro == 3)

    

    def fila_de_acoes(self, posicao: tuple(), acao) -> np.array:
        x,y = posicao
        jogadas = 0
        x_b = x
        y_b = y
        if acao == 'b' :
          while(jogadas == 0):
            x_b = x_b + 1
            y_b = y_b + 0
            custo_b = 0
            pcasa = self.get_tabuleiro(self,x_b, y_b) #"""BAIXO"""
            if pcasa == 0 or  pcasa == 3 :
              custo_b = custo_b + 1
              if pcasa == 3:
                print('Pegou a caixa')
            else:         
              jogadas = 1

          distancia_b = self.get_distancia(self, x + custo_b, y)
          fila_de_prioridade = [["b", custo_b, distancia_b]] 

        jogadas = 0
        x_c = x
        y_c = y
        if acao == 'c' :
          while(jogadas == 0):
            x_c = x_c - 1
            y_c = y_c + 0
            custo_c = 0
            pcasa = self.get_tabuleiro(self,x_c, y_c) #"""CIMA"""
            if pcasa == 0 or  pcasa == 3:
              custo_c = custo_c + 1
              if pcasa == 3:
                print('Pegou a caixa')
            else:
              jogadas = 1
          
          distancia_c = self.get_distancia(self, x - custo_c, y)
          fila_de_prioridade = [["c", custo_c, distancia_c]] 
        

        jogadas = 0
        x_d = x 
        y_d = y 
        if acao == 'd':
          while(jogadas == 0):
            
            x_d = x_d + 0
            y_d = y_d + 1
            custo_d = 0
            pcasa = self.get_tabuleiro(self, x_d, y_d)# """DIREITA"""
            if pcasa == 0 or  pcasa == 3 :
              custo_d = custo_d + 1
              if pcasa == 3:
                print('Pegou a caixa')
            else:
              jogadas = 1
          
          distancia_d = self.get_distancia(self, x, y + custo_d)
          fila_de_prioridade = [["d", custo_d, distancia_d]] 
        
        jogadas = 0
        x_e = x
        y_e = y
        if acao == 'e':
          while(jogadas == 0):
            
            x_e = x_e + 0
            y_e = y_e - 1
            custo_e = 0
            pcasa = self.get_tabuleiro(self,x_e, y_e) #"""ESQUERDA"""
            if pcasa == 0  or  pcasa == 3:
              custo_e = custo_e + 1
              if pcasa == 3:
                print('Pegou a caixa')
            else:
              jogadas = 1
        
          distancia_e = self.get_distancia(self, x, y - custo_e)

          fila_de_prioridade = [["e", custo_e, distancia_e]] 

        return fila_de_prioridade
      
    
    def isObjetive():
        return 0;

    def get_tabuleiro(self, x: int , y: int) -> int:
                
        proxima_casa = self.tabuleiro[x][y]
        return proxima_casa 
    
    def get_distancia(self, x:int, y:int)->int:
        caixa_x, caixa_y = self.caixa
        distancia_x = caixa_x - x
        distancia_y = caixa_y - y

        if distancia_x < 0:
          distancia_x = distancia_x * -1
        if distancia_y < 0:
          distancia_y = distancia_y * -1
        
        distancia = distancia_x + distancia_y
        
        return distancia




