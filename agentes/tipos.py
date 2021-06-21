from enum import Enum

class tipos_agentes(Enum):
  PREPOSTO_HUMANO = 'Preposto humano'
  AUTO_BFS = 'Automático BFS'
  GULOSA = 'Busca Gulosa'
  A_STAR = "Busca A*"    
    # adicionar outros tipos de agentes de acordo com
    # o necessário