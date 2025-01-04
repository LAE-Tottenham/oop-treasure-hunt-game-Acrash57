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
    def __init__(self, given_name, given_health = 100, given_strenght = 2, given_level = 0):
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
        return len(self.inventory)

    def add_item(self, item_instance):
        if self.calculate_inventory_size() > self.inventory_max_weight:
            self.inventory.append(item_instance)
        else:
            print("Your inventory is full...")

    def use_item(self, item_instance):
        if item_instance.type == "food":
            self.energy += 50
        elif item_instance.type == "medicine":
            self.health += 5

class Enemy(Entity):
    def __init__(self, given_name, given_damage, given_health):
        super().__init__(given_name, given_health)
        self.damage = given_damage
    




