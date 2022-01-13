#! /usr/bin/env python3

from battleships import battleships
from battleships import game

if __name__ == '__main__':
    board = battleships.board()
    game.rungame(board)