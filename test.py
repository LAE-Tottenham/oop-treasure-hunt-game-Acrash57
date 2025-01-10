import random
import copy

class Item():
    def __init__(self, given_name):
        self.name = given_name
        self.pos = [random.randint(2, 34), random.randint(1, 19)]

class Game():
    def __init__(self): 
        self.map_items = None
        self.map_items = [Weapon1, Weapon2, Weapon3]

    def add_items(self, maps):
        maps.map_items = self.map_items

class Map(): 
    def __init__(self):
        self.map_item = None
        self.final_map_items = None
    
    def add_items(self): 
        item_weights = [50, 50, 30]
        x  = random.choices(self.map_items, weights = item_weights, k = 3)
        for y in x:
            print(y.pos)
        for y in x:
            print(y.pos)
        return copy.deepcopy(x)  


Weapon1 = Item("test1")
Weapon2 = Item("test2")
Weapon3 = Item("test3")
Game1 = Game() 
Map1 = Map() 

#Weapon1.ya()
Game1.add_items(Map1)
Map1.add_items() 





