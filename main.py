from board import create_board, print_board, check_winner, is_board_full, PLAYER, AI
from ai import best_move

def play_game():
    board = create_board()
    current_player = PLAYER
    print("Jogo da Velha - Você é X e a IA é O.")
    print_board(board)

    while True:
        if current_player == PLAYER:
            try:
                move = int(input("Escolha sua posição (0-8): "))
                if not 0 <= move <= 8:
                    print("A posição precisa ser um número entre 0 e 8. Tente novamente!")
                elif board[move] == " ":
                    board[move] = PLAYER
                    current_player = AI
                else:
                    print("Posição ocupada! Tente novamente.")
                    continue
            except (ValueError, IndexError):
                print("Entrada inválida! Digite um número de 0 a 8")
                continue
        else:
            print("A IA está pensando...")
            move = best_move(board)
            board[move] = AI
            current_player = PLAYER

        print_board(board)

        if check_winner(board, AI):
            print("A IA vence! Mais sorte da próxima vez")
            break
        elif check_winner(board, PLAYER):
            print("Parabéns, você venceu!!")
            break
        elif is_board_full(board):
            print("Empate!")
            break

if __name__ == "__main__":
    play_game()