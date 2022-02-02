import pygame
from Player import *
from all_weapons import *


def gimbo(x, y, objects):
    imagesF = [pygame.image.load('images/characters/Gimbo/Gimbo.png').convert_alpha(),
               pygame.image.load('images/characters/Gimbo/Gimbo_FL.png').convert_alpha(),
               pygame.image.load('images/characters/Gimbo/Gimbo.png').convert_alpha(),
               pygame.image.load('images/characters/Gimbo/Gimbo_FR.png').convert_alpha()]

    imagesL = [pygame.image.load('images/characters/Gimbo/Gimbo_L.png').convert_alpha()]
    imagesR = [pygame.image.load('images/characters/Gimbo/Gimbo_R.png').convert_alpha()]
    imagesB = [pygame.image.load('images/characters/Gimbo/Gimbo_B.png').convert_alpha()]

    speed = 0.6
    weapon = g_shot(x, y)
    objects.append(weapon)
    return Player(x, y, weapon, [imagesF, imagesL, imagesR, imagesB], speed)
