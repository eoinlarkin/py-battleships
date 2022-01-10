#! /usr/bin/env python3

from blessed import Terminal
from random import randint

term = Terminal()

scores = {"computer": 0, "player": 0}

class board():
    def __init__(self, type):
        #self.size = size
        #self.board == [["." for z in range(size)] for y in range(size)]
        #self.num_ships = num_ships
        #self.name = name
        #self.guesses = []
        #self.ships=[]
        self.ship_data = {'S0':2, 'S1':3, 'S2':4}
        self.ship_hits = {'S0': 0, 'S1': 0, 'S2':0}
        self.coords_targets = {}
        self.type = type

        if type == 'player':
            self.termLocations = {'A1': [19,4],'A2': [23,4],'A3': [27,4],'A4': [31,4],'A5': [35,4],'A6': [39,4],'A7': [43,4],'A8': [47,4],'B1': [19,6],'B2': [23,6],'B3': [27,6],'B4': [31,6],'B5': [35,6],'B6': [39,6],'B7': [43,6],'B8': [47,6],'C1': [19,8],'C2': [23,8],'C3': [27,8],'C4': [31,8],'C5': [35,8],'C6': [39,8],'C7': [43,8],'C8': [47,8],'D1': [19,10],'D2': [23,10],'D3': [27,10],'D4': [31,10],'D5': [35,10],'D6': [39,10],'D7': [43,10],'D8': [47,10],'E1': [19,12],'E2': [23,12],'E3': [27,12],'E4': [31,12],'E5': [35,12],'E6': [39,12],'E7': [43,12],'E8': [47,12],'F1': [19,14],'F2': [23,14],'F3': [27,14],'F4': [31,14],'F5': [35,14],'F6': [39,14],'F7': [43,14],'F8': [47,14],'G1': [19,16],'G2': [23,16],'G3': [27,16],'G4': [31,16],'G5': [35,16],'G6': [39,16],'G7': [43,16],'G8': [47,16],'H1': [19,18],'H2': [23,18],'H3': [27,18],'H4': [31,18],'H5': [35,18],'H6': [39,18],'H7': [43,18],'H8': [47,18]}
        elif type == 'computer':
            self.termLocations = {'A1': [19,4],'A2': [23,4],'A3': [27,4],'A4': [31,4],'A5': [35,4],'A6': [39,4],'A7': [43,4],'A8': [47,4],'B1': [19,6],'B2': [23,6],'B3': [27,6],'B4': [31,6],'B5': [35,6],'B6': [39,6],'B7': [43,6],'B8': [47,6],'C1': [19,8],'C2': [23,8],'C3': [27,8],'C4': [31,8],'C5': [35,8],'C6': [39,8],'C7': [43,8],'C8': [47,8],'D1': [19,10],'D2': [23,10],'D3': [27,10],'D4': [31,10],'D5': [35,10],'D6': [39,10],'D7': [43,10],'D8': [47,10],'E1': [19,12],'E2': [23,12],'E3': [27,12],'E4': [31,12],'E5': [35,12],'E6': [39,12],'E7': [43,12],'E8': [47,12],'F1': [19,14],'F2': [23,14],'F3': [27,14],'F4': [31,14],'F5': [35,14],'F6': [39,14],'F7': [43,14],'F8': [47,14],'G1': [19,16],'G2': [23,16],'G3': [27,16],'G4': [31,16],'G5': [35,16],'G6': [39,16],'G7': [43,16],'G8': [47,16],'H1': [19,18],'H2': [23,18],'H3': [27,18],'H4': [31,18],'H5': [35,18],'H6': [39,18],'H7': [43,18],'H8': [47,18]}


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
    target = print_target_request()

    while check_input(target):
        printTerminal(term.center('Invalid coordinate selected; please try again...!'),
        termStatus['statusloc'][0],termStatus['statusloc'][1],
        term.black_on_yellow)
        target = input('Select your next target:') 
    
    while target in coords_dict:
        printTerminal(term.center('This target has already been selected; please select an alternative target.'),
        termStatus['statusloc'][0],termStatus['statusloc'][1],
        term.black_on_yellow)


        #print(term.move(TERM_STATUS_LINE,0) + 'This target has already been selected; please #select an alternative target.')
        target = print_target_request()
    coords_dict[target] = 'X' # adding the value to the dictionary of shots
    return target

