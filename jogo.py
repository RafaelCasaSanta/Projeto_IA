import time
from regras.regras_skb import construir_jogo
from regras.personagens import Personagens
from agentes import construir_agente
from agentes.tipos import  tipos_agentes

def ler_tempo(em_turnos=False):
    """ Se o jogo for em turnos, retorna a passada de 1 rodada.
    
    Se não for em turno, é continuo ou estratégico, retorna tempo
    preciso (ns) do relógio.
    """
    return 1 if em_turnos else time.time()


def iniciar_jogo():
    ind = 0
    # Inicializar e configurar jogo
    jogo = construir_jogo()
    personagem_jogador = jogo.registrarAgentePersonagem(Personagens.JOGADOR_SOKOBAN)
    # Escolhe o jogador:
    personagem = input("Escolha um personagem (1 - Humano 2 - BFS  3 - Gulosa 4 - A*): ").strip()
    print(personagem)
    if personagem == '1':
      agente_jogador = construir_agente(tipos_agentes.PREPOSTO_HUMANO)
    elif personagem == '2':
      agente_jogador = construir_agente(tipos_agentes.AUTO_BFS)
    elif personagem == '3':
      agente_jogador = construir_agente(tipos_agentes.GULOSA)
    elif personagem == '4':
      agente_jogador = construir_agente(tipos_agentes.A_STAR)
 
    

    tempo_de_jogo = 0
    while not jogo.isFim():
        
        # Mostrar mundo ao jogador
        ambiente_perceptivel = jogo.gerarCampoVisao(personagem_jogador)
        agente_jogador.adquirirPercepcao(ambiente_perceptivel)

        # Decidir jogada e apresentar ao jogo
        if personagem == '1':
         acao = agente_jogador.escolherProximaAcao()
        else:
         acao = agente_jogador.escolherProximaAcao(ind)
        jogo.registrarProximaAcao(personagem_jogador, acao)
        ind = ind + 1

        # Atualizar jogo
        # tempo_corrente = ler_tempo()
        jogo.atualizarEstado(1)  # tempo_corrente - tempo_de_jogo)
        tempo_de_jogo += 1  # tempo_corrente
    
    jogo.terminarJogo()


if __name__ == '__main__':
    iniciar_jogo()