from board import board

def check_winner():
    win_combinations= [ 
        [0, 1, 2] , [3, 4, 5] , [6, 7, 8],
        [0, 3, 6] , [1, 4, 7] , [2, 5, 8],
        [0, 4, 8] , [2, 4, 6]]
    
    for combo in win_combinations:
        a, b, c = combo

        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
        
    return None

def check_draw():
    if " " not in board:
        return True
    return False