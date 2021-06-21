from agentes.buscadores.heuristicas import busca_heuristica
from percepcoes import PercepcoesJogador
from acoes import AcaoJogador, DirecaoMoverJogador

from agentes.abstrato import AgenteAbstrato

# Implementar agente de busca gulosa com retrocesso

class AgenteBuscaGulosa(AgenteAbstrato):
    def __init__(self) -> None:
        super().__init__()


    def adquirirPercepcao(self, percepcao_mundo: PercepcoesJogador):
        """ Inspeciona a disposicao dos elementos no objeto de visao."""
        AgenteBuscaGulosa.desenhar_tabuleiro(percepcao_mundo)
            

    def escolherProximaAcao( self,ind:int):

      if not self.solucao:
          no_solucao = fila_de_prioridades(self.problema)
          self.solucao = no_solucao.caminho_acoes
          "chamar a busca e o proxima ação estaria correto no gulosa ?"
          (busca_heuristica.escolherProximaAcao)
          print(len(self.solucao), self.solucao)
          if not self.solucao:
              raise Exception("Agente Guloso não encontrou solução.")

          acao = self.solucao.pop(0)
          print(f"Próxima ação é {acao}.")
          time.sleep(2)

          direcoes= AgenteBuscaGulosa.traduzir_acao_jogo(acao)

      if  self.solucao:
            acao = self.solucao[ind]
            direcoes=AgenteBuscaGulosa.traduzir_acao_jogo(acao)
            
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

"tentei realizar a implementação do gulosa, mas n to conseguindo sair do 0 "

""""
mov = [1]
movif = [2, 3, 4, 5]

comeco = []
final = []


def seletor_atv_recursiva (c, f, p, a)

" c = lista de começos"
" f = lista de finais"
" p = posição atual "
" a = total de açoes possiveis"

d = p + 1
while d < a and c[d] < f[p] 

d = d + 1

if d < a:
        print("Adding activity " + str(d) + " that finishes at "
              + str(f[d]))
        return [d] + seletor_atv_recursiva(c, f, p, a)
    else:
        return []

        def seletor_atv_gulosa(c, f):
   
    assert(len(c) == len(f))  
    a = len(c)  # could be len f as well!
    b = []
    p = 0
    for d in range(1, p):
        if c[d] >= f[p]:
            b.append(d)
            p = d
    return b"""""