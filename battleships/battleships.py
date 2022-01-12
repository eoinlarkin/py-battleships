#! /usr/bin/env python3


import random
from time import sleep
import battleships.print_term as print_term
#from blessed import Terminal
#term = Terminal()

BOARD_X = 1
BOARD_Y = 1
TERM_INPUT_LINE = 41
TERM_STATUS_LINE = 43

class board():
    def __init__(self):
        self.p1_ship_data = {'S1':2, 'S2':3, 'S3':4}
        self.p1_ship_hits = {'S1': 0, 'S2': 0, 'S3':0}
        self.p1_coords_targets = {}
        self.p1_type = 'p1'
        self.p1_coords_ships = {}
        self.p1_coords_board = {}
        self.p1_active_target = ()
        self.p1_active_target_invalid = False
        self.p1_active_target_previous = False
        self.p1_active_target_status = []

        self.p2_ship_data = {'S1':2, 'S2':3, 'S3':4}
        self.p2_ship_hits = {'S1': 0, 'S2': 0, 'S3':0}
        self.p2_coords_targets = {}
        self.p2_type = 'p2'
        self.p2_coords_ships = {}
        self.p2_coords_board = {}
        self.p2_active_target = ()
        self.p2_active_target_invalid = False
        self.p2_active_target_previous = False
        self.p2_active_target_status = []


        self.p1_termLocations = {'A1': [19,4],'A2': [23,4],'A3': [27,4],'A4': [31,4],'A5': [35,4],'A6': [39,4],'A7': [43,4],'A8': [47,4],'B1': [19,6],'B2': [23,6],'B3': [27,6],'B4': [31,6],'B5': [35,6],'B6': [39,6],'B7': [43,6],'B8': [47,6],'C1': [19,8],'C2': [23,8],'C3': [27,8],'C4': [31,8],'C5': [35,8],'C6': [39,8],'C7': [43,8],'C8': [47,8],'D1': [19,10],'D2': [23,10],'D3': [27,10],'D4': [31,10],'D5': [35,10],'D6': [39,10],'D7': [43,10],'D8': [47,10],'E1': [19,12],'E2': [23,12],'E3': [27,12],'E4': [31,12],'E5': [35,12],'E6': [39,12],'E7': [43,12],'E8': [47,12],'F1': [19,14],'F2': [23,14],'F3': [27,14],'F4': [31,14],'F5': [35,14],'F6': [39,14],'F7': [43,14],'F8': [47,14],'G1': [19,16],'G2': [23,16],'G3': [27,16],'G4': [31,16],'G5': [35,16],'G6': [39,16],'G7': [43,16],'G8': [47,16],'H1': [19,18],'H2': [23,18],'H3': [27,18],'H4': [31,18],'H5': [35,18],'H6': [39,18],'H7': [43,18],'H8': [47,18]}
        
        self.p2_termLocations = {'A1': [47,24],'A2': [51,24],'A3': [55,24],'A4': [59,24],'A5': [63,24],'A6': [67,24],'A7': [71,24],'A8': [76,24],'B1': [47,26],'B2': [51,26],'B3': [55,26],'B4': [59,26],'B5': [63,26],'B6': [67,26],'B7': [71,26],'B8': [76,26],'C1': [47,28],'C2': [51,28],'C3': [55,28],'C4': [59,28],'C5': [63,28],'C6': [67,28],'C7': [71,28],'C8': [76,28],'D1': [47,30],'D2': [51,30],'D3': [55,30],'D4': [59,30],'D5': [63,30],'D6': [67,30],'D7': [71,30],'D8': [76,30],'E1': [47,32],'E2': [51,32],'E3': [55,32],'E4': [59,32],'E5': [63,32],'E6': [67,32],'E7': [71,32],'E8': [76,32],'F1': [47,34],'F2': [51,34],'F3': [55,34],'F4': [59,34],'F5': [63,34],'F6': [67,34],'F7': [71,34],'F8': [76,34],'G1': [47,36],'G2': [51,36],'G3': [55,36],'G4': [59,36],'G5': [63,36],'G6': [67,36],'G7': [71,36],'G8': [76,36],'H1': [47,38],'H2': [51,38],'H3': [55,38],'H4': [59,38],'H5': [63,38],'H6': [67,38],'H7': [71,38],'H8': [47,38]}


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
    target = random.choice(list(board.p1_coords_board.keys()))
    while (target in board.p2_coords_targets):
        target = random.choice(list(board.p1_coords_board.keys())) #selecting a new target if already chosen
    board.p2_active_target = target # adding the value to the dictionary of shots
    board.p2_coords_targets[target] = 'X' # adding the value to the dictionary of shots


