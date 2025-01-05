class Item():
    def __init__(self, given_name, given_type):
        self.name = given_name
        self.type = given_type
    
class Weapon(Item):
    def __init__(self, given_name, given_type, given_weapon_type, given_damage):
        super().__init__(given_name, given_type)
        self.weapon_type = given_weapon_type
        self.damage = given_damage
    
class Consumables(Item):
    def __init__(self, given_name, given_type, given_effect):
        super().__init__(given_name,given_type)
        self.effect = given_effect



