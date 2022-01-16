"""
Module to define the logic to run the game
Assumed that a Board class has been intitialised
termprint module is used to print the output to the screen
"""
# pylint: disable=no-name-in-module
from time import sleep
from battleships import termprint

TERM_INPUT_LINE = 41
TERM_STATUS_LINE = 42


def wait():
    """
    Shorthand function to trigger sleep
    """
    sleep(0.85)  # time in seconds


def user_input_request(gameboard):
    """
    Function to request a target from the user
    If a valid target is entered, the 'active_target' object is updated
    Otherwise the user is asked for a valid target. The status of the
    input is recorded in the Board() class
    """
    gameboard.active_target['p1'] = termprint.print_target_request(
        TERM_INPUT_LINE)
    gameboard.validate_target()
    while gameboard.active_target_invalid['p1'] or \
            gameboard.active_target_previous['p1']:
        if gameboard.active_target_invalid['p1']:
            termprint.target_invalid(0, TERM_STATUS_LINE)
        if gameboard.active_target_previous['p1']:
            termprint.target_previously_selected(0, TERM_STATUS_LINE)
        gameboard.active_target['p1'] = termprint.print_target_request(
            TERM_INPUT_LINE)
        gameboard.validate_target()


def confirm_ship_sunk(gameboard, active_player):
    """
    Function to print message to screen if the most recent target
    results in a ship being sunk. Requires termprint functionality
    as well as relying on the Board() class
    """
    if active_player == 'p1':
        player, opponent = 'p1', 'p2'
    else:
        player, opponent = 'p2', 'p1'

    if gameboard.active_target_status[player] == 'hit':
        ship = gameboard.active_target_shipname[player]
        if gameboard.ship_sunk[opponent][ship]:
            wait()
            ship_name = gameboard.ship_names_long[ship]
            termprint.ship_sunk(xcoords=0, ycoords=TERM_STATUS_LINE, ship=ship_name)


def rungame(board):
    """
    Function to run Battleship game with output printed to the terminal
    """

    # ************************************
    # Step 1: Initialise the Board Object
    # ************************************
    board.gen_target_list(8)
    board.place_ships('p1')
    board.place_ships('p2')
    board.gen_terminal_mapping(
        'p1', size=8, start_x=21, start_y=4, ygap=2, xgap=4)
    board.gen_terminal_mapping(
        'p2', size=8, start_x=49, start_y=24, ygap=2, xgap=4)

    # ************************************
    # Step 2: Draw Terminal Output
    # ************************************
    termprint.intro()
    termprint.instruct()
    termprint.boards()
    termprint.printships(board, 'p1')
    termprint.ship_status(board)

    # ************************************
    # Step 3: Run Game until victor:
    # ************************************
    while True:
        with termprint.term.hidden_cursor():  # hiding the cursor

            # ************************************
            # Step 3-1-1: Set P1 as Active Player
            # ************************************
            board.active_player['p1'], board.active_player['p2'] = True, False

            # ************************************
            # Step 3-1-2: Get P1 Move
            # ************************************
            user_input_request(board)

            # ************************************
            # Step 3-1-3: Check Move and Update Board
            # ************************************

            wait()
            termprint.clear_line(TERM_STATUS_LINE)
            termprint.print_checking_move(xcoords=0,
                                          ycoords=TERM_INPUT_LINE,
                                          target=board.active_target['p1'])

            wait()
            board.check_target_hit('p1')
            termprint.confirm_hit(xcoords=0,
                                  ycoords=TERM_INPUT_LINE,
                                  hit_type=board.active_target_status['p1'])
            termprint.update_board(xcoords=board.active_target_loc['p1'][0],
                                   ycoords=board.active_target_loc['p1'][1],
                                   hit_type=board.active_target_status['p1'])

            # ************************************
            # Step 3-1-4: Check if ship has sunk
            # ************************************
            board.update_ship_sunk_status()
            confirm_ship_sunk(board, 'p1')
            wait()
            termprint.clear_line(TERM_STATUS_LINE)
            termprint.ship_status(board)

            # ************************************
            # Step 3-1-5: Check if player victorious
            # ************************************
            if board.check_victory():
                break

            # ************************************
            # Step 3-2-1: Set P2 as Active Player
            # ************************************
            wait()
            board.active_player['p1'], board.active_player['p2'] = False, True

            # ************************************
            # Step 3-1-3: Get P2 Move
            # ************************************
            board.generate_target('p2')
            termprint.opponent_move_text(xcoords=0,
                                         ycoords=TERM_INPUT_LINE,
                                         target=board.active_target['p2'])

            # ************************************
            # Step 3-1-3: Check Move and Update Board
            # ************************************
            wait()
            board.check_target_hit(board)
            termprint.confirm_hit(xcoords=0,
                                  ycoords=TERM_INPUT_LINE,
                                  hit_type=board.active_target_status['p2'])
            termprint.update_board(xcoords=board.active_target_loc['p2'][0],
                                   ycoords=board.active_target_loc['p2'][1],
                                   hit_type=board.active_target_status['p2'])

            # ************************************
            # Step 3-1-4: Check if ship has sunk
            # ************************************
            board.update_ship_sunk_status()
            confirm_ship_sunk(board, 'p2')
            wait()
            termprint.ship_status(board)

            # ************************************
            # Step 3-1-5: Check if player victorious
            # ************************************
            if board.check_victory():
                break

    # ************************************
    # Step 4: Exit While loop and print victory message
    # ************************************
    if board.victory['p1']:
        termprint.victory_message()
    else:
        termprint.defeat_message()
