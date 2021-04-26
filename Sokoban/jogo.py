import os
import time
from regras_jogo.regras_resta_um import construir_jogo
from regras_jogo.personagens import Personagens
from agentes import construir_agente
from agentes.tipos import TiposAgentes

_ROOT = os.path.abspath(os.path.dirname(__file__))



"classe dos objetos no mundo"
class Level(object):
    parede = '*'
    buraco = 'o'
    caixa_buraco = '@'
    caixa = '#'
    jogador = 'J'
    chao = ' '


"puxar imagens para o jogo"

class Image(object):
  parede = os.path.join(_ROOT, 'img_mundo/parede.gif')
  buraco = os.path.join(_ROOT, 'img_mundo/buraco.gif')
  caixa_buraco = os.path.join(_ROOT, 'img_mundo/caixa_buraco.gif')
  caixa = os.path.join(_ROOT, 'img_mundo/caixa.gif')
  jogador = os.path.join(_ROOT, 'img_mundo/jogador.gif')
  jogador_buraco = os.path.join(_ROOT, 'img_mundo/jogador_buraco.gif')



def ler_tempo(em_turnos=False):
    """ Se o jogo for em turnos, retorna a passada de 1 rodada.
    
    Se não for em turno, é continuo ou estratégico, retorna tempo
    preciso (ns) do relógio.
    """
    return 1 if em_turnos else time.time()


def iniciar_jogo():
    
    # Inicializar e configurar jogo
    jogo = construir_jogo()
    personagem_jogador = jogo.registrarAgentePersonagem(Personagens.JOGADOR_SOKOBAN)
    agente_jogador = construir_agente(TiposAgentes.PREPOSTO_HUMANO, Personagens.JOGADOR_SOKOBAN)
    
    tempo_de_jogo = 0
    while not jogo.isFim():
        
        # Mostrar mundo ao jogador
        ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
        agente_jogador.adquirirPercepcao(ambiente_perceptivel)
        
        # Decidir jogada e apresentar ao jogo
        acao = agente_jogador.escolherProximaAcao()
        jogo.registrarProximaAcao(personagem_jogador, acao)

        # Atualizar jogo
        # tempo_corrente = ler_tempo()
        jogo.atualizarEstado(1)  # tempo_corrente - tempo_de_jogo)
        tempo_de_jogo += 1  # tempo_corrente
    
    jogo.terminarJogo()


if __name__ == '__main__':
    iniciar_jogo()


