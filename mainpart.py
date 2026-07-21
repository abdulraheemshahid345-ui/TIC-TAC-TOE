
from board import display_board, reset_board
from player import player_move
from winner import check_winner, check_draw
from main import main_menu, show_game_mode, show_rules
from ai import ai_move


while True:

    choice = main_menu()

    if choice == 1:

        mode = show_game_mode()

        if mode == 1:
            player_x_name = input("Enter Player X name: ")
            player_o_name = input("Enter Player O name: ")

            x_score = 0
            o_score = 0

            while True:

                current_player = "X"
                reset_board()
                display_board()

                while True:

                    if current_player == "X":
                        print(f"\nTurn: {player_x_name} (X)")
                    else:
                        print(f"\nTurn: {player_o_name} (O)")

                    player_move(current_player)
                    display_board()

                    winner = check_winner()
                    if winner :
                        if winner == "X":
                            x_score+= 1
                            print(f"🏆 {player_x_name} Won the Match!")
                        else:
                            o_score += 1
                            print(f"🏆 {player_o_name} Won the Match!")    
                        break

                    if check_draw():
                        print("🤝 Match Draw!")
                        break

                    if current_player == "X":
                        current_player = "O"
                    else:
                        current_player = "X"

                print("\n===== SCOREBOARD =====")
                print(f"{player_x_name} (X): {x_score}")
                print(f"{player_o_name} (O): {o_score}")
                print("======================")

                again = input("\nDo you want to play again? (y/n): ").lower()

                if again == "y":
                    continue
                else:
                    break

        elif mode == 2:
            player_x_name = input("Enter Player_X name: ")
            x_score = 0        
            ai_score = 0 
            
    
            while True:                        
                current_player = "X"
                reset_board()
                display_board()
                
                while True:                   
                    if current_player == "X":
                        print(f"\nTurn: {player_x_name} (X)")
                        player_move(current_player)
                    else:
                        print("\n🤖 AI thinking...")
                        ai_move()
                    
                    display_board()
                    
                    winner = check_winner()
                    if winner:
                        if winner == "X":
                            x_score += 1
                            print(f"🎉 {player_x_name} Won!")
                        else:
                            ai_score += 1  
                            print("🤖 AI Won!")
                        break
                    
                    if check_draw():
                        print("🤝 Draw!")
                        break
                    
                    if current_player == "X":
                        current_player = "O"
                    else:
                        current_player = "X"

                print("\n===== SCOREBOARD =====")
                print(f"{player_x_name} (X): {x_score}")
                print(f"🤖 AI (O): {ai_score}")
                print("=====================")
                
                again = input("\nPlay Again? (y/n): ").lower()
                if again == "y":
                    continue
                else:
                    break

    elif choice == 2:
        show_rules()

    elif choice == 3:
        print("Thanks for Playing! 👋")
        break