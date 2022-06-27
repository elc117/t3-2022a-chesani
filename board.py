import pygame;
import os;
from itertools import product
from tkinter import messagebox

def empty(): #inicializa o tabuleiro sem nenhuma posicao
    return [[('empty', 'empty') for _ in range(0, 8)] for _ in range(0, 8)];

def displayInit():#inicia o pygame
    pygame.display.set_caption('Chessani'); #nome do jogo
    pygame.init();
    return pygame.display.set_mode([800, 800]); #tamanho do display
    
def update(): 
    pygame.display.update();

def rangeToList(start, stop): #gera uma lista a partir de um intervalo
    return list(range(start, stop));

def charRange(l): #gera uma lista com numeros convertidos para caracteres
    return list(map(chr, l));

def productOfRC(rows, columns): #produto cartesiano das linhas e colunas
    return list(product(rows, columns));

def positions():
    return productOfRC(charRange(rangeToList(49, 57)), charRange(rangeToList(97, 105)));

def split(rc): #recebe a lista de linhas e colunas e divide em listas de 8, gerando uma "matriz"
    return [rc[i:i + 8] for i in range(0, len(rc), 8)] #um exemplo de list comprehension
    
def checkMate(board_):
    return False if ((True in (map((lambda x : ('King', 'white') in x), board_))) & (True in (map((lambda x : ('King', 'black') in x), board_)))) else True;

def winner(board_):
    return ' brancas ' if (True in (map((lambda x : ('King', 'white') in x), board_))) else ' pretas ';

def congrats(winner):
    messagebox.showinfo('Parabéns!', 'As' + winner + 'venceram! 😎')

def draw(display): #desenha o tabuleiro base, sem levar em consideracao as pecas
    cellSize = 100;
    display.fill((70,130,180));
    for x in range(0, 8, 2):
        for y in range(0, 8, 2):
            pygame.draw.rect(display, (176,196,222), (x*cellSize, y*cellSize, cellSize, cellSize));
    for x in range(1, 9, 2):
        for y in range(1, 9, 2):
            pygame.draw.rect(display, (176,196,222), (x*cellSize, y*cellSize, cellSize, cellSize));




#funcoes que nao usam programacao funcional
def init():
    begin = empty();
    for i in range(0, 8):
        begin[1][i] = ('Pawn', 'black');
    for i in range(0, 8):
        begin[6][i] = ('Pawn', 'white');
    begin[7][0] = begin[7][7] = ('Rook', 'white');
    begin[0][0] = begin[0][7] = ('Rook', 'black');
    begin[7][1] = begin[7][6] = ('Knight', 'white'); 
    begin[0][1] = begin[0][6] = ('Knight', 'black');
    begin[7][2] = begin[7][5] = ('Bishop', 'white');
    begin[0][2] = begin[0][5] = ('Bishop', 'black');
    begin[7][3] = ('Queen', 'white');
    begin[0][3] = ('Queen', 'black');
    begin[7][4] = ('King', 'white');
    begin[0][4] = ('King', 'black');
    return begin;

def drawPieces(display, board):
    blackRook = pygame.image.load(os.path.join('pieces', 'blackRook.png'));
    whiteRook = pygame.image.load(os.path.join('pieces', 'whiteRook.png'));
    blackKnight = pygame.image.load(os.path.join('pieces', 'blackKnight.png'));
    whiteKnight = pygame.image.load(os.path.join('pieces', 'whiteKnight.png'));
    blackBishop = pygame.image.load(os.path.join('pieces', 'blackBishop.png'));
    whiteBishop = pygame.image.load(os.path.join('pieces', 'whiteBishop.png'));
    blackQueen = pygame.image.load(os.path.join('pieces', 'blackQueen.png'));
    whiteQueen = pygame.image.load(os.path.join('pieces', 'whiteQueen.png'));
    blackKing = pygame.image.load(os.path.join('pieces', 'blackKing.png'));
    whiteKing = pygame.image.load(os.path.join('pieces', 'whiteKing.png'));
    blackPawn = pygame.image.load(os.path.join('pieces', 'blackPawn.png'));
    whitePawn = pygame.image.load(os.path.join('pieces', 'whitePawn.png'));
    for i in range(0, 8):
        for j in range(0, 8):
                if board[i][j] == ('Rook', 'black'):
                    display.blit(blackRook, (j*100,i*100));
                if board[i][j] == ('Rook', 'white'):
                    display.blit(whiteRook, (j*100,i*100));
                if board[i][j] == ('Knight', 'black'):
                    display.blit(blackKnight, (j*100,i*100));
                if board[i][j] == ('Knight', 'white'):
                    display.blit(whiteKnight, (j*100,i*100));
                if board[i][j] == ('Bishop', 'black'):
                    display.blit(blackBishop, (j*100,i*100));
                if board[i][j] == ('Bishop', 'white'):
                    display.blit(whiteBishop, (j*100,i*100));
                if board[i][j] == ('Queen', 'black'):
                    display.blit(blackQueen, (j*100,i*100));
                if board[i][j] == ('Queen', 'white'):
                    display.blit(whiteQueen, (j*100,i*100));
                if board[i][j] == ('King', 'black'):
                    display.blit(blackKing, (j*100,i*100));
                if board[i][j] == ('King', 'white'):
                    display.blit(whiteKing, (j*100,i*100));
                if board[i][j] == ('Pawn', 'black'):
                    display.blit(blackPawn, (j*100,i*100));
                if board[i][j] == ('Pawn', 'white'):
                    display.blit(whitePawn, (j*100,i*100));

def getPos():
    for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                c = pygame.mouse.get_pos()
                return (int(c[1]/100), int(c[0]/100))

def move(board_):
    x = y = None
    while x == None:
        x = getPos();
    while y == None:
        y = getPos();
    print(x)
    print(y)
    aux = board_[x[0]][x[1]]
    board_[x[0]][x[1]] = ('empty', 'empty')
    board_[y[0]][y[1]] = aux