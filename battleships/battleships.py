#! /usr/bin/env python3

from blessed import Terminal
import random
from time import sleep

term = Terminal()

class board():
    def __init__(self, type):
        self.ship_data = {'S1':2, 'S2':3, 'S3':4}
        self.ship_hits = {'S1': 0, 'S2': 0, 'S3':0}
        self.coords_targets = {}
        self.type = type
        self.coords_ships = {}
        self.coords_board = {}

        if type == 'player':
            self.termLocations = {'A1': [19,4],'A2': [23,4],'A3': [27,4],'A4': [31,4],'A5': [35,4],'A6': [39,4],'A7': [43,4],'A8': [47,4],'B1': [19,6],'B2': [23,6],'B3': [27,6],'B4': [31,6],'B5': [35,6],'B6': [39,6],'B7': [43,6],'B8': [47,6],'C1': [19,8],'C2': [23,8],'C3': [27,8],'C4': [31,8],'C5': [35,8],'C6': [39,8],'C7': [43,8],'C8': [47,8],'D1': [19,10],'D2': [23,10],'D3': [27,10],'D4': [31,10],'D5': [35,10],'D6': [39,10],'D7': [43,10],'D8': [47,10],'E1': [19,12],'E2': [23,12],'E3': [27,12],'E4': [31,12],'E5': [35,12],'E6': [39,12],'E7': [43,12],'E8': [47,12],'F1': [19,14],'F2': [23,14],'F3': [27,14],'F4': [31,14],'F5': [35,14],'F6': [39,14],'F7': [43,14],'F8': [47,14],'G1': [19,16],'G2': [23,16],'G3': [27,16],'G4': [31,16],'G5': [35,16],'G6': [39,16],'G7': [43,16],'G8': [47,16],'H1': [19,18],'H2': [23,18],'H3': [27,18],'H4': [31,18],'H5': [35,18],'H6': [39,18],'H7': [43,18],'H8': [47,18]}
        elif type == 'computer':
            self.termLocations = {'A1': [47,24],'A2': [51,24],'A3': [55,24],'A4': [59,24],'A5': [63,24],'A6': [67,24],'A7': [71,24],'A8': [76,24],'B1': [47,26],'B2': [51,26],'B3': [55,26],'B4': [59,26],'B5': [63,26],'B6': [67,26],'B7': [71,26],'B8': [76,26],'C1': [47,28],'C2': [51,28],'C3': [55,28],'C4': [59,28],'C5': [63,28],'C6': [67,28],'C7': [71,28],'C8': [76,28],'D1': [47,30],'D2': [51,30],'D3': [55,30],'D4': [59,30],'D5': [63,30],'D6': [67,30],'D7': [71,30],'D8': [76,30],'E1': [47,32],'E2': [51,32],'E3': [55,32],'E4': [59,32],'E5': [63,32],'E6': [67,32],'E7': [71,32],'E8': [76,32],'F1': [47,34],'F2': [51,34],'F3': [55,34],'F4': [59,34],'F5': [63,34],'F6': [67,34],'F7': [71,34],'F8': [76,34],'G1': [47,36],'G2': [51,36],'G3': [55,36],'G4': [59,36],'G5': [63,36],'G6': [67,36],'G7': [71,36],'G8': [76,36],'H1': [47,38],'H2': [51,38],'H3': [55,38],'H4': [59,38],'H5': [63,38],'H6': [67,38],'H7': [71,38],'H8': [47,38]}


def draw_board(gridsize):
    """
    Generates an empty dictionary of all potential targets
    """
    coords = {}
    for i in range(gridsize):
            for j in range(gridsize):
                coords[chr(i+65)+str(j+1)] = ""
    return coords

def place_ships(ship_data):
    ship_coords = {}
    ship_lengths = list(ship_data.values())
    for i in range(len(ship_lengths)):
        for j in range(ship_lengths[i]):
            ship_coords[chr(j+65)+str(i+1)] = "S" + str(i+1)
    return ship_coords


