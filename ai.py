import random

from board import check_winner, is_board_full, AI, PLAYER

def minimax(b, depth, is_maximizing):
    # Stop conditions
    if check_winner(b, AI): return 10 - depth
    if check_winner(b, PLAYER): return depth - 10
    if is_board_full(b): return 0

    positions = range(9)
    if is_maximizing:
        max_eval = -float('inf')
        for i in range(9):
            if b[i] == " ":
                b[i] = AI
                eval_score = minimax(b, depth + 1, False)
                b[i] = " "
                max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if b[i] == " ":
                b[i] = PLAYER
                eval_score = minimax(b, depth + 1, True)
                b[i] = " "
                min_eval = min(min_eval, eval_score)
        return min_eval

def best_move(b):
    best_score = -float('inf')
    best_moves = []
    for i in range(9):
        if b[i] == " ":
            b[i] = AI
            score = minimax(b, 0, False)
            b[i] = " "
            if score > best_score:
                best_score = score
                move = i
                best_moves = [i]
            elif score == best_score:
                best_moves.append(i)

    return random.choice(best_moves)