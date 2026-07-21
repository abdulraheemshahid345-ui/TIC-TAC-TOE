from board import board
def player_move(current_player):   
    while True:
        row= int(input("Enter Row(1-3):"))
        column= int(input("Enter Column(1-3):"))

        if row < 1 or row > 3 or column < 1 or column > 3:
            print(" Invalid Input! Row and column will be 1, 2 and ")
            continue

        index= (row - 1)* 3 + (column - 1)

        if board[index] != " ":
            print("Position is Occupied")
            continue

        
        board[index] = current_player 
        break