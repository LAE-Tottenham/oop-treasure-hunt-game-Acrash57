from tile import player_icon
from place import Map

class Entity():
    def __init__(self, given_name, given_health):
        self.name = given_name
        self.health = given_health
        self.max_health = given_health
        
    
    def attack(self, target):
        target.health -= self.damage
        target.health = max(target.health, 0)
        print(f"{self.name} has done {self.damage} damage!")
        print(f"{target.name}'s health is now {target.health}")
    

class Player(Entity):
    def __init__(self, given_name, given_health = 100, given_strenght = 1, given_level = 0):
        super().__init__(given_name, given_health)
        self.level = given_level
        self.strenght = given_strenght
        self.inventory_max_weight = 25
        self.inventory = []
        self.pos = [0,0]
        self.marker = player_icon
        

    def move(self, x, y):
        self.pos[0] += x 
        self.pos[1] += y
    
    def calculate_possible_moves(self, width = 25, height = 35):
        return {
            "up": self.pos[1] > 0,
            "down": self.pos[1] < height,
            "left": self.pos[0] > 0, 
            "right": self.pos[0] < width
        }
    
    def calculate_inventory_size(self):
        x = len(self.inventory)
        return x 
    
    def add_item(self, item_instance):
        if self.calculate_inventory_size() < self.inventory_max_weight:
            self.inventory.append(item_instance)
        else:
            print("Your inventory is full")

    def use_item(self, item_instance):
        item_loop = True
        while item_loop:
            if item_instance in self.inventory: 
                if item_instance == "Food":
                    self.energy += 50
                    self.inventory.remove("Food")
                    item_loop = False
                elif item_instance == "Health Potion":
                    self.health += 25
                    self.inventory.remove("Health Potion")
                    item_loop = False
            elif self.calculate_inventory_size() == 0:
                print("You do not have any items to use")
                item_loop = False    
            else:
                print("You do not have that item")

class Enemy(Entity):
    def __init__(self, given_name, given_damage, given_health):
        super().__init__(given_name, given_health)
        self.damage = given_damage
    




