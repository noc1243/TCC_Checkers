# Projeto Final - Diogo Nocera Magalhães

## Introdução e Objetivo do Projeto

Neste projeto tentamos ensinar uma rede neural a jogar Damas tão bem quanto ou melhor que um ser humano. O intuito final do projeto é conseguir esse feito sem que haja a necessidade de utilizar alguém com expertise em Damas para auxiliar no treinamento do computador. Ou seja, será feito um treinamento não supervisionado.       
Para tal fim, tentou-se reproduzir o paper:     
`K. Chellapilla and D.B. Fogel. Evolving an expert checkers playing program
without human expertise. IEEE Transactions on Evolutionary Computation,
5(4):422–428, 2001.`

## Metodologia
A solução utilizada para realizar esse treinamento de forma não supervisionada é usar um algoritmo genético que, através de várias gerações, selecionará uma rede neural para jogar Damas. Nessa seleção natural, 30 jogadores jogam entre si num campeonato. Nele cada vitória dá 1 ponto ao jogador. A cada derrota, ele perde 2 pontos. Cada empate dá 0 pontos. Ao final do campeonato, os 15 jogadores com maior pontuação são selecionados.          
Em seguida, esses 15 jogadores geram 15 filhos, um para cada jogador. Terminada esta etapa, a seleção natural começa novamente, com 15 novos jogadores sendo selecionados e assim repetindo o ciclo até que um bom jogador seja criado.         

![alt text](https://github.com/noc1243/TCC_Checkers/blob/master/imagens/CicloDeSelecao.png)

Para realizar tal objetivo, inicialmente, cria-se uma rede neural que classifique o quão bom um tabuleiro é para um jogador. Um array que representa esse tabuleiro é enviado como entrada para uma rede neural multicamadas 91x40x10x1 que dá como uma saída um número entre -1 e 1. Quanto maior o número, melhor a situação do tabuleiro é para o jogador. Quanto menor é o número, pior a situação. A decisão de qual a melhor jogada é feita através da pontuação dada para cada jogada possível a partir de um tabuleiro. São olhadas *n* jogadas à frente utilizando um algoritmo de MinMax Alpha Beta.       
Além disso, foram usados dois tipos de mutação na criação de cada filho:
1. Os pesos e biases são variados;
1. A representação da Dama no array é mudada.

Para avaliar os resultados do algoritmo genético, a cada 20 gerações, os jogadores selecionados jogam com os jogadores de 20 gerações atrás num campeonato e a pontuação de cada jogador no final é observada.

![alt text](https://github.com/noc1243/TCC_Checkers/blob/master/imagens/ValidacaoDoTreino.png)

Outro meio de avaliação usado foi realizadando partidas entre uma pessoa e o computador para verificar se as jogadas do computador, realmente, não estão sendo escolhidas ao acaso.

## Resultados até o momento   
1. Vislumbrando 2 jogadas à frente e treinando até a 100ª geração, observou-se que, até a 80ª geração, houve uma melhora significativa dos jogadores em relação aos anteriores. Após este ponto, os jogadores parecem não estar mais melhorando.     
Dentre as possíveis causas para este problema estão:
  * A pontuação de empate está fazendo com que os jogadores aprendam a **não perder** ao invés de ganhar. Isso pode estar causando um ciclo entre as gerações;
  * Olhar apenas 2 jogadas a frente pode estar limitando os jogadores graças a suas opções limitadas.

2. Ao realizar um jogo contra um desses jogadores selecionados na 80ª geração, observou-se que, o jogador selecionado fazia jogadas que:
  * Impediam que uma de suas peças fosse capturada facilmente;
  * Tentavam fazer damas;
  * Quando possível, faziam movimentos para capturar duas peças ao invés de uma;
  * Quando perdendo, faziam toda e qualquer jogada possível pra obter um empate;

## Próximos Objetivos
1. Já que vislumbrar 2 jogadas a frente não está trazendo melhores resultados, um treinamento que vislumbra 4 jogadas à frente está sendo realizado.
1. Terminado o objetivo anterior, caso ainda exista a tendência de empate nos jogadores, a função de fit será reavalida para punir jogadores que buscam muito o empate.

## Usando o projeto
Para que o projeto rode, no caso a branch `master`só se faz necessário rodar o código `treinamento.py` e que as pastas `modelos` e `pesosDamas` existam no diretório do projeto. Todos os modelos que aparecem no treinamento são salvos na pasta `modelos` e todos os pesos na pasta `pesosDamas`.    
Existem vários códigos de teste escritos que testam cada "módulo" do projeto caso haja interesse de testar alguma parte específica do código.   
Para jogar com um dos jogadores selecionados, basta rodar o código `partidaEntreHumanoEComputador.py`. Dentro dele é necessário que você aponte qual jogador deseja jogar com. O modelo desse jogador  deve se encontrar na pasta `melhores_modelos` e o peso deste jogador deve se encontrar na pasta `melhores_pesos`.   

**Importante**: Para rodar a versão desse código que se encontra na branch `Multi_Thread` não é possível usar interpretadores, como o **Spyder**. O Código precisa ser rodado via cli para funcionar.

Mais detalhes e exemplos de uso serão mostrados na <a href="https://github.com/noc1243/TCC_Checkers/wiki">Wiki</a> do projeto.
