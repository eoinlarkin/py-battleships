from blessed import Terminal
from random import randint
import boards

scores = {"computer": 0, "player": 0}

class board:
    def __init__(self, size, num_ships, name):
        self.size = size
        #self.board == [["." for z in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.guesses = []
        self.ships=[]

print(boards.mini_board)

# Code for generating a coordinate dictionary
def draw_board(gridsize):
    """
    Generates an empty dictionary of targets for targeting
    """
    coords = {}
    for i in range(gridsize):
        coords[chr(i+97)+str(i)] = ""
    return coords

def place_ships(ship_data):
    ship_coords = {}
    for i in range(len(ship_data)):
        for j in range(ship_data[i]):
            ship_coords[chr(j+97)+str(i)] = "S" + str(i)
    return ship_coords

# Initializing variables to play game
ship_data = {'S0':2, 'S1':3, 'S2':4}
coords_ships_player = place_ships([2,4,5])
ship_hits_player = {'S0': 0, 'S1': 0, 'S2':0}
coords_ships_computer = place_ships([2,4,5])
ship_hits_computer = {'S0': 0, 'S1': 0, 'S2':0}
coords_targets_player = {}
coords_targets_computer = {}

def check_input(value):
    return False

def get_target(coords_dict):
    """
    Requests target from user and performs input validation
    Check is completed to see if the target has already been selected
    Target is also appended to the dictionary of prior targets
    """
    target = input('Select your next target:')

    while check_input(target):
        print('Invalid coordinate selected; please try again...!')
        target = input('Select your next target:') 
    
    while target in coords_dict:
        print('This target has already been selected; please select an alternative target.')
        target = input('Select your next target:') 
    coords_dict[target] = 'X' # adding the value to the dictionary of shots
    return target

def check_hit(target, coords_ships, ship_hits):
    if target in coords_ships:
        print("It's a hit!")
        ship_name = coords_ships[target]
        ship_hits[ship_name] += 1
    else:
        print("It's a miss....")

def check_victory(ship_hits, ship_data):
    """
    Function to check if player is victorious
    Sum up the total number of successful hits from the ship hit register 
    and checks this against the total ship footprint
    """
    return ship_hits.values() == ship_data.values()


# Steps to Execute Game:
    # generate empty board
    # place ships
    # add ships to board
    # Loop:
        # print board
        # ask user for target
        # update dict of targets
        # update dict of ships
        # redraw board


board = draw_board(10)
print(board)
print('Ship hits for player\n')
print(ship_hits_player)
target = get_target(coords_targets_player)
print(coords_targets_player)
print(coords_ships_player)
check_hit(target,coords_ships_player,ship_hits_player)
print(ship_hits_player)
print(check_victory(ship_hits_player, ship_data))