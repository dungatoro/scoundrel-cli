import random

MONSTER = "):"
POTION  = "<3"
WEAPON  = "/@"

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
        equipped_weapon = None
        weapon_bound = 13 # the weapon can be used on anything

        room = []
        deck = []
        self.__fill_deck() 
    
    def drink(self, potion_val: int):
        if (potion_val, POTION) in self.room:
            print(f"Drinking the potion brings your health to {self.health}.")
            self.room = [item for item in self.room if item[1] != POTION] 
        else:
            print("Item not found in this room.")

    def fight(self, monster_val: int, barehanded: bool):
        if (monster_val, MONSTER) not in self.room:
            print("No such monster in the room.")
        elif barehanded:
            health -= monster_val
        elif self.weapon_bound < monster_val:
            print("Your weapon won't work on this monster.")



            





