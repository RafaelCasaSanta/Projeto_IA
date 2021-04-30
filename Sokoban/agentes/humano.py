import numpy as np
from typing import Tuple


from agentes.abstrato import AgenteAbstrato
from percepcoes import PercepcoesJogador
from acoes import AcaoJogador, DirecaoMoverJogador

class AgentePrepostoESHumano(AgenteAbstrato):
    
    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        """ Inspeciona a disposicao dos elementos no objeto de visao e escreve
        na tela para o usuário saber o que seu agente está percebendo.
        """
        print("\nNivel 01.")        
        print("1-parede 2-buraco 3-caixa 4-jogador")
        print("Tabuleiro:")
        print(percepcao_mundo.tabuleiro)
        print('-')
        if percepcao_mundo.mensagem_jogo:
            print(f'Mensagem do jogo: {percepcao_mundo.mensagem_jogo}')
    
    def escolherProximaAcao(self):
        jogada = None
        while not jogada:
            jogada = input("Escreva a direção (d|e|c|b): ").strip()
            try:                
                 d = AgentePrepostoESHumano.parse_jogada(jogada)            
            except ValueError:
                jogada = None
                print("Jogada entrada é inválida. Tente novamente.")

        return AcaoJogador.MOVER_JOGADOR(d)

    @staticmethod
    def parse_jogada(entrada: str) -> str:
        direcoes = {
            'd': DirecaoMoverJogador.DIREITA,
            'e': DirecaoMoverJogador.ESQUERDA,
            'c': DirecaoMoverJogador.CIMA,
            'b': DirecaoMoverJogador.BAIXO
        }

        raw_d = entrada
        direcao =  direcoes.get(raw_d.lower())
        if not direcao:
            raise ValueError()
        
        return direcao




