board=[" ", " ", " ",
       " ", " ", " ",
       " ", " ", " "]

def display_board():
    print("\n")
    print("   1   2   3")
    print(f"1  {board[0]} | {board[1]} | {board[2]}")  
    print("  ---+---+---")
    print(f"2  {board[3]} | {board[4]} | {board[5]}") 
    print("  ---+---+---")
    print(f"3  {board[6]} | {board[7]} | {board[8]}")  

def reset_board():
    for i in  range(9):
        board[i] = " "