from player import Player
from events import events


def game():
    print("Welcome to the game!")
    input("press any key to continue")
    
    print("""
    It was a morning like usual when you got a letter from your old neighbour. He told you that your father had passed away
    and had left you a big fortune and his farmland. you were called to inherit it and run his farm and business in his stead 
    from now on. with grief about your father's passing you started your journey to your home
    """)

    input("press any key to continue")

    name = input("Enter your name: ")

    player = Player(name)


    while player.hp>0:
        player.status()

        action = input("\nWhat would you like to do?")
        print("\n")
        if action == "travel":
            player.Travels()
            events(player)
        elif action == "status":
            player.status()
        elif action == "quit":
            print("Thank you for playing")
            break
        else:
            print("Invalid command, please try again")
        

if __name__ == "__main__":
    game()