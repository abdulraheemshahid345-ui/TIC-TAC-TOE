import random
from board import board

def ai_move():
    empty_box = []

    for i in range(9):
      if board[i] == " ":
        empty_box.append(i)

    index = random.choice(empty_box)
    board[index] = "O"
    print(f"🤖 AI ne box {index} choose kiya!")