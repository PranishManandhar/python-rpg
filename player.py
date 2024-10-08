import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.coins = 200
        self.energy = 100
        self.food = 10
        self.distance = 0

    def status(self):
        print(f"\nyour name is {self.name}")
        print(f"your hp is {self.hp}")
        print(f"you have {self.coins} coins")
        print(f"you have {self.energy} energy left")
        print(f"your food amount is {self.food}")
        print(f"you have covered {self.distance} metres in distance from the starting point")

    def Travels(self):
        travelled = random.randint(10,22)
        self.food -= random.randint(2,5)
        self.energy -= random.randint(10,20)
        self.distance += travelled
        self.check_health()
        print(f"you have {100-self.distance} meters left to travell")

    def check_health(self):
        if self.food <= 0:
            self.food = 0
            hp_loss = random.randint(5,10)
            self.hp -= hp_loss
            print(f"your food is now empty, your health has been reduced by {hp_loss}")
        
        if self.energy <= 0:
            self.energy = 0
            self.hp = 0
            print(f"you were so tired that you fell on the road. Another Traveller found you dead and buried you at a nearby cemetery")