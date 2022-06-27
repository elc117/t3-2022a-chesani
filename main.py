#!/usr/bin/env python
import board;
__author__ = 'Luís Henrique Chesani';
__email__ = 'lhchesani@inf.ufsm.br';

if __name__ == '__main__':
    display = board.displayInit();
    board_ = board.init();
    player = 'white'
    while not board.checkMate(board_):
        board.draw(display);
        board.drawPieces(display, board_);
        board.update();
        player = board.move(board_, player);
    winner = board.winner(board_)
    board.congrats(winner);