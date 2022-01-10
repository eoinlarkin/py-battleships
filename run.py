#! /usr/bin/env python3

# Calling the python script
#exec(open("/app/battleships/battleships.py").read())
# exec(open("battleships/battleships.py").read())

import battleships.battleships as battleships

if __name__ == '__main__':
    player = battleships.board('player')
    computer = battleships.board('computer')
    battleships.rungame(player, computer)