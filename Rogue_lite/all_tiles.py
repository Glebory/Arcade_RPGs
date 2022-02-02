from ActiveTile import *
import pygame


def beach_tile( x, h):
    DEFAUALT_Y = h-32
    DEFAULT_IMGS = [pygame.image.load('images/sea-tile.png').convert_alpha(),
                    pygame.image.load('images/sea-tile2.png').convert_alpha(),
                    pygame.image.load('images/sea-tile3.png').convert_alpha(),
                    pygame.image.load('images/sea-tile4.png').convert_alpha()]
    return ActiveTile(x, DEFAUALT_Y, DEFAULT_IMGS)

def create_random_tile(x,y):
    print ("success at "+ str(x)+" "+str(y))
    return