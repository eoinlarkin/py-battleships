#! /usr/bin/env python3
import random
from time import sleep
import battleships.termprint as termprint

class board():
    def __init__(self):
        self.ship_data = {
                          'p1':{'S1':2, 'S2':3, 'S3':4},
                          'p2':{'S1':2, 'S2':3, 'S3':4}
                          }
                          
        self.ship_hits = {
                        'p1':{'S1': 0, 'S2': 0, 'S3':0},
                        'p2':{'S1': 0, 'S2': 0, 'S3':0}
                        }

        self.coords_targets = {'p1':{}, 'p2':{}}
        self.type = {'p1':"player", 'p2':"computer"}
        self.coords_ships = {'p1':{}, 'p2':{}}
        self.coords_board = {'p1':{}, 'p2':{}}
        self.active_target = {'p1':(), 'p2':()}
        self.active_target_invalid = {'p1':False, 'p2':False}
        self.active_target_previous = {'p1':False, 'p2':False}
        self.active_target_status = {'p1':[], 'p2':[]}
        self.active_target_loc = {'p1':[], 'p2':[]}

        self.loc = {'p1':{'A1': [19,4],'A2': [23,4],'A3': [27,4],'A4': [31,4],'A5': [35,4],'A6': [39,4],'A7': [43,4],'A8': [47,4],'B1': [19,6],'B2': [23,6],'B3': [27,6],'B4': [31,6],'B5': [35,6],'B6': [39,6],'B7': [43,6],'B8': [47,6],'C1': [19,8],'C2': [23,8],'C3': [27,8],'C4': [31,8],'C5': [35,8],'C6': [39,8],'C7': [43,8],'C8': [47,8],'D1': [19,10],'D2': [23,10],'D3': [27,10],'D4': [31,10],'D5': [35,10],'D6': [39,10],'D7': [43,10],'D8': [47,10],'E1': [19,12],'E2': [23,12],'E3': [27,12],'E4': [31,12],'E5': [35,12],'E6': [39,12],'E7': [43,12],'E8': [47,12],'F1': [19,14],'F2': [23,14],'F3': [27,14],'F4': [31,14],'F5': [35,14],'F6': [39,14],'F7': [43,14],'F8': [47,14],'G1': [19,16],'G2': [23,16],'G3': [27,16],'G4': [31,16],'G5': [35,16],'G6': [39,16],'G7': [43,16],'G8': [47,16],'H1': [19,18],'H2': [23,18],'H3': [27,18],'H4': [31,18],'H5': [35,18],'H6': [39,18],'H7': [43,18],'H8': [47,18]},
        'p2':{'A1': [47,24],'A2': [51,24],'A3': [55,24],'A4': [59,24],'A5': [63,24],'A6': [67,24],'A7': [71,24],'A8': [76,24],'B1': [47,26],'B2': [51,26],'B3': [55,26],'B4': [59,26],'B5': [63,26],'B6': [67,26],'B7': [71,26],'B8': [76,26],'C1': [47,28],'C2': [51,28],'C3': [55,28],'C4': [59,28],'C5': [63,28],'C6': [67,28],'C7': [71,28],'C8': [76,28],'D1': [47,30],'D2': [51,30],'D3': [55,30],'D4': [59,30],'D5': [63,30],'D6': [67,30],'D7': [71,30],'D8': [76,30],'E1': [47,32],'E2': [51,32],'E3': [55,32],'E4': [59,32],'E5': [63,32],'E6': [67,32],'E7': [71,32],'E8': [76,32],'F1': [47,34],'F2': [51,34],'F3': [55,34],'F4': [59,34],'F5': [63,34],'F6': [67,34],'F7': [71,34],'F8': [76,34],'G1': [47,36],'G2': [51,36],'G3': [55,36],'G4': [59,36],'G5': [63,36],'G6': [67,36],'G7': [71,36],'G8': [76,36],'H1': [47,38],'H2': [51,38],'H3': [55,38],'H4': [59,38],'H5': [63,38],'H6': [67,38],'H7': [71,38],'H8': [47,38]}}

        def gen_loc(player,size, start_col, start_row, rowgap, colgap):
            out = {player:{}}
            for y in range(size):
                for x in range(size):
                    out[player][chr(y+65)+str(x+1)] = [start_col +x*colgap,start_row+y*rowgap]
            return out

gen_loc('p1',8,19,4,4,2)

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
    target = random.choice(list(board.coords_board['p1'].keys()))
    while (target in board.coords_targets['p2']):
        target = random.choice(list(board.coords_board['p1'].keys())) #selecting a new target if already chosen
    board.active_target['p2'] = target # adding the value to the dictionary of shots
    board.coords_targets['p2'][target] = 'X' # adding the value to the dictionary of shots


def get_target_player(board):
    """
    Requests target from user and performs input validation
    Check is completed to see if the target has already been selected
    Target is also appended to the dictionary of prior targets
    """ 
    board.active_target_invalid['p1'] = False
    board.active_target_previous['p1'] = False  
    board.active_target['p1'] = termprint.print_target_request() 
    if board.active_target['p1'] not in board.coords_board['p2']:
        board.active_target_invalid['p1'] = True
    if board.active_target['p1'] in board.coords_targets['p1']:
        board.active_target_previous['p1'] = True
    else:
        board.coords_targets['p1'][board.active_target['p1']] = 'X' # adding the value to the dictionary of shots



def check_target_hit(active_player, board):
    if active_player == 'p1':
        player, opponent = 'p1','p2'
    else:
        player, opponent = 'p2','p1'
    
    board.active_target_loc[player] = board.loc[opponent][board.active_target[player]]
 
    if board.active_target[player] in board.coords_ships[opponent].keys():
        board.active_target_status[player] = 'hit'
        ship_name = board.coords_ships[player][board.active_target[player]]
        board.ship_hits[opponent][ship_name] += 1
    else:
        board.active_target_status[player] = 'miss'

def check_victory(board):
    """
    Function to check if player is victorious
    Sum up the total number of successful hits from the ship hit register and checks this against the total ship footprint
    """
    return sum(board.ship_hits['p2'].values()) == sum(board.ship_data['p2'].values())
