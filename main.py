#!/usr/bin/env python
import board;
__author__ = 'Luís Henrique Chesani';
__email__ = 'lhchesani@inf.ufsm.br';

checkMate = False;

def gameLoop():
    return True if not checkMate else False;





if __name__ == '__main__':
    display = board.displayInit();
    board_ = board.init();
    while gameLoop:
        board.draw(display);
        board.drawPieces(display, board_);
        board.update();
        board.cachorro()