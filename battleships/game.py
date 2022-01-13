import battleships.battleships as battleships
import battleships.termprint as termprint
from time import sleep

def wait():
    sleep(1) # time in seconds


def rungame(board):

    board.coords_ships['p1'] = battleships.place_ships(board.ship_data['p1'])
    board.coords_board['p1'] = battleships.gen_board(8)
    board.loc['p1'] = board.gen_loc(size=8, start_x=21, start_y=4, ygap=2, xgap=4)
    board.coords_ships['p2'] = battleships.place_ships(board.ship_data['p2'])
    board.coords_board['p2'] = battleships.gen_board(8)
    board.loc['p2'] = board.gen_loc(size=8, start_x=49, start_y=24, ygap=2, xgap=4)

    termprint.intro()
    termprint.instruct()
    termprint.boards()
    termprint.printships(board, 'p1')
    termprint.print_integ(board)

    while not battleships.check_victory(board):
        termprint.clear_status_line()
        board.active_target['p1'] = termprint.print_target_request() 
        battleships.validate_target(board)
        while board.active_target_invalid['p1'] or board.active_target_previous['p1']:
            if board.active_target_invalid['p1']:
                termprint.target_invalid(0, 43)
            if board.active_target_previous['p1']:
                termprint.target_previously_selected(0, 43)
            board.active_target['p1'] = termprint.print_target_request() 
            battleships.validate_target(board)

        wait()
        termprint.clear_input_line()

        termprint.player_move_text(xcoords=0,
                        ycoords=termprint.TERM_INPUT_LINE,
                        target=board.active_target['p1'])

        wait()
        battleships.check_target_hit('p1',board)
        termprint.confirm_hit(xcoords=0,
                              ycoords=termprint.TERM_INPUT_LINE,
                              hit_type=board.active_target_status['p1'])
        termprint.update_board(xcoords=board.active_target_loc['p1'][0],
                                ycoords=board.active_target_loc['p1'][1],
                                hit_type=board.active_target_status['p1'])

        wait()
        battleships.target_computer(board)
        termprint.opponent_move_text(xcoords=0,
                               ycoords=termprint.TERM_INPUT_LINE,
                               target=board.active_target['p2'])
        
        wait()
        battleships.check_target_hit('p2',board)
        termprint.confirm_hit(xcoords=0,
                    ycoords=termprint.TERM_INPUT_LINE,
                    hit_type=board.active_target_status['p2'])
        termprint.update_board(xcoords=board.active_target_loc['p2'][0],
                                ycoords=board.active_target_loc['p2'][1],
                                hit_type=board.active_target_status['p2'])

        wait()
        battleships.check_target_hit('p2',board)
        
    termprint.victory()

