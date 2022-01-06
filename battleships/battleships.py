from blessed import Terminal
from random import randint
import boards

scores = {"computer": 0, "player": 0}

class game:
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board == [["." for z in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.guesses = []
        self.ships=[]

print(boards.mini_board)


def gen_coord_log(size):
    coords = {}
    for i in range(size):
        coords[chr(i+97)+str(i)] = ""
    return coords

print(gen_coord_log(4))