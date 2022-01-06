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

def place_ships(lengths):
    ship_coords = {}
    for val in lengths:
        for i in range(val):
            ship_coords[chr(val+97)+str(i)] = "S" + str(val)
    return ship_coords

# Initializing variables to play game
ccords_ships_player = place_ships([2,4,5])
ccords_ships_computer = place_ships([2,4,5])
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
    coords_dict[target] = 'X'
    return target


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
get_target(coords_targets_player)
get_target(coords_targets_player)
print(coords_targets_player)