def target_computer(board):
    """
    Randomly generates a target for the computer
    Validation done to make sure target has not already been selected
    """
    target = random.choice(list(board.coords_board.keys()))
    print(target)
    while (target in board.coords_targets):
        target = random.choice(list(board.coords_board.keys())) #selecting a new target if already chosen
    board.coords_targets[target] = 'X' # adding the value to the dictionary of shots
    print(target)
    return target



def target_player(board):
    """
    Requests target from user and performs input validation
    Check is completed to see if the target has already been selected
    Target is also appended to the dictionary of prior targets
    """   
    target = print_target_request()
    while not(target in board.coords_board):
        printTerminal(term.center('Invalid coordinate selected; please try again...!'),0,
        TERM_STATUS_LINE,
        term.black_on_yellow)
        target = print_target_request()
    
    while target in board.coords_targets:
        printTerminal(term.center('This target has already been selected; please select an alternative target.'),0,
        TERM_STATUS_LINE,
        term.black_on_yellow)
        target = print_target_request()
    board.coords_targets[target] = 'X' # adding the value to the dictionary of shots
    return target

def check_hit(target, board): 
    if target in board.coords_ships:
        with term.location():
            printTerminal(term.center("It's a hit!"), 0, TERM_STATUS_LINE, term.yellow_on_black)
            printTerminal('X',board.termLocations[target][0],board.termLocations[target][1],term.red)
        ship_name = board.coords_ships[target]
        board.ship_hits[ship_name] += 1
        if board.ship_hits[ship_name] == board.ship_data[ship_name]:
            sleep(1) # Time in seconds
            printTerminal(term.center(f"Ship {ship_name} is sunk...!"), 0, TERM_STATUS_LINE, term.black_on_green)
    else:
        printTerminal(term.center("It's a miss......"), 0, TERM_STATUS_LINE, term.white_on_red)
        printTerminal('O',board.termLocations[target][0],board.termLocations[target][1],term.blue)

def check_victory(board):
    """
    Function to check if player is victorious
    Sum up the total number of successful hits from the ship hit register 
    and checks this against the total ship footprint
    """
    return sum(board.ship_hits.values()) == sum(board.ship_data.values())


def printTerminal(text, xcoords, ycoords, color):
    term.home
    with term.location(x=xcoords, y=ycoords):
       print(color + text)

def print_target_request():
    print(term.move(TERM_INPUT_LINE,0)+term.normal)
    target = input(term.white_on_blue + term.center('Select your next target:')+term.move(TERM_INPUT_LINE+1,58)+term.normal)
    return target

def clearTerminal():
    print(term.home + term.clear)


# *************************************************
# Splash Screen
# *************************************************
TERM_INPUT_LINE = 41
TERM_STATUS_LINE = 43
BOARD_X = 1
BOARD_Y = 1


def print_boards():
    import battleships.layout as layout
    with term.location():
        print(term.home + term.move_xy(1, 0)  + term.green + layout.player_board)
    with term.location():
        print(term.home + term.move_xy(1, 20)  + term.orange + layout.computer_board)


def print_intro():
    import battleships.layout as layout
    clearTerminal()
    printTerminal(term.center(layout.logo), 1,5,term.orangered)
    printTerminal(term.center('press and key to continue'),0,30,term.black_on_green)
    with term.cbreak(), term.hidden_cursor():
        inp = term.inkey()
    clearTerminal()


def rungame(player_board, computer_board):
    print_intro()
    print_boards()

    player_board.coords_ships = place_ships(player_board.ship_data)
    player_board.coords_board = draw_board(8)

    computer_board.coords_ships = place_ships(computer_board.ship_data)
    computer_board.coords_board = draw_board(8)

    while not check_victory(computer_board):
        target = target_player(computer_board)
        print(term.move(0,0) + target)
        check_hit(target,computer_board)
        target = target_computer(player_board)
        print(term.move(0,0) + target)
        check_hit(target,player_board)
        
    print(term.clear+term.move(TERM_STATUS_LINE,0) + term.center('You have defeated the computer!'))


