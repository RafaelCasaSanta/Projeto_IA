## Projeto_IA
## Instruções 
* Projeto em duplas. 
* Obrigatório uso de uma plataforma de projetos e controle de versão pública (Github, GitLab, Bitbucket, etc).  

## Etapas de execução:    
### 0. Escolha um problema que exija planejamento para solução. O problema precisa ser completamente observável, discreto, determinístico, sequencial e de agente único. Como se trata de problemas simples e específicos, tipicamente, jogos são a melhor opção.   
### 1. Com base nos elementos de jogo (peças, jogador, inimigos, paredes, alvos, destrutíveis, etc): 
* Crie uma linguagem para representação de quaisquer estados válidos para seu jogo. 
* Exemplifique o emprego da linguagem com três cadeias válidas: um estado inicial do jogo, um estado intermediário qualquer, um possível estado objetivo.
* Esboce uma representação visual (tela de jogo) para cada um desses estados. 
* Registre toda essa produção na documentação wiki do jogo. 

### 2. Ilustre um subconjunto do espaço de estados de seu jogo. Para tal, siga o roteiro 
* Crie outra linguagem, agora para representar ações possíveis para o jogador. Explique em prosa o que representa cada ação, e indique as restrições para aplicação de cada uma.
* Utilizando grafos, represente o espaço de estados de seu jogo a partir de um estado inicial, indique todas as ações válidas para este primeiro estado, e também para seus filho, mas se restrinja a no máximo 10 vértices para este grafo. 
* Repita a atividade, porém agora partindo de um estado objetivo qualquer, caminhando no sentido inverso das ações.
* Registre toda essa produção na wiki de seu jogo. 


### 3. Implemente o jogo partindo do esqueleto-de-código para jogos com agentes inteligentes, disponibilizado nessa disciplina (ver link anexo). 


### 4. Com o jogo implementado e jogável, crie novas implementações de agentes, agora automatizados. Crie uma implementação para cada algoritmo, de busca cega, a seguir: 
* BFS; * DFS; 


### 5. Implemente um seletor de jogador no início de seu jogo, que permite escolher qual dos agentes jogará a partida a começar.  

** Gravar um video de até 3 minutos, apresentando o seu projeto, mostrando o sistema funcionando, e mostrando as principais funções do código-fonte.
