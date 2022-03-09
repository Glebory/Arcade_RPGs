import pygame
from ui import *

def heart(spawn, handler):
    image = pygame.image.load('images/ui/Heart.png').convert_alpha()
    heart = Ui(spawn[0],spawn[1], image)
    handler.ui_group.add(heart)
    return heart

def coins(spawn, handler):
    image = pygame.image.load('images/ui/coin.png').convert_alpha()
    coin = Ui(spawn[0],spawn[1], image)
    handler.ui_group.add(coin)
    return coin