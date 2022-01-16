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
    Otherwise the user is asked for a valid target
    """
    gameboard.active_target['p1'] = termprint.print_target_request(
        TERM_INPUT_LINE)
    gameboard.validate_target()
    while gameboard.active_target_invalid['p1'] or gameboard.active_target_previous['p1']:
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
    results in a ship being sunk
    """
    if active_player == 'p1':
        player, opponent = 'p1', 'p2'
    else:
        player, opponent = 'p2', 'p1'

    if gameboard.active_target_status[player] == 'hit':
        ship = gameboard.active_target_shipname[player]
        if gameboard.ship_sunk[opponent][ship]:
            wait()
            termprint.ship_sunk(xcoords=0, ycoords=TERM_STATUS_LINE, ship=ship)


def rungame(board):
    """
    Function to run Battleship game with output printed to the terminal
    """

    # *******************************
    # Step 1: Draw the Board
    # *******************************

    board.gen_target_list(8)
    board.place_ships()
    board.gen_loc('p1', size=8, start_x=21, start_y=4, ygap=2, xgap=4)
    board.gen_loc('p2', size=8, start_x=49, start_y=24, ygap=2, xgap=4)

    termprint.intro()
    termprint.instruct()
    termprint.boards()
    termprint.printships(board, 'p1')
    termprint.ship_status(board)

    while True:
        with termprint.term.hidden_cursor():  # hiding the cursor
            board.active_player['p1'], board.active_player['p2'] = True, False
            user_input_request(board)

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

            board.update_ship_sunk_status()
            confirm_ship_sunk(board, 'p1')

            wait()
            termprint.clear_line(TERM_STATUS_LINE)
            termprint.ship_status(board)
            if board.check_victory():
                break

            wait()
            board.active_player['p1'], board.active_player['p2'] = False, True
            board.generate_target('p2')
            termprint.opponent_move_text(xcoords=0,
                                         ycoords=TERM_INPUT_LINE,
                                         target=board.active_target['p2'])

            wait()
            board.check_target_hit(board)
            termprint.confirm_hit(xcoords=0,
                                  ycoords=TERM_INPUT_LINE,
                                  hit_type=board.active_target_status['p2'])
            termprint.update_board(xcoords=board.active_target_loc['p2'][0],
                                   ycoords=board.active_target_loc['p2'][1],
                                   hit_type=board.active_target_status['p2'])

            board.update_ship_sunk_status()
            confirm_ship_sunk(board, 'p2')

            wait()
            termprint.ship_status(board)
            if board.check_victory():
                break

    termprint.victory_message()
