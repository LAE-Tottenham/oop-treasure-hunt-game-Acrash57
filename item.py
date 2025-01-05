
class Item():
    def __init__(self, given_name, given_type):
        self.name = given_name
        self.type = given_type
    
class Weapon(Item):
    def __init__(self, given_name, given_type, given_weapon_type, given_damage):
        super().__init__(given_name, given_type)
        self.weapon_type = given_weapon_type
        self.damage = given_damage
    
    def use(self, player):
        player.current_weapon = self
        print(f"You equip the weapon {self.name}")
        print(f"Its damage is: {self.damage} per attack")
        print(f"Its type is {self.weapon_type}")
    

class Consumables(Item):
    def __init__(self, given_name, given_type, given_effect):
        super().__init__(given_name,given_type)
        self.effect = given_effect
    
    def use(self, player):
            if self.effect == "Energy_25":
                player.energy += 25
                print(f"You consume the {self.name} and gained 25 energy") 
            elif self.effect == "Heal_25":
                player.health += 25
                print(f"You consume the {self.name} and gained 25 health")


