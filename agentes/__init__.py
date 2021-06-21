from agentes.humano import AgentePrepostoESHumano
from agentes.buscadores.auto_bfs import  AgenteAutomaticoBfs
from agentes.buscadores.busca_a_star import AgenteAStar
from agentes.buscadores.busca_gulosa  import AgenteBuscaGulosa
from agentes.tipos import *

def construir_agente(tipo_agente: tipos_agentes):
    """ Método factory para uma instância Agente arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """
    print(tipo_agente)
    if tipo_agente == tipos_agentes.AUTO_BFS:
      Agente = AgenteAutomaticoBfs()
    elif tipo_agente == tipos_agentes.GULOSA:
      Agente = AgenteBuscaGulosa()
    elif tipo_agente == tipos_agentes.A_STAR:
      Agente = AgenteAStar()
    else:
      Agente = AgentePrepostoESHumano()
    print(Agente)  
    return Agente
