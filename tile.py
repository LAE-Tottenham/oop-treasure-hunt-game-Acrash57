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
enemy_icon = Tile("E", ANSI_RED)