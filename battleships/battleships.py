#! /usr/bin/env python3
"""
Module to define the Board class; this contains all
relevant data attributes required to run the Battleship game
"""
import random


class Board():
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=consider-using-dict-items
    """
    Class to store the game board and associated data model
    """

    def __init__(self):
        self.active_player = {'p1': False, 'p2': False}

        # Coordinate objects
        self.coords_board = {'p1': [], 'p2': []}
        self.coords_targets = {'p1': [], 'p2': []}
        self.coords_ships = {'p1': {}, 'p2': {}}

        # Objects detailing ship sizes, hits and status
        self.ship_size = {
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

        self.ship_sunk = {
            'p1': {'S1': False, 'S2': False, 'S3': False},
            'p2': {'S1': False, 'S2': False, 'S3': False}
        }

        # Objects recording status of the active target
        self.active_target = {'p1': "", 'p2': ""}
        self.active_target_invalid = {'p1': False, 'p2': False}
        self.active_target_previous = {'p1': False, 'p2': False}
        self.active_target_status = {'p1': [], 'p2': []}
        self.active_target_shipname = {'p1': '', 'p2': ''}
        self.active_target_loc = {'p1': [], 'p2': []}

        # Objects recording ship locaation
        self.loc = {'p1': {}, 'p2': {}}
        self.loc_ships = {'p1': {'S1': {'direction': "t2b", 'size': 2, 'start': 'A1'},
                                 'S2': {'direction': "t2b", 'size': 3, 'start': 'A2'},
                                 'S3': {'direction': "t2b", 'size': 4, 'start': 'A3'}},
                          'p2': {'S1': {'direction': "t2b", 'size': 2, 'start': 'A1'},
                                 'S2': {'direction': "t2b", 'size': 3, 'start': 'A2'},
                                 'S3': {'direction': "t2b", 'size': 4, 'start': 'A3'}}
                          }
        # obejct to record whether plany is victorious
        self.victory = {'p1': False, 'p2': False}

    def gen_loc(self, player, size, start_x, start_y, ygap, xgap):
        """"
        Generates the mapping table to link the board grid coordinates
        and the relevant positions on the terminal screen
        """
        for y_coord in range(size):
            for x_coord in range(size):
                self.loc[player][chr(y_coord+65)+str(x_coord+1)
                                 ] = [start_x + x_coord*xgap, start_y+y_coord*ygap]

    def place_ships(self):
        """
        Randomly placing the ships on the game board
        """
        for player in self.coords_ships:
            number_ships = len(self.ship_size[player])
            for i in range(number_ships):
                length_ships = list(self.ship_size[player].values())
                for j in range(length_ships[i]):
                    self.coords_ships[player][chr(
                        j+65)+str(i+1)] = "S" + str(i+1)

    def gen_board(self, gridsize):
        """
        Generates an empty dictionary of all potential targets
        """
        for player in self.coords_board:
            for i in range(gridsize):
                for j in range(gridsize):
                    self.coords_board[player].append(chr(i+65)+str(j+1))

    def check_victory(self):
        """
        Function to check if player is victorious. Returns True or False.
        Sum up the total number of successful hits from the ship hit register
        and checks this against the total ship footprint
        """
        victoryp1 = (sum(self.ship_hits['p2'].values()) == sum(
            self.ship_size['p2'].values()))
        victoryp2 = (sum(self.ship_hits['p1'].values()) == sum(
            self.ship_size['p1'].values()))
        self.victory['p1'] = victoryp1
        self.victory['p2'] = victoryp2
        return victoryp1 or victoryp2

    def update_ship_integ(self):
        """
        Update the ship integrity status
        Function directly updates the ship_integ for the board class
        """
        for player in self.ship_integ:
            for ship in self.ship_integ[player]:
                damage = int(
                    100 * (self.ship_hits[player][ship] / self.ship_size[player][ship]))
                self.ship_integ[player][ship] = max(100 - damage, 0)

    def generate_target(self, active_player):
        """
        Randomly generates a target for the computer
        Validation done to make sure target has not already been selected
        """
        if active_player == 'p1':
            player, opponent = 'p1', 'p2'
        else:
            player, opponent = 'p2', 'p1'

        target = random.choice(self.coords_board[opponent])
        while target in self.coords_targets[player]:
            # selecting a new target if already chosen
            target = random.choice(self.coords_board[opponent])
        # adding the value to the dictionary of shots
        self.active_target[player] = target

    def update_ship_sunk_status(self):
        """
        Checks the active target and updates the ship status if it
        has been sunk
        """
        for player in self.ship_sunk:
            for ship in self.ship_sunk[player]:
                status = self.ship_hits[player][ship] == self.ship_size[player][ship]
                self.ship_sunk[player][ship] = status

    def validate_target(self):
        """
        Requests target from user and performs input validation
        Check is completed to see if the target has already been selected
        Target is also appended to the dictionary of prior targets
        """
        self.active_target_invalid['p1'] = False
        self.active_target_previous['p1'] = False
        if self.active_target['p1'] not in self.coords_board['p2']:
            self.active_target_invalid['p1'] = True
        if self.active_target['p1'] in self.coords_targets['p1']:
            self.active_target_previous['p1'] = True
        else:
            # adding the value to the dictionary of shots
            self.coords_targets['p1'].append(self.active_target['p1'])

    def check_target_hit(self, active_player):
        """
        Checks if the target from the most recent shot by
        the active player has registered a hit
        """
        if active_player == 'p1':
            player, opponent = 'p1', 'p2'
        else:
            player, opponent = 'p2', 'p1'

        target = self.active_target[player]
        self.active_target_loc[player] = self.loc[opponent][target]

        if target in self.coords_ships[opponent]:
            self.active_target_status[player] = 'hit'
            ship_name = self.coords_ships[opponent][self.active_target[player]]
            self.active_target_shipname[player] = ship_name
            self.ship_hits[opponent][ship_name] += 1
            self.update_ship_integ()
        else:
            self.active_target_status[player] = 'miss'
