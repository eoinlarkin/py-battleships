from blessed import Terminal
from random import randint
import boards

term = Terminal()

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
    ship_lengths = list(ship_data.values())
    for i in range(len(ship_lengths)):
        for j in range(ship_lengths[i]):
            ship_coords[chr(j+97)+str(i)] = "S" + str(i)
    return ship_coords

# Initializing variables to play game
ship_data = {'S0':2, 'S1':3, 'S2':4}

ship_hits_player = {'S0': 0, 'S1': 0, 'S2':0}

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
    print(term.move(60,0))
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
        with term.location():
            print(term.move(15,0) + "It's a hit!")
        ship_name = coords_ships[target]
        ship_hits[ship_name] += 1
        if ship_hits[ship_name] == ship_data[ship_name]:
            print(f"Ship {ship_name} is sunk...!")
    else:
        print("It's a miss....")

def check_victory(ship_hits, ship_data):
    """
    Function to check if player is victorious
    Sum up the total number of successful hits from the ship hit register 
    and checks this against the total ship footprint
    """
    return sum(ship_hits.values()) == sum(ship_data.values())


# *************************************************
# Splash Screen
# *************************************************

# prints content to the screen
print(term.home + term.clear + term.move_y(term.height - term.height // 5))
print(term.black_on_darkgreen(term.center('press any key to continue.')))
with term.cbreak(), term.hidden_cursor():
    inp = term.inkey()
print(term.home + term.clear)


# Steps to Execute Game:

# generate empty board
board = draw_board(10)

# place ships
coords_ships_player = place_ships(ship_data)
coords_ships_computer = place_ships(ship_data)

    # add ships to board
    # Loop:
        # print board
        # ask user for target
        # update dict of targets
        # update dict of ships
        # redraw board

while not check_victory(ship_hits_player, ship_data):
    target = get_target(coords_targets_player)
    check_hit(target,coords_ships_player,ship_hits_player)
    print(ship_hits_player)


#board = draw_board(10)
#print(board)
#print('Ship hits for player\n')
#print(ship_hits_player)
#target = get_target(coords_targets_player)
#print(coords_targets_player)
#print(coords_ships_player)
#check_hit(target,coords_ships_player,ship_hits_player)
#print(ship_hits_player)
#print(check_victory(ship_hits_player, ship_data))

print('You have defeated the computer!')


