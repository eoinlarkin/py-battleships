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

SHIP_INTEG_LOC = {
    'p1': {'S1': [73, 6], 'S2': [73, 7], 'S3': [73, 8]},
    'p2': {'S1': [31, 35], 'S2': [31, 36], 'S3': [31, 37]}
}


def xy(text, xcoords, ycoords, color):
    with term.location(x=xcoords, y=ycoords):
        print(color + text)


def ship_status(board):
    for player in SHIP_INTEG_LOC:
        for ship in SHIP_INTEG_LOC[player]:
            value = board.ship_integ[player][ship]
            xcoords = SHIP_INTEG_LOC[player][ship][0]
            ycoords = SHIP_INTEG_LOC[player][ship][1]
            with term.location(x=xcoords, y=ycoords):
                print(term.gold + str(value) + '% ')


def print_target_request(ycoord):
    print(term.move(ycoord, 0) +
          term.white_on_blue +
          term.center('Select your next target:') +
          term.normal)
    print(term.move(ycoord, 58)+term.normal)
    with term.cbreak():
        target, inp, i = '', term.inkey(), 1
        print(term.move(ycoord, 58+i)+inp)
        while inp.name != 'KEY_ENTER' and i <= 2:
            target += inp
            inp = term.inkey()
            i += 1
            if i <= 2:
                print(term.move(ycoord, 58+i)+inp)
        print(term.move(ycoord-1, 0))
        return target


def clear():
    print(term.home + term.clear)


def clear_line(ycoords):
    with term.location(x=0, y=ycoords), term.cbreak():
        print(term.clear_eol)


def target_invalid(xcoords, ycoords):
    with term.location(x=xcoords, y=ycoords):
        print(term.black_on_yellow +
              term.center('Invalid coordinate selected; please try again...!'))


def target_previously_selected(xcoords, ycoords):
    with term.location(x=xcoords, y=ycoords):
        print(term.black_on_yellow +
              term.center("This target has already been selected; please " +
                          "select an alternative target."))


def confirm_hit(xcoords, ycoords, hit_type):
    with term.location(x=xcoords, y=ycoords):
        if hit_type == 'hit':
            print(term.yellow_on_black + term.center("It's a hit!"))
        else:
            print(term.white_on_red + term.center("It's a miss!"))


def ship_sunk(xcoords, ycoords, ship):
    with term.location(x=xcoords, y=ycoords):
        print(term.black_on_green +
              term.center(f"The {ship} is sunk...!"))


def update_board(xcoords, ycoords, hit_type):
    with term.location(x=xcoords, y=ycoords):
        if hit_type == 'hit':
            print(term.red + ("X"))
        else:
            print(term.blue + ("0"))


def opponent_move_text(xcoords, ycoords, target):
    with term.location(x=xcoords, y=ycoords):
        print(term.black_on_orange +
              term.center(f"The Computer has selected target {target}...."))


def print_checking_move(xcoords, ycoords, target):
    with term.location(x=xcoords, y=ycoords):
        print(term.white_on_purple +
              term.center(f"Checking target {target}...."))


def boards():
    xy(layout.player_board, 1, 0, term.lawngreen)
    xy(layout.computer_board, 1, 20, term.orange)


def intro():
    clear()
    for line in layout.logo.split('\n'):
        print(term.orangered + term.center(line))
    xy(term.center('press any key to continue'), 0, 40, term.black_on_green)
    with term.cbreak(), term.hidden_cursor():
        term.inkey()
    clear()


def instruct():
    clear()
    for line in layout.welcome_text.split('\n'):
        print(term.green + term.center(line))
    for line in layout.instruct_text.split('\n'):
        print(term.orangered + term.center(line))
    xy(term.center(layout.goodluck_text), 0, 39, term.black_on_green)
    xy(term.center('press any key to continue'), 0, 40, term.black_on_green)
    with term.cbreak(), term.hidden_cursor():
        term.inkey()
    clear()


def victory_message():
    clear()
    for line in layout.victory_text.split('\n'):
        print(term.green + term.center(line))
    xy(term.center('press the RESTART GAME button to play again'),
       0, 40, term.black_on_green)


def defeat_message():
    clear()
    for line in layout.defeat_text.split('\n'):
        print(term.orangered + term.center(line))
    xy(term.center('press the RESTART GAME button to play again'),
       0, 40, term.black_on_green)


def printships(board, player):
    ship_pos = board.loc_ships[player]
    grid_pos = board.loc_terminal[player]

    for ship in ship_pos:
        start_pos = grid_pos[ship_pos[ship]['start']]
        if ship_pos[ship]['orient'] == 't2b':
            for length in range(ship_pos[ship]['size']*2-1):
                print(term.deepskyblue4 +
                      term.move(start_pos[1]+length, start_pos[0]) + "█")
        elif ship_pos[ship]['orient'] == 'l2r':
            for length in range(ship_pos[ship]['size']*4-2):
                print(term.deepskyblue4 +
                      term.move(start_pos[1], start_pos[0]+length) + "█")
