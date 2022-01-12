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
        self.loc = {}

    @staticmethod
    def gen_loc (size, start_x, start_y, ygap, xgap):
        out = {}
        for y in range(size):
            for x in range(size):
                out[chr(y+65)+str(x+1)] = [start_x +x*xgap,start_y+y*ygap]
        return out

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