def check_hit(target, coords_ships, ship_hits):
    if target in coords_ships:
        with term.location():
            printTerminal(term.center("It's a hit!"), 0, TERM_STATUS_LINE, term.yellow_on_black)
            printTerminal('X',termLocations[target][0],termLocations[target][1],term.red)
        ship_name = coords_ships[target]
        ship_hits[ship_name] += 1
        if ship_hits[ship_name] == ship_data[ship_name]:
            print(term.move(TERM_STATUS_LINE-1,0) + f"Ship {ship_name} is sunk...!")
    else:
        printTerminal(term.center("It's a miss......"), 0, TERM_STATUS_LINE, term.white_on_red)
        #print(term.move(TERM_STATUS_LINE,0) + "It's a miss....")
        printTerminal('O',termLocations[target][0],termLocations[target][1],term.blue)

def check_victory(ship_hits, ship_data):
    """
    Function to check if player is victorious
    Sum up the total number of successful hits from the ship hit register 
    and checks this against the total ship footprint
    """
    return sum(ship_hits.values()) == sum(ship_data.values())


def printTerminal(text, xcoords, ycoords, color):
    term.home
    with term.location(x=xcoords, y=ycoords):
       print(color + text)


def print_target_request():
    print(term.move(TERM_INPUT_LINE,0)+term.normal)
    target = input(term.black_on_blue + term.center('Select your next target:')+term.move(TERM_INPUT_LINE+1,58)+term.normal)
    return target



def clearTerminal():
    print(term.home + term.clear)
# *************************************************
# Import Boards
# *************************************************
import battleships.layout as layout


# *************************************************
# Splash Screen
# *************************************************
termLocations = {'A1': [19,4],'A2': [23,4],'A3': [27,4],'A4': [31,4],'A5': [35,4],'A6': [39,4],'A7': [43,4],'A8': [47,4],
'B1': [19,6],'B2': [23,6],'B3': [27,6],'B4': [31,6],'B5': [35,6],'B6': [39,6],'B7': [43,6],'B8': [47,6],
'C1': [19,8],'C2': [23,8],'C3': [27,8],'C4': [31,8],'C5': [35,8],'C6': [39,8],'C7': [43,8],'C8': [47,8],
'D1': [19,10],'D2': [23,10],'D3': [27,10],'D4': [31,10],'D5': [35,10],'D6': [39,10],'D7': [43,10],'D8': [47,10],
'E1': [19,12],'E2': [23,12],'E3': [27,12],'E4': [31,12],'E5': [35,12],'E6': [39,12],'E7': [43,12],'E8': [47,12],
'F1': [19,14],'F2': [23,14],'F3': [27,14],'F4': [31,14],'F5': [35,14],'F6': [39,14],'F7': [43,14],'F8': [47,14],
'G1': [19,16],'G2': [23,16],'G3': [27,16],'G4': [31,16],'G5': [35,16],'G6': [39,16],'G7': [43,16],'G8': [47,16],
'H1': [19,18],'H2': [23,18],'H3': [27,18],'H4': [31,18],'H5': [35,18],'H6': [39,18],'H7': [43,18],'H8': [47,18]}


# *************************************************
# Splash Screen
# *************************************************
TERM_INPUT_LINE = 41
TERM_STATUS_LINE = 43
BOARD_X = 1
BOARD_Y = 1

# Code to print terminal locations:
#termStatus = {'inputloc': [0,41], 'statusloc': [0,43]}


# Checks line height and waits for user input
#print(f'Term height is {term.height},Term width is {term.width}')
#with term.cbreak(), term.hidden_cursor():
#    inp = term.inkey()


def rungame():
    # prints splash screen to the screen
    clearTerminal()
    printTerminal(term.center(layout.logo), 1,5,term.orangered)
    printTerminal(term.center('press and key to continue'),0,30,term.black_on_green)

    #term.move_y(term.height - term.height // 5)
    #print(term.black_on_darkgreen(term.center('press any key to continue.')))
    with term.cbreak(), term.hidden_cursor():
        inp = term.inkey()

    clearTerminal()


    # Steps to Execute Game:

    # generate empty board
    board = draw_board(10)

    # print board
    #print(term.move(BOARD_Y, BOARD_X) + layout.player_board)

    with term.location():
        print(term.home + term.move_xy(1, 0)  + term.green + layout.player_board)

    with term.location():
        print(term.home + term.move_xy(1, 20)  + term.orange + layout.computer_board)

    #with term.location(x=1, y=19):
    #    print(term.home+ term.orange + layout.computer_board)

    # print(term.move(BOARD_Y+19, BOARD_X) + layout.computer_board)

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
        # print(ship_hits_player)


    print(term.move(TERM_STATUS_LINE,0) + 'You have defeated the computer!')



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
