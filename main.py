import random

MONSTER = "£"
POTION  = "&"
WEAPON  = "/"

MAX_HEALTH = 20

class Dungeon:
    def __fill_deck(self):
        for i in range(1, 14):
            self.deck += [(i, MONSTER)]*2 

        for i in range(2, 11): 
            self.deck += [(i, POTION), (i, WEAPON)]

        random.shuffle(self.deck)

    def __init__(self):
        health = MAX_HEALTH
        weapon = None
        weapon_bound = 14 # the weapon can be used on anything

        room = []
        deck = []
        self.__fill_deck() 
    
    def drink(self, potion_val: int):
        if (potion_val, POTION) in self.room:
            if self.health == 20:
                print("You drink the potion to no effect. You are at full health.")
            else:
                print(f"Drinking the potion restores your health.")
            self.room = [item for item in self.room if item[1] != POTION] 
        else:
            print("No such potion in this room.")

    def fight(self, monster_val: int, barehanded: bool):
        if (monster_val, MONSTER) not in self.room:
            print("No such monster in this room.")
        elif barehanded:
            health -= monster_val
            self.room.remove((monster_val, MONSTER))
        elif self.weapon_bound > monster_val:
            if self.weapon < monster_val:
                health -= monster_val - self.weapon
                print("You're weapon stops some of the damage.")
                self.weapon_bound
        else:
            print("Your weapon won't work on this monster.")



            





