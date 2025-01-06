
class Item():
    def __init__(self, given_name, given_type, given_value):
        self.name = given_name
        self.type = given_type
        self.value = given_value

class Weapon(Item):
    def __init__(self, given_name, given_type, given_weapon_type, given_damage, given_value):
        super().__init__(given_name, given_type, given_value)
        self.weapon_type = given_weapon_type
        self.damage = given_damage
    
    def use(self, player):
        player.current_weapon = self
        print(f"You equip the weapon {self.name}")
        print(f"Its damage is: {self.damage} per attack")
        print(f"Its type is {self.weapon_type}")
    

class Consumables(Item):
    def __init__(self, given_name, given_type, given_effect, given_value):
        super().__init__(given_name,given_type, given_value)
        self.effect = given_effect
    
    def use(self, player):
            if self.effect == "Ener_25":
                player.energy += 25
                print(f"You consume the {self.name} and gained 25 energy")
            if self.effect == "Ener_50":
                player.energy += 50
                print(f"You consume the {self.name} and gained 50 energy")
            if self.effect == "Ener_100":
                player.energy += 100
                print(f"You consume the {self.name} and gained 100 energy")
            elif self.effect == "Heal_25":
                player.health += 25
                print(f"You consume the {self.name} and gained 25 health")
            elif self.effect == "Heal_50":
                player.health += 50
                print(f"You consume the {self.name} and gained 50 health")
            elif self.effect == "Heal_100":
                player.health += 100
                print(f"You consume the {self.name} and gained 100 health")
                
            if player.max_health < player.health:
                player.health = player.max_health
            if player.max_energy < player.energy:
                player.energy = player.max_energy


