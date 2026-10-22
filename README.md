<p align="center">
  <img src="./assets/tictactoe.jpg" alt="Capa do Repositório" width="100%">
</p>

# ❌⭕ Jogo da Velha com IA — Algoritmo Minimax

Implementei o algoritmo de busca adversarial **Minimax** no jogo da velha para a criação de um modelo de Inteligência Artificial que busca sempre a melhor jogada, maximizando o seu próprio potencial e minimizando o do adversário por meio de uma busca recursiva que prevê os movimentos futuros.

> 🎯 **O Desafio:** Te desafio a executar o arquivo no terminal e vencê-la! *(Aviso: Como o algoritmo calcula todas as possibilidades, o melhor resultado que você conseguirá alcançar é um empate).*

---

## 🧠 Como Funciona o Algoritmo Minimax?

O **Minimax** é um algoritmo clássico da teoria dos jogos e inteligência artificial utilizado em jogos de decisão e soma zero de dois jogadores (como Jogo da Velha, Xadrez e Damas).

1. **Árvore de Decisão Recursiva:** A IA simula todas as jogadas possíveis a partir do estado atual do tabuleiro, gerando uma árvore de estados até alcançar o fim da partida (vitória, derrota ou empate).
2. **Pontuação dos Estados (Função de Avaliação):**
   * **Vitória da IA:** Retorna pontuação positiva (`10 - profundidade`).
   * **Vitória do Jogador:** Retorna pontuação negativa (`profundidade - 10`).
   * **Empate:** Retorna `0`.
3. **Otimização por Profundidade:** A variável `depth` (profundidade) garante que a IA prefira caminhos onde ganha mais rápido ou onde adia o máximo possível a vitória do adversário.
4. **Decisão:** A IA escolhe a jogada que resulta no maior valor retornado pela busca recursiva (`max_eval`). Se houver mais de uma jogada com o mesmo valor máximo, a IA escolhe uma delas aleatoriamente para variar as partidas.

---

## 📁 Estrutura do Projeto

O código está organizado de forma modular nos seguintes arquivos:

* `main.py`: Ponto de entrada do jogo. Gerencia o loop principal, entradas do usuário e alternância de turnos.
* `ai.py`: Contém a lógica do algoritmo `minimax` e a função `best_move` para tomada de decisão da IA.
* `board.py`: Funções utilitárias para criação, exibição e verificação de condições de vitória/empate no tabuleiro.

---

## 💻 Como Executar

### Pré-requisitos
* **Python 3.x** instalado na sua máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Execute o jogo:**
   ```bash
   python main.py
   ```

3. **Como Jogar:**
   * O tabuleiro é representado por posições numeradas de **0 a 8**:
     ```text
      0 | 1 | 2 
     -----------
      3 | 4 | 5 
     -----------
      6 | 7 | 8 
     ```
   * Digite o número correspondente à posição desejada no terminal e pressione `Enter`.
   * Você joga como **X** e a IA joga como **O**.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3** (módulos padrão, sem necessidade de bibliotecas externas).
