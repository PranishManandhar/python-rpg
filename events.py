import random

def events(player):
    events = random.choice(["storm","bandits","dropped Resources","nothing"])
    nothingScene = ["you heard the wind flowing by as you thought about the way you still have to go",
                    "you found the day to be very calm and thought about the journey ahead",
                    "the empty road made you think that you might just have taken the wrong day to travel",
                    "you almost fell asleep while riding your carriage you should be careful"]

    if events == "storm":
        player.hp -= 10
        print("you lost some hp due to a storm that was heading towards your way")

    if events == "bandits":
        hploss = random.randint(0,90)
        foodloss = random.randint(3,10)

        player.hp -= hploss
        player.food -= foodloss
        print(f"you were attacked by bandits and lost {player.food} food and {player.coins} coins")

    if events == "dropped Resources":
        coinloss = random.randint(10,30)
        foodloss = random.randint(3,10)

        player.coins -= coinloss
        player.food -= foodloss
        print(f"you dropped some resoruces and lost {player.food} food and {player.coins} coins")

    if events == "nothing":
        print(nothingScene[random.randint(0,3)])