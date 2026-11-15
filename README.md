Connect Four - INE5201 (UFSC)

Implementação do jogo Connect Four no Python utilizando matrizes 2D e interface gráfica com FreeSimpleGUI

Como Executar
1. Certifique-se de ter o Python instalado.
2. Instale a biblioteca gráfica necessária executando no terminal:
   `pip install FreeSimpleGUI`
3. Execute o jogo:
   `python connect_four.py`

Funcionalidades e Regras
- Tabuleiro interativo de 7 colunas por 6 linhas.
- Simulação de gravidade (as fichas caem automaticamente para a posição mais baixa disponível na coluna).
- Validação de colunas cheias e alternância automática de turnos entre o Jogador 1 (Vermelho) e o Jogador 2 (Amarelo).
- Detecção automática de vitória (4 fichas alinhadas na horizontal, vertical ou diagonal) e de empate (tabuleiro cheio).
- Botão "Reiniciar Jogo" integrado.

Uso do GitHub Copilot
O GitHub Copilot foi utilizado como assistente de programação ao longo do desenvolvimento do projeto para acelerar a escrita de código, sugerir estruturas lógicas e encontrar erros de interface gráfica:

- Estruturação e Lógica de Matriz: Auxiliou na criação da matriz 2D `6x7` e na implementação da função de gravidade , percorrendo as linhas de baixo para cima para encontrar a primeira posição vazia.
- Verificação de Vitória: Sugeriu a estrutura de laços para validar as três condições de alinhamento (horizontal, vertical e diagonal) evitando erros de índice fora dos limites.
- Interface Gráfica (`FreeSimpleGUI`): Ajudou a configurar os elementos do `Graph`, calcular as coordenadas matemáticas dos círculos de cada ficha e corrigir parâmetros da função `draw_oval` para renderizar corretamente as cores dos jogadores.

- Exemplos de Prompts Utilizados:
  - "Crie uma função em Python que verifica vitória nas diagonais de uma matriz 6x7 no Connect Four"
  - "Como mapear cliques no elemento Graph do FreeSimpleGUI para identificar a coluna clicada?"
  - "Explique e corrija o erro de parâmetros na função draw_oval do FreeSimpleGUI"