#! /usr/bin/env python3
"""
Module to run the battleships game
The Board class is initialised and the rungame() function is
called from the game module
"""
from battleships import battleships
from battleships import game

if __name__ == '__main__':
    board = battleships.Board()
    game.rungame(board)
