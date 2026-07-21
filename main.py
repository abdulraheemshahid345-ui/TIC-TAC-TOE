def main_menu():

    while True:
        print("\n" + "="*30)
        print("          TIC TAC TOE")
        print("="*30)
        print("1.  Start Game")
        print("2.  Rules")
        print("3.  Exit")
        print("="*30)

        try:
            choice = int(input("Choose: "))  
            
            if choice in [1, 2, 3]:           
                return choice               
            else:
                print("❌ Only choose 1, 2 and 3")  
                
        except ValueError:
            print("❌ Only choose Number!")     


def show_game_mode():

    while True:
        print("\n" + "="*30)
        print("       SELECT MODE")
        print("="*30)
        print("1.  Player VS Player")
        print("2.  Player VS AI")
        print("="*30)

        try:
            mode = int(input("Choose: "))
            
            if mode in [1, 2]:
                return mode
            else:
                print("❌ Sirf 1 ya 2!")
                
        except ValueError:
            print("❌ Sirf Number Likho!")
            

def show_rules():
    print("\n" + "="*30)
    print("          RULES")
    print("="*30)
    print("1. Board 3x3 hota hai")
    print("2. X hamesha pehle chalega")
    print("3. Row/Column/Diagonal mein")
    print("   If X or O is same in Row , Column and Diagonal = Win 🎉")
    print("4. If board is full without Win = Draw 🤝")
    print("="*30)