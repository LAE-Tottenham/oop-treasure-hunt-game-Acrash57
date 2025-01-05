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
    def setup(self):
        map_1 = Map("First Map", 35, 20)
        shattered_sentinel = Enemy("Shattered Sentinel", 7, 130)
        self.sentinel = shattered_sentinel
        rusted_sword = Weapon("Rusted Sword", "Weapon", "Sharp", 5)
        health_potion = Consumables("Health Potion", "Consumable", "Heal_25")
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
            print(char, end = "", flush = True )
            time.sleep(0.005)
        print("\n")
    def fight(self, enemy):
        fight_loop = True
        Game.clear()
        while fight_loop:
            choice1 = input("""
    1. Attack
    2. Use Item      
    """)
            if choice1 == "1":
                Game.clear()
                self.player.attack(enemy)
                enemy.attack(self.player)
            if choice1 == "2":
                print(f"{self.player.name}'s inventory")
                for index, item in enumerate(self.player.inventory, start = 1):
                    print(f"{index}. {item.name}")
                check = True
                while check:
                    choice2 = input("What item would you like to use: ")
                    try:
                        self.player.use_item(self.player.inventory[int(choice2) - 1])
                    except ValueError:
                        print("Please input the number corresponding to the item you want to use")
  
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
            time.sleep(3)
            self.fight(self.sentinel)
            game_loop = False
    


Game1 = Game()
Game1.setup()
