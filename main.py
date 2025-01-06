from place import Map
from entity import Player, Enemy
from item import Weapon, Consumables
from pyfiglet import Figlet
from termcolor import colored
import os
import time

class Game():
    def __init__(self):
        self.current_place = None
        self.player = None
        self.sentinel = None
        self.rat = None
        self.globin = None
        self.slime = None
        self.wolf = None
        self.health_potion = None
        self.energy_bar = None
        self.katana = None  
        self.scythe = None  
        self.short_bow = None  
        self.crossbow = None  
        self.long_bow = None  
        self.long_sword = None  
        self.throwing_knife = None  
        self.staff = None  
        self.magic_wand = None  
        self.crowdbreaker = None
        self.ethereal_reaper = None
        self.pheonix_bow = None
        self.staff_of_dominion = None
        self.large_health_potion = None  
        self.energy_drink = None  
        self.superior_health_potion = None  
        self.energy_pack = None
        self.shop_items = [self.health_potion, self.energy_bar, self.katana, self.scythe, self.short_bow, self.crossbow, self.long_bow, self.long_sword, self.throwing_knife, self.staff, self.magic_wand, self.crowdbreaker, self.ethereal_reaper, self.pheonix_bow, self.staff_of_dominion, self.large_health_potion, self.energy_drink, self.superior_health_potion, self.energy_pack]
        self.map_1 = None

    def setup(self):
        map_1 = Map("Ruined King's Keep", 35, 20)
        self.map_1 = map_1
        rat = Enemy("Rat", 2, 50)
        goblin = Enemy("Globin", 3, 35)
        slime = Enemy("Slime", 2, 40)
        wolf = Enemy("Wolf", 2, 20)
        shattered_sentinel = Enemy("Shattered Sentinel", 6, 120, True)
        self.sentinel = shattered_sentinel
        rusted_sword = Weapon("Rusted Sword", "Weapon", "Sharp", 5, 2)
        health_potion = Consumables("Health Potion", "Consumable", "Heal_25", 10)
        energy_bar = Consumables("Energy bar", "Consumable", "Ener_25", 10)
        katana = Weapon("Katana", "Weapon", "Sharp", 8, 20)
        scythe = Weapon("Scythe", "Weapon", "Sharp", 13, 30)
        short_bow = Weapon("Short Bow", "Weapon", "Ranged", 10, 25)
        crossbow = Weapon("Crossbow", "Weapon", "Ranged", 12, 30)
        long_bow = Weapon("Long Bow", "Weapon", "Ranged", 14, 35)
        long_sword = Weapon("Long Sword", "Weapon", "Sharp", 25, 65)
        throwing_knife = Weapon("Throwing Knifes", "Weapon", "Ranged", 15, 40)
        staff = Weapon("Staff", "Weapon", "Magical", 20, 50)
        magic_wand = Weapon("Magic Wand", "Weapon", "Magical", 23, 55)
        crowdbreaker_blade = Weapon("Crowdbreaker Blade", "Weapon", "Sharp", 55, 125)
        ethereal_reaper = Weapon("Ethereal Reaper", "Weapon", "Sharp", 65, 150)
        pheonix_bow = Weapon("Phoenix Bow", "Weapon", "Ranged", 60, 135)
        staff_of_dominion = Weapon("Staff Of Dominion", "Weapon",  "Magical", 40, 75)
        large_health_potion = Consumables("Health Potion", "Consumable", "Heal_50", 25)
        energy_drink = Consumables("Energy Drink", "Consumable", "Ener_50", 25)
        superior_health_potion = Consumables("Superior Health Potion", "Consumable", "Heal_100", 55)
        energy_pack = Consumables("Energy Drink", "Consumable", "Ener_100", 55)
        self.rat = rat
        self.globin = goblin
        self.slime = slime
        self.wolf = wolf
        self.health_potion = health_potion
        self.energy_bar = energy_bar
        self.katana = katana
        self.scythe = scythe
        self.short_bow = short_bow
        self.crossbow = crossbow
        self.long_bow = long_bow
        self.long_sword = long_sword
        self.throwing_knife = throwing_knife
        self.staff = staff
        self.magic_wand = magic_wand
        self.crowdbreaker = crowdbreaker_blade
        self.ethereal_reaper = ethereal_reaper
        self.pheonix_bow = pheonix_bow
        self.staff_of_dominion = staff_of_dominion
        self.large_health_potion = large_health_potion
        self.energy_drink = energy_drink
        self.superior_health_potion = superior_health_potion
        self.energy_pack = energy_pack
        name = input("Enter player name: ")
        player = Player(name, rusted_sword)
        self.player = player
        player.add_item(rusted_sword)
        player.add_item(health_potion)
        player.add_item(health_potion)
        player.add_item(health_potion)
        player.add_item(health_potion)
        player.add_item(energy_bar)
        player.add_item(energy_bar)
        player.add_item(energy_bar)
        self.add_enemy(rat, map_1)
        self.add_enemy(slime, map_1)
        self.add_enemy(goblin, map_1)
        self.add_enemy(wolf, map_1)
        self.map_1.update_map(player.pos)
        self.map_1.display_map()
        #Game.clear()
        Game.start(self)

    def move(self, maps):
        while True:
            os.system("clear")

            print(f"Explore {maps.name}")
            maps.display_map()

            print(f"Player's current position: {self.player.pos}")
            
            move = input("Move (W/A/S/D to move, Q to leave the map): ").upper()
            if move == "Q":
                print("Exiting the map.")
                self.player.pos = [0,0]
                break

            if move == "W" and self.player.pos[1] > 0:
                self.player.move(0, -1)
            elif move == "S" and self.player.pos[1] < maps.height - 1:
                self.player.move(0, 1)
            elif move == "A" and self.player.pos[0] > 0:
                self.player.move(-1, 0)
            elif move == "D" and self.player.pos[0] < maps.width - 1:
                self.player.move(1, 0)
            else:
                print("Invalid move!")

            maps.update_map(self.player.pos)
    
    def add_enemy(self, enemy, map):
        map.enemy_list.append(enemy)


    def line():
        print("-------------------------------------------------------")

    def clear():
        os.system("clear")

    def slow_print(text):
        for char in text:
            print(char, end = "", flush = True)
            time.sleep(0.005)
        print("\n")

    def fight(self, enemy):
        fight_loop = True
        choice_loop1 = True
        choice_loop2 = True
        Game.clear()
        if enemy.boss_status == True:
            while fight_loop:
                print(f"{self.player.name}'s fight with {enemy.name}")
                choice1 = input("""
        1. Attack
        2. Use Item      
        """)
                choice_loop1 = True
                choice_loop2 = True
                while choice_loop1:
                    if choice1 == "1":
                        Game.clear()
                        self.player.attack(enemy)
                        enemy.attack(self.player)
                        print(self.player.energy)
                    choice_loop1 = False
                while choice_loop2:
                    if choice1 == "2":
                        if self.player.calculate_inventory_size() == 0:
                            print("You have no items in your inventory, you cannot use item")
                            choice_loop2 = False
                        print(f"{self.player.name}'s inventory")
                        for index, item in enumerate(self.player.inventory, start = 1):
                            print(f"{index}. {item.name}")
                        check = True
                        while check:
                            choice2 = input("What item would you like to use: ")
                            try:
                                self.player.use_item(self.player.inventory[int(choice2) - 1])
                                choice_loop2 = False
                                check = False
                            except ValueError:
                                print("Please input the number corresponding to the item you want to use")
                    choice_loop2 = False

                if enemy.health == 0:
                    print(f"The boss {enemy.name} has been defeated congratulations!")
                    if enemy.boss_status == True:
                        self.player.essence += 1
                        self.player.level_up()
                        print(f"{self.player.name} collect the bounty on {enemy.name} and recieve 75 coins")
                        self.player.money += 75
                    print(f"{self.player.name} finds 4 coins on the enemy")
                    self.player.money += 5
                    self.player.health = self.player.max_health
                    self.player.energy = self.player.max_energy
                    self.shop()
        
                elif self.player.health == 0:
                    print(f"The {enemy.name} has defeated {self.player.name}")
                    f = Figlet(font="slant")
                    x = f.renderText("Game Over")
                    y = colored(x, "red" , attrs=['bold'])
                    print(y)
                    quit()
        else:
            while fight_loop:
                print(f"{self.player.name}'s fight with {enemy.name}")
                choice1 = input("""
        1. Attack
        2. Use Item
        3. Flee     
        """)
                choice_loop1 = True
                choice_loop2 = True
                choice_loop3 = True
                while choice_loop1:
                    if choice1 == "1":
                        Game.clear()
                        self.player.attack(enemy)
                        enemy.attack(self.player)
                        print(self.player.energy)
                    choice_loop1 = False
                while choice_loop2:
                    if choice1 == "2":
                        if self.player.calculate_inventory_size() == 0:
                            print("You have no items in your inventory, you cannot use item")
                            choice_loop2 = False
                        print(f"{self.player.name}'s inventory")
                        for index, item in enumerate(self.player.inventory, start = 1):
                            print(f"{index}. {item.name}")
                        check = True
                        while check:
                            choice2 = input("What item would you like to use: ")
                            try:
                                self.player.use_item(self.player.inventory[int(choice2) - 1])
                                choice_loop2 = False
                                check = False
                            except ValueError:
                                print("Please input the number corresponding to the item you want to use")
                    choice_loop2 = False
                while choice_loop3:
                    if choice1 == '3':
                        print(f"{self.player.name} has fled from {enemy.name}")
                        fight_loop = False
                        choice_loop3 = False

                if enemy.health == 0:
                    print(f"The boss {enemy.name} has been defeated congratulations!")
                    if enemy.boss_status == True:
                        self.player.essence += 1
                        self.player.level_up()
                        print(f"{self.player.name} collect the bounty on {enemy.name} and recieve 75 coins")
                        self.player.money += 75
                    print(f"{self.player.name} finds 4 coins on the enemy")
                    self.player.money += 5
                    self.player.health = self.player.max_health
                    self.player.energy = self.player.max_energy
                    self.shop() 

                elif self.player.health == 0:
                    print(f"The {enemy.name} has defeated {self.player.name}")
                    f = Figlet(font="slant")
                    x = f.renderText("Game Over")
                    y = colored(x, "red" , attrs=['bold'])
                    print(y)
                    quit()

    def shop(self):
            shop_loop = True
            while shop_loop:
                print("You have the chance to buy and sell items in the shop")
                shop_choice = input("""
1. Buy
2. Sell
3. Exit    
""")
                if shop_choice == '1':
                    print("The shop's items:")
                    print(f"{self.player.name} has {self.player.money} coins")
                    for index, item in enumerate(self.shop_items, start = 1):
                        print(f"{index}. {item.name} - Price = {item.value}")
                    check1 = True
                    while check1:
                        item_choice = input("What item would you like to buy: ")
                        try:
                            self.player.add_item(self.shop_items[int(item_choice) - 1])
                            self.player.money -= self.shop_items[int(item_choice - 1)].value
                            check1 = False
                        except ValueError:
                            print("Please input the number corresponding to the item you want to buy")

                if shop_choice == '2':
                    print(f"Your inventory:")
                    for index, item in enumerate(self.player.inventory, start = 1):
                        print(f"{index}. {item.name} - Price {item.value}")
                    check2 = True
                    while check2:
                        item_sell_choice = input("What item would you like to sell: ")
                        try:
                            self.player.remove_item(self.player.inventory[int(item_sell_choice) - 1])
                            item_selling_price = self.inventory[int(item_sell_choice)]
                            print(f"{self.player.name} has gain {item_selling_price.value}")
                            self.player.money += item_selling_price.value
                            check2 = False
                        except ValueError:
                            print("Please input the number corresponding to the item you want to buy")

                if shop_choice == '3':
                    shop_loop = False


    def start(self):
        game_loop = True
        while game_loop:
            f = Figlet(font="slant")
            x = f.renderText("Welcome To Forgetten Realm!")
            y = colored(x, "red" , attrs=['bold'])
            print(y)
            Game.line()
            opp1 = True
            while opp1:  
                choice = input("""
    1. New Game
    2. Rules
    3. Quit Game      
    """)
                Game.line() 
                if choice == '1':
                    Game.clear()
                    Game.line()
                    storyline = "You awaken in a crumbling temple at the heart of the Forgotten Realm, a world shrouded in eternal twilight. The kings once ruled here, but their power fractured, plunging the land into chaos. Monstrous creatures roam the desolate ruins, guarding the fragments of royal essence scattered across the realm. With only a rusted sword and a weathered bag, you must uncover the truth of your identity and restore balance or claim the power of the kings for yourself. Each fragment brings you closer to salvation or domination.\nThe fate of the Forgotten Realm rests in your hands."
                    Game.slow_print(storyline)
                    Game.line() 
                    opp1 = False
                if choice == '2':
                    print("There are no rules just have fun!")
                    Game.line()
                if choice == '3':
                    print("Goodbye")
                    quit() 
            
            Game.clear()
            introduction = "You step into the heart of the Crumbling Temple, the air heavy with age. From the shadows, a hulking figure emerges—stone armour cracked and glowing eyes fixed on you. You seek the essence of kings?  it growls. I am the Shattered Sentinel. You will not pass.\nWith a roar, it raises its jagged sword, charging toward you. The battle begins."
            Game.line()
            Game.slow_print(introduction)
            time.sleep(2)
            self.fight(self.sentinel)

            game_loop = False
    


Game1 = Game()
Game1.setup()
