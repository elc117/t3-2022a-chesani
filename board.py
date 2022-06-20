import pygame;
from itertools import product


def init():#inicia o pygame
    pygame.display.set_caption('Chessani'); #nome do jogo
    pygame.init();
    return pygame.display.set_mode([1920, 1080]); #tamanho do display
    
def update(): 
    pygame.display.update();

def rangeToList(start, stop): #gera uma lista a partir de um intervalo
    return list(range(start, stop));

def charRange(l): #gera uma lista com numeros convertidos para caracteres
    return list(map(chr, l));

def productOfRC(rows, columns): #produto cartesiano das linhas e colunas
    return list(product(rows, columns));

def positions():
    return productOfRC(rangeToList(1, 9), charRange(rangeToList(97, 105)));

def split(rc): #recebe a lista de linhas e colunas e divide em listas de 8, gerando uma "matriz"
    return [rc[i:i + 8] for i in range(0, len(rc), 8)] #um exemplo de list comprehension
    

def draw():
    print('a');

