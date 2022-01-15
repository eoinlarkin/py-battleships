# pylint: disable=E0611
from time import sleep
from battleships import battleships
from battleships import termprint


def wait():
    """
    Shorthand function to trigger sleep
    """
    sleep(1)  # time in seconds

def user_input_request(gameboard):
    gameboard.active_target['p1'] = termprint.print_target_request()
    battleships.validate_target(gameboard)
    while gameboard.active_target_invalid['p1'] or gameboard.active_target_previous['p1']:
        if gameboard.active_target_invalid['p1']:
            termprint.target_invalid(0, termprint.TERM_STATUS_LINE)
        if gameboard.active_target_previous['p1']:
            termprint.target_previously_selected(0, termprint.TERM_STATUS_LINE)
        gameboard.active_target['p1'] = termprint.print_target_request()
        battleships.validate_target(gameboard)

def confirm_ship_sunk(gameboard, active_player):
    if active_player == 'p1':
        player, opponent = 'p1', 'p2'
    else:
        player, opponent = 'p2', 'p1'

    if gameboard.active_target_status[player] == 'hit':
        ship = gameboard.coords_ships[opponent][gameboard.active_target[player]]
        if gameboard.ship_hits[opponent][ship] == gameboard.ship_size[opponent][ship]:
            wait()
            termprint.ship_sunk(x=0,y=termprint.TERM_STATUS_LINE,ship=ship)

def rungame(board):
    """
    Function to run Battleship game with output printed to the terminal
    """
    board.gen_board(8)
    board.place_ships()
    board.gen_loc('p1',size=8, start_x=21, start_y=4, ygap=2, xgap=4)
    board.gen_loc('p2',size=8, start_x=49, start_y=24, ygap=2, xgap=4)

    termprint.intro()
    termprint.instruct()
    termprint.boards()
    termprint.printships(board, 'p1')
    termprint.ship_status(board)

    while True:
        termprint.clear_status_line(x=0,y=termprint.TERM_STATUS_LINE)
        user_input_request(board)
        
        wait()
        termprint.print_checking_move(xcoords=0,
                                      ycoords=termprint.TERM_INPUT_LINE,
                                      target=board.active_target['p1'])

        wait()
        battleships.check_target_hit('p1', board)
        termprint.confirm_hit(xcoords=0,
                              ycoords=termprint.TERM_INPUT_LINE,
                              hit_type=board.active_target_status['p1'])
        termprint.update_board(xcoords=board.active_target_loc['p1'][0],
                               ycoords=board.active_target_loc['p1'][1],
                               hit_type=board.active_target_status['p1'])

        confirm_ship_sunk(board, 'p1')


        wait()
        termprint.ship_status(board)
        if board.check_victory():
            break

        wait()
        battleships.target_computer(board)
        termprint.opponent_move_text(xcoords=0,
                                     ycoords=termprint.TERM_INPUT_LINE,
                                     target=board.active_target['p2'])

        wait()
        battleships.check_target_hit('p2', board)
        termprint.confirm_hit(xcoords=0,
                              ycoords=termprint.TERM_INPUT_LINE,
                              hit_type=board.active_target_status['p2'])
        termprint.update_board(xcoords=board.active_target_loc['p2'][0],
                               ycoords=board.active_target_loc['p2'][1],
                               hit_type=board.active_target_status['p2'])

        confirm_ship_sunk(board, 'p2')

        wait()
        termprint.ship_status(board)
        if board.check_victory():
            break

    termprint.victory_message()
