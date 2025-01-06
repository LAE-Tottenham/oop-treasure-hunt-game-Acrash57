import random
import copy
import os

ANSI_RESET = "\033[0m"
ANSI_YELLOW = "\033[33m"
ANSI_GREEN = "\033[32m"
ANSI_BLUE = "\033[34m"
ANSI_RED = "\033[31m"
ANSI_WHITE = "\033[97m"
ANSI_MAGENTA = "\033[35m"
ANSI_CYAN = "\033[36m"

class Tile():
    def __init__(self, symbol, colour, coloured = True):
        self.symbol = f"{colour}{symbol}{ANSI_RESET}" if coloured else symbol

plains = Tile(".", ANSI_GREEN)  
forest = Tile("T", ANSI_GREEN)  
pine = Tile("P", ANSI_CYAN)  
mountain = Tile("#", ANSI_WHITE)  
water = Tile("~", ANSI_BLUE)  
player_icon = Tile("X", ANSI_MAGENTA)


class Map():
    def __init__(self, given_name, given_width, given_height):
        self.name = given_name
        self.width = given_width
        self.height = given_height
        self.next_places = []
        self.items = []
        self.generate_map()
        self.generate_patch(2,6,8,forest)
        self.generate_patch(2,5,8,water)
        self.generate_patch(2,6,10,mountain)
        self.generate_patch(3,6,6,pine)
     
    def generate_map(self):
        self.init_map_data = []
        for row in range(self.height):
            row_data = [] 
            for col in range(self.width):
                row_data.append(plains)
            self.init_map_data.append(row_data)
        self.map_data = copy.deepcopy(self.init_map_data)
    
    def update_map(self, pos, marker):
        x, y = pos
        self.map_data = copy.deepcopy(self.init_map_data)
        self.map_data[y][x] = marker

    
    def generate_patch(self, given_patch_amount, min_size, max_size, tile: Tile, irr = True):
        for _ in range(given_patch_amount):
            width = random.randint(min_size, max_size)
            height = random.randint(min_size, max_size)
            start_x = random.randint(1, self.width - width - 1)
            start_y = random.randint(1, self.height - height - 1)

            if irr:
                fir_start_x = random.randint(3, self.width - max_size)
                for i in range(height):
                    width = random.randint(int(0.7 * max_size), max_size)
                    start_x = fir_start_x - random.randint(1,2)
                    for j in range(width):
                        self.init_map_data[start_y + i][start_x + j] = tile
            else:
                for i in range(height):  
                    for j in range(width):
                        self.init_map_data[start_y + i][start_x + j] = tile

    def display_map(self):
        frame = self.width * "-" + '--'
        print(frame)
        for row in self.map_data:
            row_tiles = [tile.symbol for tile in row]
            print("|" + "".join(row_tiles) + "|")
        print(frame)


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
    def __init__(self, given_name, given_weapon, given_health = 100, given_strenght = 1, given_level = 0):
        super().__init__(given_name, given_health)
        self.level = given_level
        self.strenght = given_strenght
        self.inventory_max_weight = 25
        self.inventory = []
        self.pos = [0,0]
        self.marker = player_icon
        self.weapon = given_weapon
        

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
    
game_map = Map("Demo Map", 35, 20)
player = Player("Hero", "Sword")
game_map.update_map(player.pos, player.marker)


while True:
    os.system("clear")

    game_map.display_map()

    print(f"Player's current position: {player.pos}")
    
    move = input("Move (W/A/S/D to move, Q to quit): ").upper()
    if move == "Q":
        print("Exiting the game.")
        break

    if move == "W" and player.pos[1] > 0:
        player.move(0, -1)
    elif move == "S" and player.pos[1] < game_map.height - 1:
        player.move(0, 1)
    elif move == "A" and player.pos[0] > 0:
        player.move(-1, 0)
    elif move == "D" and player.pos[0] < game_map.width - 1:
        player.move(1, 0)
    else:
        print("Invalid move or out of bounds!")

    game_map.update_map(player.pos, player.marker)
    #reset players pos after each map