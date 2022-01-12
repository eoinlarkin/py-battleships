import battleships.battleships as battleships
import battleships.termprint as termprint
from time import sleep

def rungame(board):

    termprint.intro()
    termprint.boards()

    board.coords_ships['p1'] = battleships.place_ships(board.ship_data['p1'])
    board.coords_board['p1'] = battleships.draw_board(8)

    board.coords_ships['p2'] = battleships.place_ships(board.ship_data['p2'])
    board.coords_board['p2'] = battleships.draw_board(8)

    while not battleships.check_victory(board):
        
        battleships.get_target_player(board)
        while board.active_target_invalid['p1'] or board.active_target_previous['p1']:
            if board.active_target_invalid['p1']:
                termprint.target_invalid(0, 43)
            if board.active_target_previous['p1']:
                termprint.target_previously_selected(0, 43)
            battleships.get_target_player(board)

        battleships.check_target_hit('p1',board)
        termprint.confirm_hit(xcoords=0,
                              ycoords=termprint.TERM_INPUT_LINE,
                              hit_type=board.active_target_status['p1'])
        termprint.update_board(xcoords=board.active_target_loc['p1'][0],
                                ycoords=board.active_target_loc['p1'][1],
                                hit_type=board.active_target_status['p1'])

        sleep(1) # Time in seconds

        battleships.target_computer(board)
        termprint.opponent_move(xcoords=0,
                               ycoords=termprint.TERM_INPUT_LINE,
                               target=board.active_target['p2'])
        sleep(1)
        battleships.check_target_hit('p2',board)
        termprint.confirm_hit(xcoords=0,
                    ycoords=termprint.TERM_INPUT_LINE,
                    hit_type=board.active_target_status['p2'])
        termprint.update_board(xcoords=board.active_target_loc['p2'][0],
                                ycoords=board.active_target_loc['p2'][1],
                                hit_type=board.active_target_status['p2'])


        sleep(1) # Time in seconds
        battleships.check_target_hit('p2',board)
        
    termprint.victory()