def get_target_player(board):
    """
    Requests target from user and performs input validation
    Check is completed to see if the target has already been selected
    Target is also appended to the dictionary of prior targets
    """ 
    board.p1_active_target_invalid = False
    board.p1_active_target_previous = False  
    board.p1_active_target = print_term.print_target_request() 
    if board.p1_active_target not in board.p2_coords_board:
        board.p1_active_target_invalid = True
    if board.p1_active_target in board.p1_coords_targets:
        board.p1_active_target_previous = True
    else:
        board.p1_coords_targets[board.p1_active_target] = 'X' # adding the value to the dictionary of shots



def check_target_hit(active_player, board):

    if active_player == board.p1_type: 
        if board.p1_active_target in board.p2_coords_ships.keys():
            print_term.confirm_hit(0, TERM_STATUS_LINE,'hit')
            print_term.update_board(board.p2_termLocations[board.p1_active_target][0],board.p2_termLocations[board.p1_active_target][1],'hit')
            ship_name = board.p2_coords_ships[board.p1_active_target]
            board.p2_ship_hits[ship_name] += 1
            if board.p2_ship_hits[ship_name] == board.p2_ship_data[ship_name]:
                sleep(1) # Time in seconds
                print_term.confirm_ship_sunk(0,TERM_STATUS_LINE,ship_name)
        else:
            print_term.confirm_hit(0, TERM_STATUS_LINE,'miss')
            print_term.update_board(board.p2_termLocations[board.p1_active_target][0],board.p2_termLocations[board.p1_active_target][1],'miss')

    else: 
        if board.p2_active_target in board.p1_coords_ships.keys():
            print_term.update_board(board.p1_termLocations[board.p2_active_target][0],board.p1_termLocations[board.p2_active_target][1],'hit')
            ship_name = board.p2_coords_ships[board.p1_active_target]
            board.p2_ship_hits[ship_name] += 1
            if board.p2_ship_hits[ship_name] == board.p2_ship_data[ship_name]:
                sleep(1) # Time in seconds
                #print_term.confirm_ship_sunk(0,TERM_STATUS_LINE,ship_name)
        else:
            print_term.update_board(board.p1_termLocations[board.p2_active_target][0],board.p1_termLocations[board.p2_active_target][1],'miss')
      

def check_victory(board):
    """
    Function to check if player is victorious
    Sum up the total number of successful hits from the ship hit register 
    and checks this against the total ship footprint
    """
    return sum(board.p2_ship_hits.values()) == sum(board.p2_ship_data.values())


def rungame(board):
    import battleships.print_term as print_term
    print_term.intro()
    print_term.boards()

    board.p1_coords_ships = place_ships(board.p1_ship_data)
    board.p1_coords_board = draw_board(8)

    board.p2_coords_ships = place_ships(board.p2_ship_data)
    board.p2_coords_board = draw_board(8)

    while not check_victory(board):
        
        get_target_player(board)
        while board.p1_active_target_invalid or board.p1_active_target_previous:
            if board.p1_active_target_invalid:
                print_term.target_invalid(0, 43)
            if board.p1_active_target_previous:
                print_term.target_previously_selected(0, 43)
            get_target_player(board)

        check_target_hit('p1',board)
        target_computer(board)
        check_target_hit('p2',board)
        
    print(term.clear+term.move(TERM_STATUS_LINE,0) + term.center('You have defeated the computer!'))


