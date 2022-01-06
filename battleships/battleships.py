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
def gen_dict(gridsize):
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

print(place_ships([2,4,5]))


hits_player = gen_dict(10)
hits_computer = gen_dict(10)

def check_input(value):
    return False

def get_input():
    hit = input('Select your next target:')

    while check_input(hit):
        hit = input('Invalid coordinate selected; please try again...!') 

target = get_input()