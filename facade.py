board = ["" for _ in range(9)]

AI = "O"
PLAYER = "X"

def print_board(b):
    print(f" {b[0]} | {b[1]} | {b[2]}")
    print("---------")
    print(f" {b[3]} | {b[4]} | {b[5]}")
    print("---------")
    print(f" {b[6]} | {b[7]} | {b[8]}")

def check_winner(b, player):
    winner_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in winner_conditions:
        if all(b[i] == player for i in condition):
            return True
        return False