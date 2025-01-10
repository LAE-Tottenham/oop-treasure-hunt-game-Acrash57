from tile import Tile, plains, forest, pine, mountain, water, player_icon, enemy_icon, item_icon
import random
import copy

class Map():
    def __init__(self, given_name, given_width, given_height):
        self.name = given_name
        self.width = given_width
        self.height = given_height
        self.next_places = []
        self.items = []
        self.enemy_list = []
        self.map_items = None
        self.final_map_items = None
        self.generate_map()
        self.generate_patch(2,6,8,forest)
        self.generate_patch(2,5,8,water)
        self.generate_patch(2,7,10,mountain)
        self.generate_patch(3,6,6,pine)
     
    def generate_map(self):
        self.init_map_data = []
        for row in range(self.height):
            row_data = [] 
            for col in range(self.width):
                row_data.append(plains)
            self.init_map_data.append(row_data)
        self.map_data = copy.deepcopy(self.init_map_data)

    def update_map(self, pos, marker_player = player_icon, marker_enemy = enemy_icon, marker_item = item_icon):
        x, y = pos
        self.map_data = copy.deepcopy(self.init_map_data)
        self.map_data[y][x] = marker_player
        for enemy in self.enemy_list:
            self.map_data[enemy.pos[1]][enemy.pos[0]] = marker_enemy
        for item in self.final_map_items:
            print(item.pos) 
            self.map_data[item.pos[1]][item.pos[0]] = marker_item

    def get_items(self):
        item_weights = [50, 50, 30, 30, 15, 15, 5, 5]
        x = random.choices(self.map_items, weights=item_weights, k=3)
        
        for item in x:
            item.set_position()
            print(f"Position of {item.name}: {item.pos}")
        
        self.final_map_items = copy.deepcopy(x)  
        return self.final_map_items
        

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
        print(f"{plains.symbol} = Plain, {mountain.symbol} = Mountain, {forest.symbol} = Forest, {pine.symbol} = Pine, {water.symbol} = Water, {player_icon.symbol} = You, {enemy_icon.symbol} = Enemy, {item_icon.symbol} = Chest")

    def add_next_place(self, place_instance):
        self.next_places.append(place_instance)


    def show_next_places(self):
        print("The possible places you can go to are: ")
        for place in self.next_places:
            print(place.name)
    
    
