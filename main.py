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
        self.essence = 0
        self.player = None
        self.sentinel = None
        self.rat = None
        self.globin = None
        self.slime = None

    def setup(self):
        map_1 = Map("First Map", 35, 20)
        rat = Enemy("Rat", 2, 50)
        goblin = Enemy("Globin", 1, 35)
        slime = Enemy("Slime", 2, 40)
        shattered_sentinel = Enemy("Shattered Sentinel", 6, 120, True)
        self.sentinel = shattered_sentinel
        rusted_sword = Weapon("Rusted Sword", "Weapon", "Sharp", 5, 15)
        health_potion = Consumables("Health Potion", "Consumable", "Heal_25", 10)
        energy_bar = Consumables("Energy bar", "Consumable", "Ener_25", 10)
        katana = Weapon("Katana", "Weapon", "Sharp", 8, 20)
        scythe = Weapon("Scythe", "Weapon", "Sharp", 13, 30)
        short_bow = Weapon("Short Bow", "Weapon", "Ranged", 10, 25)
        long_bow = Weapon("Long Bow", "Weapon", "Ranged", 12, 28)
        large_health_potion = Consumables("Health Potion", "Consumable", "Heal_50", 25)
        energy_drink = Consumables("Energy Drink", "Consumable", "Ener_25", 25)
        map_1.display_map()
        name = input("Enter player name: ")
        player = Player(name, rusted_sword)
        self.player = player
        player.add_item(rusted_sword)
        player.add_item(health_potion)
        player.add_item(health_potion)
        player.add_item(health_potion)
        player.add_item(health_potion)
        Game.clear()
        Game.start(self) 

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
                print(f"The {enemy.name} has been defeated congratulations!")
                if enemy.boss_status == True:
                    self.player.essence += 1
                    self.player.level += 1
                    self.player.money += 75
                self.player.money += 5
                shop_loop = True
                while shop_loop:
                    print(f"The Shop")
                    shop_choice = input("""
    1. Shop
    2. Exit    
    """)
                    if shop_choice == '1':
                        pass
                    if shop_choice == '2':
                        shop_loop = False
                        pass

                fight_loop = False
            elif self.player.health == 0:
                print(f"The {enemy.name} has defeated {self.player.name}")
                f = Figlet(font="slant")
                x = f.renderText("Game Over")
                y = colored(x, "red" , attrs=['bold'])
                print(y)
                quit()

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
