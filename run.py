#! /usr/bin/env python3

import battleships.battleships as battleships
import battleships.game as game

if __name__ == '__main__':
    board = battleships.board()
    game.rungame(board)