#!/usr/bin/env python
import board;
__author__ = 'Luís Henrique Chesani';
__email__ = 'lhchesani@inf.ufsm.br';

checkMate = False;






if __name__ == '__main__':
    display = board.displayInit();
    board_ = board.init();
    while not board.checkMate(board_):
        board.draw(display);
        board.drawPieces(display, board_);
        board.update();
        board.move(board_)
    winner = board.winner(board_)
    board.congrats(winner);