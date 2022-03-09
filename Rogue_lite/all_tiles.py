from ActiveTile import *
import pygame


def beach_images():
    beach_imgs = [pygame.image.load('images/Error.png').convert_alpha(),
                  pygame.image.load('images/tree_barrier.png').convert_alpha(),
                  pygame.image.load('images/sea-tile.png').convert_alpha(),
                  pygame.image.load('images/tree_barrier.png').convert_alpha(),
                  pygame.image.load('images/rockS.png').convert_alpha(),
                  pygame.image.load('images/RockB.png').convert_alpha(),
                  pygame.image.load('images/RockM.png').convert_alpha()]
    return beach_imgs