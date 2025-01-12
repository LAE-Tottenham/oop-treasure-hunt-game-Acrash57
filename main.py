from place import Map
from entity import Player, Enemy
from item import Weapon, Consumables
from pyfiglet import Figlet
from termcolor import colored
import os
import time

class Game():
    def __init__(self):
        self.last_move = None
        self.player = None
        self.sentinel = None
        self.korrath = None
        self.valkar = None
        self.aetheris = None
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
        self.shop_items = None
        self.map_items = None
        self.map_1 = None
        self.map_2 = None
        self.map_3 = None
        self.map_4 = None
        self.map_5 = None
        self.map_6 = None
        self.map_7 = None
        self.map_8 = None
        self.map_9 = None
        self.map_10 = None

    def setup(self):
        map_1 = Map("Ruined King's Keep", 35, 20)
        map_2 = Map("Duskwither Grove", 35, 20)
        map_3 = Map("Ashenfall Basin", 35, 20)
        map_4 = Map("Shadowspire Pass", 35, 20)
        map_5 = Map("Solrend Ruins", 35, 20)
        map_6 = Map("Oblivion Reach", 35, 20)
        map_7 = Map("Crystalhollow Depths", 35, 20)
        map_8 = Map("Echoheart Sanctum", 35, 20)
        map_9 = Map("Mire of Wails", 35, 20)
        map_10 = Map("Forsaken King's Throne", 35, 20)
        self.map_1 = map_1
        self.map_2 = map_2
        self.map_3 = map_3
        self.map_4 = map_4
        self.map_5 = map_5
        self.map_6 = map_6
        self.map_7 = map_7
        self.map_8 = map_8
        self.map_9 = map_9
        self.map_10 = map_10
        rat = Enemy("Rat", 2, 50)
        goblin = Enemy("Globin", 3, 35)
        slime = Enemy("Slime", 2, 40)
        wolf = Enemy("Wolf", 4, 65)
        dragon = Enemy("Dragon", 15, 120)
        mercenary = Enemy("Mercenary", 13, 135)
        brute = Enemy("Brute", 11, 150)
        skeleton_warrior = Enemy("Skeleton Warrior", 8, 100)
        zombie = Enemy("Zombie", 5, 70)
        golem = Enemy("Golem", 3, 150)
        shattered_sentinel = Enemy("Shattered Sentinel", 7, 120, True)
        korrath = Enemy("Korrath the Stormbringer", 16, 160, True)
        valkar = Enemy("Valkar the Fallen", 35, 180, True)
        aetheris = Enemy("King Aetheris the Lost Monarch", 45, 225, True)
        self.sentinel = shattered_sentinel
        self.korrath = korrath
        self.valkar = valkar
        self.aetheris = aetheris
        rusted_sword = Weapon("Rusted Sword", "Weapon", "Sharp", 5, 2)
        health_potion = Consumables("Health Potion", "Consumable", "Heal_25", 20)
        energy_bar = Consumables("Energy bar", "Consumable", "Ener_25", 20)
        katana = Weapon("Katana", "Weapon", "Sharp", 8, 20)
        scythe = Weapon("Scythe", "Weapon", "Sharp", 13, 30)
        short_bow = Weapon("Short Bow", "Weapon", "Ranged", 10, 25)
        crossbow = Weapon("Crossbow", "Weapon", "Ranged", 12, 30)
        long_bow = Weapon("Long Bow", "Weapon", "Ranged", 14, 35)
        long_sword = Weapon("Long Sword", "Weapon", "Sharp", 25, 65)
        throwing_knife = Weapon("Throwing Knifes", "Weapon", "Ranged", 15, 40)
        staff = Weapon("Staff", "Weapon", "Magical", 20, 50)
        magic_wand = Weapon("Magic Wand", "Weapon", "Magical", 23, 55)
        crownbreaker_blade = Weapon("Crownbreaker Blade", "Weapon", "Sharp", 55, 145)
        ethereal_reaper = Weapon("Ethereal Reaper", "Weapon", "Sharp", 65, 185)
        pheonix_bow = Weapon("Phoenix Bow", "Weapon", "Ranged", 60, 155)
        staff_of_dominion = Weapon("Staff Of Dominion", "Weapon",  "Magical", 40, 125)
        large_health_potion = Consumables("Health Potion", "Consumable", "Heal_50", 30)
        energy_drink = Consumables("Energy Drink", "Consumable", "Ener_50", 30)
        superior_health_potion = Consumables("Superior Health Potion", "Consumable", "Heal_100", 55)
        energy_pack = Consumables("Energy Drink", "Consumable", "Ener_100", 55)
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
        self.crownbreaker = crownbreaker_blade
        self.ethereal_reaper = ethereal_reaper
        self.pheonix_bow = pheonix_bow
        self.staff_of_dominion = staff_of_dominion
        self.large_health_potion = large_health_potion
        self.energy_drink = energy_drink
        self.superior_health_potion = superior_health_potion
        self.energy_pack = energy_pack
        self.shop_items = [self.health_potion, self.energy_bar, self.katana, self.scythe, self.short_bow, self.crossbow, self.long_bow, self.long_sword, self.throwing_knife, self.staff, self.magic_wand, self.crownbreaker, self.ethereal_reaper, self.pheonix_bow, self.staff_of_dominion, self.large_health_potion, self.energy_drink, self.superior_health_potion, self.energy_pack]
        self.map_items = [self.health_potion, self.energy_bar, self.large_health_potion, self.energy_drink, self.katana, self.short_bow, self.staff_of_dominion, self.crownbreaker]
        check = True
        name = input("Enter player name: ")
        while check:
            if name == '':
                Game.clear() 
                print("Please input a valid name!")
                name = input("Enter player name: ")
            else:
                check = False
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
        self.add_items(map_1)
        map_1.get_items()
        self.map_1.update_map(player.pos)

        self.add_enemy(rat, map_2)
        self.add_enemy(slime, map_2)
        self.add_enemy(goblin, map_2)
        self.add_enemy(zombie, map_2)
        self.add_items(map_2)
        map_2.get_items()
        self.map_2.update_map(player.pos)

        self.add_enemy(slime, map_3)
        self.add_enemy(goblin, map_3)
        self.add_enemy(wolf, map_3)
        self.add_enemy(skeleton_warrior, map_3)
        self.add_items(map_3)
        map_3.get_items()
        self.map_3.update_map(player.pos)

        self.add_enemy(goblin, map_4)
        self.add_enemy(wolf, map_4)
        self.add_enemy(zombie, map_4)
        self.add_enemy(skeleton_warrior, map_4)
        self.add_items(map_4)
        map_4.get_items()
        self.map_4.update_map(player.pos)

        self.add_enemy(wolf, map_5)
        self.add_enemy(zombie, map_5)
        self.add_enemy(skeleton_warrior, map_5)
        self.add_enemy(brute, map_5)
        self.add_items(map_5)
        map_5.get_items()
        self.map_5.update_map(player.pos)

        self.add_enemy(zombie, map_6)
        self.add_enemy(skeleton_warrior, map_6)
        self.add_enemy(brute, map_6)
        self.add_enemy(mercenary, map_6)
        self.add_items(map_6)
        map_6.get_items()
        self.map_6.update_map(player.pos)

        self.add_enemy(skeleton_warrior, map_7)
        self.add_enemy(brute, map_7)
        self.add_enemy(mercenary, map_7)
        self.add_enemy(zombie, map_7)
        self.add_items(map_7)
        map_7.get_items()
        self.map_7.update_map(player.pos)

        self.add_enemy(brute, map_8)
        self.add_enemy(mercenary, map_8)
        self.add_enemy(skeleton_warrior, map_8)
        self.add_enemy(golem, map_8)
        self.add_items(map_8)
        map_8.get_items()
        self.map_8.update_map(player.pos)

        self.add_enemy(mercenary, map_9)
        self.add_enemy(golem, map_9)
        self.add_enemy(skeleton_warrior, map_9)
        self.add_enemy(dragon, map_9)
        self.add_items(map_9)
        map_9.get_items()
        self.map_9.update_map(player.pos)

        self.add_enemy(dragon, map_10)
        self.add_enemy(golem, map_10)
        self.add_enemy(skeleton_warrior, map_10)
        self.add_enemy(mercenary, map_10)
        self.add_items(map_10)
        map_10.get_items()
        self.map_10.update_map(player.pos)
        Game.clear()
        Game.start(self)

    def add_border(text):
        # Define the border characters
        border_char = '='
        side_border_char = '|'
        
        border_length = len(text) + 2 
        border = border_char * border_length
        
        print(border)
        print(side_border_char + text + side_border_char)
        print(border)

    def move(self, maps):
        while True:
            os.system("clear")
            x = f"Explore {maps.name}"
            Game.add_border(x)
            
            maps.display_map()

            print(f"Player's current position: {self.player.pos}")
            self.last_move = self.player.pos[:]
            
            move = input("Move (W/A/S/D to move, Q to leave the map): ").upper()
            if move == "Q":
                print(f"{self.player.name} has left {maps.name}")
                self.player.pos = [0,0]
                maps.update_map(self.player.pos)
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
            
    
            for enemy in maps.enemy_list:
                if enemy.pos == self.player.pos:
                    Game.clear()
                    print(f"{self.player.name} has encountered a {enemy.name}!")
                    time.sleep(2)
                    self.fight(enemy)
                    if enemy.health == 0:
                        self.remove_enemy(enemy, maps)
                    else:
                        self.player.pos = self.last_move[:]
            
            check = True
            while check: 
                for item in maps.final_map_items:
                    if item.pos == self.player.pos:
                        Game.clear()
                        print(f"{self.player.name} has discovered a chest and came across a {item.name}!")
                        choice = input("""
1. Take Item
2. Leave Item     
""")
                        if choice == '1':
                            Game.clear()
                            Game.line() 
                            if len(self.player.inventory) < self.player.inventory_max_weight:
                                print(f"{self.player.name} has opened the chest and taken the {item.name}")
                                self.player.add_item(item)
                                maps.final_map_items.remove(item)
                            else:
                                print("Invenrtory is full")
                            time.sleep(3) 
                            check = False
                        elif choice == '2':
                            Game.clear()
                            Game.line()  
                            print(f"{self.player.name} has closed the chest and left the {item.name}")
                            self.player.pos = self.last_move[:]
                            time.sleep(5) 
                            check = False
                        else:
                            print(f"Please input the correct number for your choice")
                    else:
                        check = False
            
            maps.update_map(self.player.pos)
    
    def add_enemy(self, enemy, map):
        map.enemy_list.append(enemy)

    def remove_enemy(self, enemy, map):
        map.enemy_list.remove(enemy)
    
    def add_items(self, maps):
        maps.map_items = self.map_items

    def line():
        print("-------------------------------------------------------")

    def clear():
        os.system("clear")

    def slow_print(text):
        for char in text:
            print(char, end = "", flush = True)
            time.sleep(0.035)
        print("\n")

    def fight(self, enemy):
        fight_loop = True
        choice_loop1 = True
        choice_loop2 = True
        Game.clear()
        Game.line() 
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
                        Game.line()
                        self.player.attack(enemy)
                        enemy.attack(self.player)
                    choice_loop1 = False
                while choice_loop2:
                    if choice1 == "2":
                        Game.clear()
                        Game.line()
                        if self.player.calculate_inventory_size() == 0:
                            print("You have no items in your inventory, you cannot use items")
                            choice_loop2 = False
                        print(f"{self.player.name}'s inventory")
                        for index, item in enumerate(self.player.inventory, start = 1):
                            print(f"{index}. {item.name}")
                        check = True
                        while check:
                            choice2 = input("What item would you like to use: ")
                            try:
                                Game.clear()
                                self.player.use_item(self.player.inventory[int(choice2) - 1])
                                choice_loop2 = False
                                check = False
                            except ValueError:
                                print("Please input the number corresponding to the item you want to use")
                    choice_loop2 = False

                if enemy.health == 0:
                    Game.clear()
                    Game.line()
                    print(f"The boss {enemy.name} has been defeated congratulations!")
                    self.player.essence += 1
                    self.player.level_up()
                    print(f"{self.player.name} has gained 1 kings essence")
                    print(f"{self.player.name} has {self.player.essence} kings fragment")
                    print(f"{self.player.name} looted 50 coins off {enemy.name}")
                    time.sleep(5) 
                    self.player.money += 50
                    self.player.health = self.player.max_health
                    self.player.energy = self.player.max_energy
                    fight_loop = False
        
                elif self.player.health == 0:
                    Game.clear()
                    Game.line()
                    print(f"The {enemy.name} has defeated {self.player.name}")
                    end = Figlet(font="slant")
                    end1 = end.renderText("Game Over")
                    end2 = colored(end1, "red" , attrs=['bold'])
                    print(end2)
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
                        Game.line()
                        self.player.attack(enemy)
                        enemy.attack(self.player)
                    choice_loop1 = False
                while choice_loop2:
                    if choice1 == "2":
                        Game.clear()
                        Game.line()
                        if self.player.calculate_inventory_size() == 0:
                            print("You have no items in your inventory, you cannot use items")
                            choice_loop2 = False
                        print(f"{self.player.name}'s inventory")
                        for index, item in enumerate(self.player.inventory, start = 1):
                            print(f"{index}. {item.name}")
                        check = True
                        while check:
                            choice2 = input("What item would you like to use: ")
                            try:
                                Game.clear()
                                self.player.use_item(self.player.inventory[int(choice2) - 1])
                                choice_loop2 = False
                                check = False
                            except ValueError:
                                print("Please input the number corresponding to the item you want to use")
                    choice_loop2 = False
                while choice_loop3:
                    if choice1 == '3':
                        Game.clear()
                        Game.line()
                        print(f"{self.player.name} was able to escape the {enemy.name}")
                        time.sleep(2) 
                        fight_loop = False
                        choice_loop3 = False
                    choice_loop3 = False

                if enemy.health == 0:
                    Game.clear()
                    Game.line()
                    print(f"The {enemy.name} has been defeated congratulations!")
                    print(f"{self.player.name} found 5 coins on the {enemy.name}")
                    time.sleep(2) 
                    self.player.money += 5
                    self.player.health = self.player.max_health
                    self.player.energy = self.player.max_energy
                    self.shop() 
                    fight_loop = False

                elif self.player.health == 0:
                    Game.clear()
                    Game.line()
                    print(f"The {enemy.name} has defeated {self.player.name}")
                    end = Figlet(font="slant")
                    end1 = end.renderText("Game Over")
                    end2 = colored(end1, "red" , attrs=['bold'])
                    print(end2)
                    quit()

    def shop(self):
            shop_loop = True
            time.sleep(3)
            Game.clear()
            while shop_loop:
                Game.line() 
                print("You have the chance to buy and sell items in the shop")
                shop_choice = input("""
1. Buy
2. Sell
3. Exit    
""")
                if shop_choice == '1':
                    Game.clear()
                    Game.line() 
                    print(f"{self.player.name} has {self.player.money} coins")
                    print("The shop's items:")
                    for index, item in enumerate(self.shop_items, start = 1):
                        time.sleep(0.025)
                        print(f"{index}. {item.name} - Price = {item.value}")
                    check1 = True
                    while check1:
                        item_choice = input("What item would you like to buy: ")
                        try:
                            if self.shop_items[int(item_choice) - 1].value > self.player.money:
                                Game.clear() 
                                print(f"{self.player.name} doesn't have enough money for the {self.shop_items[int(item_choice) - 1].name}")
                                time.sleep(2) 
                                Game.clear() 
                                continue
                            else:
                                Game.clear()
                                self.player.add_item(self.shop_items[int(item_choice) - 1])
                                self.player.money -= self.shop_items[int(item_choice) - 1].value
                                print(f"{self.player.name} has purchased {self.shop_items[int(item_choice) - 1].name} from the shop for {self.shop_items[int(item_choice) - 1].value} coins!")
                                time.sleep(2)
                                Game.clear() 
                                check1 = False
                        except ValueError:
                            print("Please input the number corresponding to the item you want to buy")
                        except IndexError:
                            print("Please choose a item within the numbered item list")

                if shop_choice == '2':
                    Game.clear()
                    Game.line() 
                    print(f"Your inventory:")
                    for index, item in enumerate(self.player.inventory, start = 1):
                        time.sleep(0.025)
                        print(f"{index}. {item.name} - Price {item.value}")
                    check2 = True
                    while check2:
                        item_sell_choice = input("What item would you like to sell: ")
                        try:
                            item_selling_price = self.player.inventory[int(item_sell_choice) - 1]
                            print(f"{item_selling_price.value} {item_selling_price.name}")
                            print(f"{self.player.name} has gained {item_selling_price.value} coins")
                            self.player.remove_item(self.player.inventory[int(item_sell_choice)])
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
                    Game.clear()
                    Game.line() 
                    goodbye_text = f.renderText("Goodbye")
                    goodbye2 = colored(goodbye_text, "red" , attrs=['bold'])
                    print(goodbye2)
                    quit() 
            
            Game.clear()
            introduction = "You step into the heart of the Crumbling Temple, the air heavy with age. From the shadows, a hulking figure emerges—stone armour cracked and glowing eyes fixed on you. You seek the essence of kings?  it growls. I am the Shattered Sentinel. You will not pass.\nWith a roar, it raises its jagged sword, charging toward you. The battle begins."
            Game.line()
            Game.slow_print(introduction)
            time.sleep(2)
            self.fight(self.sentinel)
            Game.clear()
            Game.line() 
            text1 = f"After defeating the shattered sentinel you see a quest paper on the wall of the crumbling temble which entails exploring the realm and finding the kings fragmented essence to gather it at the forsaken king's throne with the purpose of restoring peace and bringing light back to the realm"
            Game.slow_print(text1)
            opp2 = True
            while opp2:
                choice1 = input("""
1. Accept
2. Ignore    
""")
                if choice1 == '1':
                    opp3 = True
                    while opp3:
                        Game.clear()
                        Game.line() 
                        print("You can explore the following locations:")
                        choice2 = input("""
1. Ruined King's Keep
2. Duskwither Grove
3. Ashenfall Basin: The Storm's Wrath
4. Shadowspire Pass
5. Solrend Ruins
6. Oblivion Reach: The Silent Guardian
7. Crystalhollow Depths
8. Echoheart Sanctum
9. Mire of Wails
10. Forsakened King's Throne: The Last Trial    
""")
                        if choice2 == '1':
                            self.move(self.map_1)

                        elif choice2 == '2':
                            self.move(self.map_2)

                        elif choice2 == '3':
                            self.move(self.map_3)
                            Game.clear()
                            Game.line() 
                            txt3 = "You step into the heart of Ashenfall Basin, where the air crackles with electricity and the land is torn by relentless storms. In the midst of the chaos stands Korrath the Stormbringer, his figure surrounded by swirling winds and lightning. Behind him, the King's Essence pulses with the promise of peace and stability. You seek the power to restore what was lost, he intones, his voice rumbling like thunder. But I am bound to protect it, for its power is too great for any to wield alone.\nThe storm intensifies around him, and the choice is yours: face Korrath for the essence or turn away, leaving the realm in turmoil."
                            Game.slow_print(txt3)
                            opp4 = True
                            while opp4:
                                choice3 = input("""
1. Fight
2. Run   
""")
                                if choice3 == '1':
                                    self.fight(self.korrath)
                                    opp4 = False
                                elif choice3 == '2':
                                    txt4 = "As you turn to flee, the storm rages behind you, its fury intensifying with each step. Korrath's voice echoes through the wind, a warning lost in the chaos."
                                    Game.slow_print(txt4)
                                    opp4 = False

                        elif choice2 == '4':
                            self.move(self.map_4)

                        elif choice2 == '5':
                            self.move(self.map_5)

                        elif choice2 == '6':
                            self.move(self.map_6)
                            Game.clear()
                            Game.line() 
                            txt5 = "Amid the ruins of Oblivion Reach, you approach a crumbling altar, where Valkar the Fallen stands, his broken armor glowing faintly. The King’s Essence pulses within him, bound to his fractured soul.\nSilent and unwavering, he is the final guardian, and the only way forward lies through him. The storm of battle is inevitable."
                            Game.slow_print(txt5)
                            self.fight(self.valkar)

                        elif choice2 == '7':
                            self.move(self.map_7)

                        elif choice2 == '8':
                            self.move(self.map_8)

                        elif choice2 == '9':
                            self.move(self.map_9)

                        elif choice2 == '10':
                            self.move(self.map_10)
                            Game.clear()
                            Game.line() 
                            if self.player.essence >= 3:
                                txt6 = "After all your trials, you stand before King Aetheris, the final piece of the King's Essence glowing softly in his hand. His broken form stands tall, yet his weary eyes speak of a past long lost to time. You have gathered the three pieces, King Aetheris says, his voice a mixture of sorrow and hope. The fate of the realm now lies in your hands. You can choose to restore what was lost or shape a new future for this world.\nKing Aetheris extends the final essence to you. Take it, and choose wisely. Your decision will determine the future of the Forgotten Realm."
                                self.player.essence += 1 
                                Game.slow_print(txt6)
                                opp5 = True
                                while opp5:
                                    choice4 = input("""
1. Restore The Kings
2. Become King
""")
                                    if choice4 == '1':
                                        Game.clear()
                                        Game.line() 
                                        txt7 = "You take the final essence, and as it enters your being, the ancient power of the old kings flows through you. The land begins to heal, the once-shattered kingdom slowly mending. The old kings return, their guidance reshaping the future of the realm. King Aetheris finds peace, knowing that the old rulers will guide the realm back to prosperity.\nThe cycle of peace is restored under their rule."
                                        Game.slow_print(txt7)
                                        time.sleep(2) 
                                        Game.print_end()
                                        print(f"The Saviour {self.player.name} stats:")
                                        quit() 

                                    if choice4 == '2':
                                        Game.clear()
                                        Game.line()
                                        txt8 = "You grasp the final essence, and instead of restoring the old kings, you claim their power as your own. The realm trembles as you absorb the essence, and you become the new ruler of the kingdom. The old kings are lost, their reigns forgotten. The realm may heal, but it is now under your rule, shaped by your desires and ambition.\nThe future is now yours to command."
                                        Game.slow_print(txt8)
                                        time.sleep(2) 
                                        Game.print_end()
                                        Game.line() 
                                        print(f"The King {self.player.name} stats:")
                                        self.print_stats() 
                                        quit()
                            else:
                                txt9 = "You stand before King Aetheris, but you are incomplete. A piece of the King's Essence remains just out of reach, its glow beckoning you forward. You are not whole, King Aetheris says solemnly. You lack the final two pieces, and yet you seek the power of the ancients. There is no path forward without it. King Aetheris raises his hand, guarding the an essence.\nThere is no room for negotiation—only one path remains: combat."
                                Game.slow_print(txt9)
                                self.fight(self.aetheris)
                                txt10 = "You have taken the essence, King Aetheris whispers with his final breath, but the realm will never be the same, you lack the final piece. As you absorb the essences you collected, the power surges within you. But the realm cracks and trembles, broken as you are. The old kings are gone, and you are left to rule a shattered kingdom, one that reflects the fractured soul now in power.\nThe future is yours, but it is a world left in ruin, and your reign begins in the aftermath of chaos."
                                Game.slow_print(txt10)
                                time.sleep(2) 
                                Game.print_end()
                                Game.line() 
                                print(f"The Shattered Ruler {self.player.name} stats:")
                                self.print_stats() 
                                quit() 

                if choice1 == '2':
                    Game.clear()
                    Game.line() 
                    txt2 = "You have turned away from the path of destiny. The Forgotten Realm remains in chaos, the kings' essences lost, and peace out of reach. Perhaps, in time, you'll reconsider. For now, the realm awaits your decision..."
                    Game.clear()
                    Game.line() 
                    Game.slow_print(txt2)
                    Game.clear()
                    Game.line() 
                    t1 = f.renderText(f"Goodbye {self.player.name}")
                    t2 = colored(t1, "red" , attrs=['bold'])
                    print(t2)
                    Game.line()
                    print(f"{self.player.name} The Forgetten stats:")
                    self.print_stats() 
                    quit()
            
            game_loop = False

    def print_end():
        Game.clear()
        Game.line() 
        f = Figlet(font="slant")
        End = f.renderText(f"The End")
        End2 = colored(End, "red" , attrs=['bold'])
        print(End2)

    def print_stats(self):
        print(f"{self.player.name}'s level - {self.player.level}")
        print(f"{self.player.name}'s strenght - {self.player.strength}")
        print(f"{self.player.name}'s king's fragments - {self.player.essence}")
        print(f"{self.player.name}'s money - {self.player.money}")


Game1 = Game()
Game1.setup()