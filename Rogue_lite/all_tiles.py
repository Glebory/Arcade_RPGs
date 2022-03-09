from ActiveTile import *
import pygame


def beach_tile( x, h):
    DEFAUALT_Y = h-32
    DEFAULT_IMGS = [pygame.image.load('images/sea-tile.png').convert_alpha(),
                    pygame.image.load('images/sea-tile2.png').convert_alpha(),
                    pygame.image.load('images/sea-tile3.png').convert_alpha(),
                    pygame.image.load('images/sea-tile4.png').convert_alpha()]
    return ActiveTile(x, DEFAUALT_Y, DEFAULT_IMGS)

def beach_images():
    beach_imgs = ['images/sea-tile.png',
                    'images/sea-tile2.png',
                    'images/sea-tile3.png',
                    'images/sea-tile4.png']
    return beach_imgs