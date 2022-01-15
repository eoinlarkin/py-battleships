# pylint: disable=missing-function-docstring
# pylint: disable=no-name-in-module
# pylint: disable=unexpected-keyword-arg
# pylint: disable=invalid-name
# pylint: disable=consider-using-dict-items
"""
Module to define functions for printing and updating the terminal
Module leverages the blessed library for printing functions
"""
from blessed import Terminal
from battleships import layout
term = Terminal()

TERM_INPUT_LINE = 41
TERM_STATUS_LINE = 41

SHIP_INTEG_LOC = {
    'p1': {'S1': [73, 6], 'S2': [73, 7], 'S3': [73, 8]},
    'p2': {'S1': [31, 35], 'S2': [31, 36], 'S3': [31, 37]}
}


# def print_terminal(text, xcoords, ycoords, color):
#     with term.location(x=xcoords, y=ycoords):
#         print(color + text)

def xy(text, xcoords, ycoords, color):
    with term.location(x=xcoords, y=ycoords), term.hidden_cursor():
        print(color + text)


def ship_status(board):
    for player in SHIP_INTEG_LOC:
        for ship in SHIP_INTEG_LOC[player]:
            value = board.ship_integ[player][ship]
            xcoords = SHIP_INTEG_LOC[player][ship][0]
            ycoords = SHIP_INTEG_LOC[player][ship][1]
            with term.location(x=xcoords, y=ycoords):
                print(term.gold + str(value) + '% ')


def print_target_request():
    print(term.move(TERM_INPUT_LINE, 0)+term.normal)
    target = input(term.white_on_blue + term.center('Select your next target:') +
                   term.move(TERM_INPUT_LINE+1, 58)+term.normal)
    with term.hidden_cursor(), term.cbreak():
            return target
    


def clear():
    print(term.home + term.clear)


def clear_status_line(xcoords, ycoords):
    with term.location(x=xcoords, y=ycoords), term.hidden_cursor():
        print(term.clear_eol)


def clear_input_line(xcoords, ycoords):
    with term.location(x=xcoords, y=ycoords), term.hidden_cursor():
        print(term.clear_eol)


def target_invalid(xcoords, ycoords):
    with term.location(x=xcoords, y=ycoords), term.hidden_cursor():
        print(term.black_on_yellow +
              term.center('Invalid coordinate selected; please try again...!') + term.normal)


def target_previously_selected(xcoords, ycoords):
    with term.location(x=xcoords, y=ycoords), term.hidden_cursor():
        print(term.black_on_yellow + term.center(
            'This target has already been selected; please select an alternative target.') +
            term.normal)


def confirm_hit(xcoords, ycoords, hit_type):
    with term.location(x=xcoords, y=ycoords), term.hidden_cursor():
        if hit_type == 'hit':
            print(term.yellow_on_black + term.center("It's a hit!")+term.normal)
        else:
            print(term.white_on_red + term.center("It's a miss!")+term.normal)


def ship_sunk(xcoords, ycoords, ship):
    with term.location(x=xcoords, y=ycoords), term.hidden_cursor():
        print(term.black_on_green +
              term.center(f"Ship {ship} is sunk...!")+term.normal)


def update_board(xcoords, ycoords, hit_type):
    with term.location(x=xcoords, y=ycoords), term.hidden_cursor():
        if hit_type == 'hit':
            print(term.red + ("X"))
        else:
            print(term.blue + ("0"))


def opponent_move_text(xcoords, ycoords, target):
    with term.location(x=xcoords, y=ycoords), term.hidden_cursor():
        print(term.black_on_orange +
              term.center(f"The Computer has selected target {target}....")+term.normal)


def print_checking_move(xcoords, ycoords, target):
    with term.location(x=xcoords, y=ycoords), term.hidden_cursor():
        print(term.white_on_purple +
              term.center(f"Checking target {target}....")+term.normal)


def boards():
    xy(layout.player_board, 1, 0, term.green)
    xy(layout.computer_board, 1, 20, term.orange)


def intro():
    clear()
    xy(term.center(layout.logo), 1, 5, term.orangered)
    xy(term.center('press and key to continue'), 0, 30, term.black_on_green)
    with term.cbreak(), term.hidden_cursor():
        term.inkey()
    clear()


def instruct():
    clear()
    xy(term.center(layout.instruct_text), 1, 5, term.orangered)
    xy(term.center('press and key to continue'), 0, 30, term.black_on_green)
    with term.cbreak(), term.hidden_cursor():
        term.inkey()
    clear()


def victory_message():
    print(term.clear+term.move(TERM_STATUS_LINE, 0) +
          term.center('You have defeated the computer!'))


def printships(board, player):
    ship_pos = board.loc_ships[player]
    grid_pos = board.loc[player]

    for ship in ship_pos:
        start_pos = grid_pos[ship_pos[ship]['start']]
        if ship_pos[ship]['direction'] == 't2b':
            for length in range(ship_pos[ship]['size']*2-1):
                print(term.deepskyblue4 +
                      term.move(start_pos[1]+length, start_pos[0]) + "█")
        elif ship_pos[ship]['direction'] == 'l2r':
            for length in range(ship_pos[ship]['size']*4-2):
                print(term.deepskyblue4 +
                      term.move(start_pos[1], start_pos[0]+length) + "█")
