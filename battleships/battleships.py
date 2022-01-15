#! /usr/bin/env python3
import random


class board():
    # pylint: disable=too-many-instance-attributes
    """
    Class to store the game board and associated data model
    """

    def __init__(self):
        self.ship_data = {
            'p1': {'S1': 2, 'S2': 3, 'S3': 4},
            'p2': {'S1': 2, 'S2': 3, 'S3': 4}
        }

        self.ship_hits = {
            'p1': {'S1': 0, 'S2': 0, 'S3': 0},
            'p2': {'S1': 0, 'S2': 0, 'S3': 0}
        }

        self.ship_integ = {
            'p1': {'S1': 100, 'S2': 100, 'S3': 100},
            'p2': {'S1': 100, 'S2': 100, 'S3': 100}
        }

        self.coords_targets = {'p1': {}, 'p2': {}}
        self.type = {'p1': "player", 'p2': "computer"}
        self.coords_ships = {'p1': {}, 'p2': {}}
        self.coords_board = {'p1': [], 'p2': []}
        self.active_target = {'p1': (), 'p2': ()}
        self.active_target_invalid = {'p1': False, 'p2': False}
        self.active_target_previous = {'p1': False, 'p2': False}
        self.active_target_status = {'p1': [], 'p2': []}
        self.active_target_loc = {'p1': [], 'p2': []}
        self.victory = {'p1': False, 'p2': False}
        self.loc = {'p1':{},'p2':{}}
        self.loc_ships = {'p1': {'S1': {'direction': "t2b", 'size': 2, 'start': 'A1'},
                                 'S2': {'direction': "t2b", 'size': 3, 'start': 'A2'},
                                 'S3': {'direction': "t2b", 'size': 4, 'start': 'A3'}},
                          'p2': {'S1': {'direction': "t2b", 'size': 2, 'start': 'A1'},
                                 'S2': {'direction': "t2b", 'size': 3, 'start': 'A2'},
                                 'S3': {'direction': "t2b", 'size': 4, 'start': 'A3'}}
                          }

    def gen_loc(self,player,size, start_x, start_y, ygap, xgap):
        for y in range(size):
            for x in range(size):
                self.loc[player][chr(y+65)+str(x+1)] = [start_x + x*xgap, start_y+y*ygap]

    def place_ships(self):
        """
        Randomly placing the ships on the game board
        """
        for player in self.coords_ships:
            number_ships = len(self.ship_data[player])
            for i in range(number_ships):
                length_ships = list(self.ship_data[player].values()) 
                for j in range(length_ships[i]):
                    self.coords_ships[player][chr(j+65)+str(i+1)] = "S" + str(i+1)

    def gen_board(self, gridsize):
        """
        Generates an empty dictionary of all potential targets
        """
        for player in self.coords_board:
            for i in range(gridsize):
                for j in range(gridsize):
                    self.coords_board[player].append(chr(i+65)+str(j+1))


def target_computer(gameboard):
    """
    Randomly generates a target for the computer
    Validation done to make sure target has not already been selected
    """
    target = random.choice(list(gameboard.coords_board['p1'].keys()))
    # target = random.choice(list(gameboard.coords_ships['p1'].keys())) # for testing
    while (target in gameboard.coords_targets['p2']):
        # selecting a new target if already chosen
        target = random.choice(list(gameboard.coords_board['p1'].keys()))
        # target = random.choice(list(gameboard.coords_ships['p1'].keys())) # for testing
    # adding the value to the dictionary of shots
    gameboard.active_target['p2'] = target
    # adding the value to the dictionary of shots
    gameboard.coords_targets['p2'][target] = 'X'


def validate_target(gameboard):
    """
    Requests target from user and performs input validation
    Check is completed to see if the target has already been selected
    Target is also appended to the dictionary of prior targets
    """
    gameboard.active_target_invalid['p1'] = False
    gameboard.active_target_previous['p1'] = False
    if gameboard.active_target['p1'] not in gameboard.coords_board['p2']:
        gameboard.active_target_invalid['p1'] = True
    if gameboard.active_target['p1'] in gameboard.coords_targets['p1']:
        gameboard.active_target_previous['p1'] = True
    else:
        # adding the value to the dictionary of shots
        gameboard.coords_targets['p1'][gameboard.active_target['p1']] = 'X'


def check_target_hit(active_player, gameboard):
    """
    Checks if the target from the most recent shot by
    the active player has registered a hit
    """
    if active_player == 'p1':
        player, opponent = 'p1', 'p2'
    else:
        player, opponent = 'p2', 'p1'

    target = gameboard.active_target[player]
    gameboard.active_target_loc[player] = gameboard.loc[opponent][target]

    if target in gameboard.coords_ships[opponent].keys():
        gameboard.active_target_status[player] = 'hit'
        ship_name = gameboard.coords_ships[opponent][gameboard.active_target[player]]
        gameboard.ship_hits[opponent][ship_name] += 1
        update_ship_integ(gameboard)
    else:
        gameboard.active_target_status[player] = 'miss'


def update_ship_integ(gb):
    """
    Update the ship integrity status
    Function directly updates the ship_integ for the board class
    """
    for player in gb.ship_integ:
        for ship in gb.ship_integ[player]:
            damage = int(
                100 * (gb.ship_hits[player][ship] / gb.ship_data[player][ship]))
            gb.ship_integ[player][ship] = max(100 - damage, 0)


def check_victory(gameboard):
    """
    Function to check if player is victorious. Returns True or False.
    Sum up the total number of successful hits from the ship hit register
    and checks this against the total ship footprint
    """
    victoryp1 = (sum(gameboard.ship_hits['p2'].values()) == sum(
        gameboard.ship_data['p2'].values()))
    victoryp2 = (sum(gameboard.ship_hits['p1'].values()) == sum(
        gameboard.ship_data['p1'].values()))
    gameboard.victory['p1'] = victoryp1
    gameboard.victory['p2'] = victoryp2
    return victoryp1 or victoryp2


gb = board()
gb.gen_board(8)
gb.place_ships()
#print(gb.coords_board)
print(gb.coords_ships)
print('\n\n')
gb.gen_loc('p1',size=8, start_x=21, start_y=4, ygap=2, xgap=4)
print(gb.loc)