# Projeto Final - Diogo Nocera Magalhães

## Objetivo

O objetivo inicial deste projeto final é reproduzir o paper     
`K. Chellapilla and D.B. Fogel. Evolving an expert checkers playing program
without human expertise. IEEE Transactions on Evolutionary Computation,
5(4):422–428, 2001.`

## Explicando o problema

O problema designado é fazer com que uma máquina consiga jogar damas de forma a jogar tão bem quanto um ser humano ou até melhor.    


## Solução utilizada
<p>Uma possível solução para esse problema seria criar uma rede neural multicamadas que avaliasse o estado  de um tabuleiro após uma jogada e, após analisar todas as possíveis jogadas, decidir pela melhor. A princípio, pensa-se no uso de back-propagation para treinar essa rede neural, contudo, surge um problema: como decidir qual avaliação um tabuleiro deve ter para que seja feito o back-propagation? Tal solução envolveria o uso de uma quantidade de dados absurda e a criação de algumas regras para a avaliação de um tabuleiro que necessitaria de um especialista em damas.</p>
<p>Para solucionar este problema, foi usado um algoritmo genético baseado na competição entre seres da mesma espécie. Nessa solução, são criadas várias redes neurais com os pesos e biases iniciados aleatoriamente e estas são colocadas para jogar entre si a cada geração. Os melhores jogadores de uma geração são selecionados e, através de mutação, geram filhos que jogarão entre si e com os pais na próxima geração.</p>
<p>Tal solução permite que essas redes neurais fiquem melhores no jogo de damas a cada geração que passa de forma não supervisionada.</p>

## Detalhando a solução
<p>Seguindo o paper citado acima, cada geração roda um "campeonato" em que 30 redes neurais, <b>Jogadores</b> , jogam 10 partidas com jogadores adversários selecionados de forma aleatória. Cada vitória dá ao jogador 1 ponto, cada derrota -2 pontos e cada empate 0 pontos. Realizados todos os jogos, a pontuação total dos jogadores é computada e os 15 melhores jogadores são selecionados para terem 15 filhos que competirão também na próxima geração.</p>


<img src="https://github.com/noc1243/TCC_Checkers/blob/master/imagens/CicloDeSelecao.png"</img>

<p>A rede neural utilizada foi a mesma mostrada no paper: 91x40x10x1. Esta rede foi decidia através da reprodução do mesmo problema em menor escala: ensinando um computador a jogar o Jogo da Velha.</p>
<p>Na avaliação de qual jogada seria a melhor para ser realizada pelo <b>Jogador</b>, são olhados alguns movimentos a frente, <b>ply</b>. O algoritmo usado nessa decisão é um de MinMax Alpha Beta.</p>

## Avaliação dos resultados até o momento
Para avaliar os resultados, no momento atual, a cada 20 gerações, os jogadores selecionados jogam com os jogadores originais e
a pontuação de cada jogador no final do campeonato é avaliada. Caso os jogadores atuais tenham uma pontuação maior do que a dos originais, isso significa que o algoritmo genético está funcionando corretamente. Feito isso, em 20 gerações futuras, os novos jogadores selecionados jogarão com os selecionados na 20ª geração e assim por diante.    
Fora isso, estão sendo realizadas partidas entre humanos e os computadores selecionados para verificar se as jogadas do computador realmente fazem sentido.

### Resultados
Usando um **ply** de 2 e treinando até a 100ª geração, observou-se que, até a 80ª geração, houve uma melhora significativa dos jogadores em relação aos anteriores. Após este ponto, os jogadores parecem não estar mais melhorando.     
Dentre as suposições da causa para este problema estão:
1. O fit de empate está fazendo com que os **Jogadores** aprendam mais a **não perder** do que ganhar. Isso pode estar causando um ciclo entre as gerações;
1. O uso de um **ply** muito pequeno, de 2, pode acabar causando um threshold no que os jogadores podem aprender, visto que nenhum jogador bom de fato consegue jogar bem sem olhar diversas jogadas a frente.

Ao avaliar em um jogo contra um desses jogadores selecionados na 80ª geração, observou-se que, por mais que ele não seja um grande jogador, que joga a nível de especialista, o mesmo faz jogadas que fazem sentido, como:
1. Impedir que uma de suas peças seja comida "de graça";
1. Tentar fazer damas;
1. Quando possível, fazer movimentos para "comer" duas peças ao invés de uma;
1. Quando perdendo, fazer toda e qualquer jogada possível pra obter um empate;

## Próximos Objetivos
1. Como o uso de um **ply** de 2 parece não estar dando resultados melhores no treinamento, agora um treinamento que faz o uso de um **ply** de 4 está sendo realizado.
1. Caso ainda exista a tendência de empate ao invés da busca pela vitória pelos Jogadores, a função de fit será reavalida para punir jogadores que buscam muito o empate ao invés da vitória.

## Usando o projeto
Para que o projeto rode, no caso a branch `master`só se faz necessário rodar o código `treinamento.py` e que as pastas `modelos` e `pesosDamas` existam no diretório do projeto. Todos os modelos que aparecem no treinamento são salvos na pasta `modelos` e todos os pesos na pasta `pesosDamas`.    
Existem vários códigos de teste escritos que testam cada "módulo" do projeto caso haja interesse de testar alguma parte específica do código.   
Para jogar com um dos jogadores selecionados, basta rodar o código `partidaEntreHumanoEComputador.py`. Dentro dele é necessário que você aponte qual jogador deseja jogar com. O modelo desse jogador  deve se encontrar na pasta `melhores_modelos` e o peso deste jogador deve se encontrar na pasta `melhores_pesos`.   

**Importante**: Para rodar a versão desse código que se encontra na branch `Multi_Thread` não é possível usar interpretadores, como o **Spyder**. O Código precisa ser rodado via cli para funcionar.

Mais detalhes e exemplos de uso serão mostrados na <a href="https://github.com/noc1243/TCC_Checkers/wiki">Wiki</a> do projeto.
