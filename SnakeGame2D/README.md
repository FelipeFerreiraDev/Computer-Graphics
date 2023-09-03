# Documentação do Jogo da Cobra

Este documento descreve o código JavaScript para um jogo da cobra implementado em HTML5 Canvas.

## Configuração Inicial

Antes de começar a jogar, é necessário definir a configuração inicial e carregar os elementos da página.

- `canvas`: Obtém o elemento `canvas` do documento e cria um contexto 2D para desenho.
- `score`, `highscore`, `finalScore`: Obtém elementos HTML para exibir a pontuação, a pontuação mais alta e a pontuação final.
- `menu`, `buttonPlay`, `buttonSpeed`, `buttonObject`, `buttonZerar`: Obtém elementos HTML para o menu, botão de jogar, botão de velocidade, botão de objeto e botão de zerar.

## Função `zerar()`

Essa função é responsável por redefinir a pontuação mais alta no jogo para zero quando o botão "Zerar" é clicado.

- `localStorage.setItem("snakeHighScore", 0)`: Define a pontuação mais alta no armazenamento local como zero.
- `highscore.innerText = getHighScore()`: Atualiza a exibição da pontuação mais alta na tela.

## Configuração de Áudio

- `audio`: Cria um elemento de áudio para reproduzir o som do jogo a partir de um arquivo de áudio.
- O som é reproduzido quando a cobra come uma comida.

## Variáveis e Constantes

- `size`: Define o tamanho dos blocos da cobra e dos objetos no jogo.
- `initialPosition`: Define a posição inicial da cabeça da cobra no jogo.
- `snake`: Uma lista que armazena as posições dos blocos da cobra.
- `objects`: Uma lista que armazena as posições dos objetos no jogo.
- `maxObjects`: Define o número máximo de objetos permitidos no jogo.
- `gameSpeed`: Define a velocidade inicial do jogo em milissegundos.

## Função `getHighScore()`

Esta função verifica e retorna a pontuação mais alta salva no armazenamento local. Se nenhuma pontuação for encontrada, ela retorna zero.

## Funções de Desenho

- `drawFood()`: Desenha a comida no canvas. Utiliza uma imagem SVG.
- `drawSnake()`: Desenha a cobra no canvas.
- `drawGrid()`: Desenha uma grade no canvas para melhor visualização.
- `drawObject()`: Desenha os objetos no canvas.
- `ctx.drawImage()`: Desenha a imagem SVG da comida no canvas.

## Função `moveSnake()`

Move a cobra com base na direção atual definida pelo jogador.

## Função `checkCollision()`

Verifica se a cobra colidiu com as paredes ou com ela mesma. Se a colisão ocorrer, o jogo termina.

## Função `chackEat()`

Verifica se a cobra comeu a comida. Se sim, incrementa a pontuação e gera uma nova posição para a comida.

## Função `gameOver()`

Encerra o jogo e exibe o menu de jogo com a pontuação final. Também verifica e atualiza a pontuação mais alta no armazenamento local.

## Eventos de Teclado

- `document.addEventListener("keydown")`: Captura os eventos de teclado para permitir que o jogador controle a direção da cobra usando as teclas de seta.

## Botões e Eventos de Clique

- `buttonPlay`: Inicia o jogo quando o botão "Jogar" é clicado.
- `buttonSpeed`: Alterna a velocidade do jogo entre fácil, médio, difícil e brutal quando o botão "Velocidade" é clicado.
- `buttonObject`: Adiciona objetos ao jogo quando o botão "Objeto" é clicado.
- `buttonZerar`: Zera a pontuação mais alta quando o botão "Zerar" é clicado.

## Execução do Loop do Jogo

- `gameLoop()`: Executa o loop principal do jogo. Limpa o canvas, desenha os elementos do jogo, verifica colisões e objetos, e define um novo timeout para continuar o loop.