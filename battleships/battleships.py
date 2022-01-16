#! /usr/bin/env python3
"""
battleship.py
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
        self.ship_names_long = {'S1': 'Cruiser',
                                'S2': 'Destroyer',
                                'S3': 'Battleship'}

        # Objects detailing ship sizes, hits and status
        self.ship_size = {
            'p1': {'S1': 2, 'S2': 3, 'S3': 4},
            'p2': {'S1': 2, 'S2': 3, 'S3': 4}
        }

        self.ship_size_order = ['S3', 'S2', 'S1']

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
        self.loc_terminal = {'p1': {}, 'p2': {}}
        self.loc_ships = {'p1': {'S1': {'orient': "", 'size': 0, 'start': ''},
                                 'S2': {'orient': "", 'size': 0, 'start': ''},
                                 'S3': {'orient': "", 'size': 0, 'start': ''}},
                          'p2': {'S1': {'orient': "", 'size': 0, 'start': ''},
                                 'S2': {'orient': "", 'size': 0, 'start': ''},
                                 'S3': {'orient': "", 'size': 0, 'start': ''}}
                          }
        # obejct to record whether plany is victorious
        self.victory = {'p1': False, 'p2': False}

    def gen_terminal_mapping(self, player, size, start_x, start_y, ygap, xgap):
        """"
        Generates the mapping table to link the board grid coordinates
        and the relevant positions on the terminal screen
        """
        for y_coord in range(size):
            for x_coord in range(size):
                self.loc_terminal[player][chr(y_coord+65)+str(x_coord+1)] \
                    = [start_x + x_coord*xgap, start_y+y_coord*ygap]

    def place_ships_test_version(self):
        """
        Function to place ships on board
        All ships are placed in top left quadrant of the board
        Useful for testing the game functionality
        """
        for player in self.coords_ships:
            number_ships = len(self.ship_size[player])
            for i in range(number_ships):
                length_ships = list(self.ship_size[player].values())
                for j in range(length_ships[i]):
                    self.coords_ships[player][chr(
                        j+65)+str(i+1)] = "S" + str(i+1)

    def place_ships(self, player):
        """
        Function to place ships on board
        Starting with the largest ship, the ships are placed
        sequentially on the board. Orientation of ships is randomly decided.
        """
        for ship in self.ship_size_order:
            ship_len = self.ship_size[player][ship]
            check_fit = False

            # while loop will run until the ship
            # from the for loop can be placed
            while not check_fit:
                # randomly setting the orient:
                if int(random.random()+0.5) == 1:
                    orient = 't2b'
                else:
                    orient = 'l2r'

                # randomly setting the starting position
                # from which to draw the ship
                start_pos = random.choice(self.coords_board[player])
                coords = []
                if orient == 't2b':
                    for i in range(ship_len):
                        coords.append(chr(ord(start_pos[0])+i)+start_pos[1])
                if orient == 'l2r':
                    for i in range(ship_len):
                        coords.append(start_pos[0]+str(int(start_pos[1])+i))

                # checking the fit; the ship needs to fit in
                # both the board  and not occupy an existing gird
                # location taken by another ship
                board_coords = self.coords_board[player]
                ship_coords = self.coords_ships[player].keys()
                check_fit = all(c in board_coords for c in coords) and \
                    not(any(c in ship_coords for c in coords))

                # if the ship fits it is added to the dictionary of coordinates
                if check_fit:
                    for c in coords:
                        self.coords_ships[player][c] = ship
                    self.loc_ships[player][ship]['orient'] = orient
                    self.loc_ships[player][ship]['size'] = ship_len
                    self.loc_ships[player][ship]['start'] = start_pos

    def gen_target_list(self, gridsize):
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
                num_hits = self.ship_hits[player][ship]
                ship_size = self.ship_size[player][ship]
                damage = int(100 * num_hits / ship_size)
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
                status = self.ship_hits[player][ship] == \
                    self.ship_size[player][ship]
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
        self.active_target_loc[player] = self.loc_terminal[opponent][target]

        if target in self.coords_ships[opponent]:
            self.active_target_status[player] = 'hit'
            ship_name = self.coords_ships[opponent][self.active_target[player]]
            self.active_target_shipname[player] = ship_name
            self.ship_hits[opponent][ship_name] += 1
            self.update_ship_integ()
        else:
            self.active_target_status[player] = 'miss'