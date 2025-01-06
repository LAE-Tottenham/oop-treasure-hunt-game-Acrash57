import random
from tile import player_icon
from item import Consumables, Weapon
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
    def __init__(self, given_name, given_weapon, given_health = 100, given_strength = 1, given_level = 0, given_energy = 100, given_essence = 0):
        super().__init__(given_name, given_health)
        self.level = given_level
        self.essence = given_essence
        self.strength = given_strength
        self.energy = given_energy
        self.max_energy = given_energy
        self.inventory_max_weight = 25
        self.inventory = []
        self.pos = [0,0]
        self.money = 75
        self.marker = player_icon
        self.weapon = given_weapon
    
    def level_up(self):
        print(f"{self.name} has leveled up, you strenght, max health and energy have increased!")
        self.level += 1
        self.strength += 1
        self.max_health += 25
        self.max_energy += 25

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
    
    def remove_item(self, item_instance):
        self.inventory.remove(item_instance)
    
    def add_item(self, item_instance):
        if self.calculate_inventory_size() < self.inventory_max_weight:
            self.inventory.append(item_instance)
        else:
            print("Your inventory is full")

    def use_item(self, item_instance):
        if self.calculate_inventory_size() == 0:
            print("You do not have any items to use")
            return
        
        if item_instance in self.inventory: 
            if isinstance(item_instance, Weapon):
                item_instance.use(self)  
                self.inventory.remove(item_instance)
            elif isinstance(item_instance, Consumables):
                item_instance.use(self)  
                self.inventory.remove(item_instance)
        else:
            print("You do not have that item")
    
    def attack(self, target):
        if self.energy > 30:
            self.energy = max(self.energy, 0)
            self.energy -= 3
            total_dmg = self.weapon.damage + self.strength
            target.health -= total_dmg 
            target.health = max(target.health, 0)
            print(f"{self.name} has done {total_dmg} damage with the {self.weapon.name}!")
            print(f"{target.name}'s health is now {target.health}")
        elif self.energy < 30:
            self.energy = max(self.energy, 0)
            self.energy -= 4
            print(f"Your energy {self.energy} and low affecting your damage output!")
            total_dmg = self.weapon.damage - self.strength
            target.health -= total_dmg
            target.health = max(target.health, 0)
            print(f"{self.name} has done {total_dmg} damage with the {self.weapon.name}!")
            print(f"{target.name}'s health is now {target.health}")


class Enemy(Entity):
    def __init__(self, given_name, given_damage, given_health, given_boss_status = False):
        super().__init__(given_name, given_health)
        self.damage = given_damage
        self.pos = [random.randint(0, 34), random.randint(0, 19)]
        self.boss_status = given_boss_status
    