# Testing Code:
""" player_board = board('player')
computer_board = board('computer')
player_board.coords_ships = place_ships(player_board.ship_data)
player_board.coords_board = draw_board(8)

computer_board.coords_ships = place_ships(computer_board.ship_data)
computer_board.coords_board = draw_board(8) """

#target = target_computer(player_board)
#print(target)

# print('Values in board:')
# for k,v in computer_board.coords_board.items():
#     print(k, v)


# target = random.choice(list(player_board.coords_board.keys()))
# print(target)

# print('Checking if target is list of previously selected targets:')
# print(target in player_board.coords_targets)

# print('Adding target to list of targets')
# player_board.coords_targets[target] = 'X'

# print('Values in target:')
# for k,v in player_board.coords_targets.items():
#     print(k, v)






#print(target)

#target = random.choice(list(board.coords_board.keys()))
#while not(target in board.coords_targets):
#    target = random.choice(list(board.coords_board.keys()))
# board.coords_targets[target] = 'X' # adding the value to the dictionary of shots
# return target

### Testing term coordinates:

# printTerminal('a',termLocations['A1'][0],termLocations['A1'][1],term.red)
# printTerminal('B',termLocations['A2'][0],termLocations['A2'][1],term.red)
# printTerminal('C',termLocations['A3'][0],termLocations['A3'][1],term.red)
# printTerminal('0',termLocations['A4'][0],termLocations['A4'][1],term.red)
# printTerminal('0',termLocations['A5'][0],termLocations['A5'][1],term.red)
# printTerminal('0',termLocations['A6'][0],termLocations['A6'][1],term.red)
# printTerminal('0',termLocations['A7'][0],termLocations['A7'][1],term.red)
# printTerminal('0',termLocations['A8'][0],termLocations['A8'][1],term.red)


# printTerminal('0',termLocations['B1'][0],termLocations['B1'][1],term.red)
# printTerminal('0',termLocations['B2'][0],termLocations['B2'][1],term.red)
# printTerminal('0',termLocations['B3'][0],termLocations['B3'][1],term.red)
# printTerminal('0',termLocations['B4'][0],termLocations['B4'][1],term.red)
# printTerminal('0',termLocations['B5'][0],termLocations['B5'][1],term.red)
# printTerminal('0',termLocations['B6'][0],termLocations['B6'][1],term.red)
# printTerminal('0',termLocations['B7'][0],termLocations['B7'][1],term.red)
# printTerminal('0',termLocations['B8'][0],termLocations['B8'][1],term.red)

# printTerminal('0',termLocations['G1'][0],termLocations['G1'][1],term.red)
# printTerminal('0',termLocations['G2'][0],termLocations['G2'][1],term.red)
# printTerminal('0',termLocations['G3'][0],termLocations['G3'][1],term.red)
# printTerminal('0',termLocations['G4'][0],termLocations['G4'][1],term.red)
# printTerminal('0',termLocations['G5'][0],termLocations['G5'][1],term.red)
# printTerminal('0',termLocations['G6'][0],termLocations['G6'][1],term.red)
# printTerminal('0',termLocations['G7'][0],termLocations['G7'][1],term.red)
# printTerminal('0',termLocations['G8'][0],termLocations['G8'][1],term.red)

# printTerminal('1',termLocations['H1'][0],termLocations['H1'][1],term.red)
# printTerminal('2',termLocations['H2'][0],termLocations['H2'][1],term.red)
# printTerminal('3',termLocations['H3'][0],termLocations['H3'][1],term.red)
# printTerminal('0',termLocations['H4'][0],termLocations['H4'][1],term.red)
# printTerminal('0',termLocations['H5'][0],termLocations['H5'][1],term.red)
# printTerminal('0',termLocations['H6'][0],termLocations['H6'][1],term.red)
# printTerminal('0',termLocations['H7'][0],termLocations['H7'][1],term.red)
# printTerminal('0',termLocations['H8'][0],termLocations['H8'][1],term.red)
