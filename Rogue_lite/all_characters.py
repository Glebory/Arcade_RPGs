import pygame
from Player import *
from all_weapons import *


def gimbo(spawn, handler):
    imagesF = [pygame.image.load('images/characters/Gimbo/Gimbo.png').convert_alpha(),
               pygame.image.load('images/characters/Gimbo/Gimbo_FL.png').convert_alpha(),
               pygame.image.load('images/characters/Gimbo/Gimbo.png').convert_alpha(),
               pygame.image.load('images/characters/Gimbo/Gimbo_FR.png').convert_alpha()]

    imagesL = [pygame.image.load('images/characters/Gimbo/Gimbo_L.png').convert_alpha()]
    imagesR = [pygame.image.load('images/characters/Gimbo/Gimbo_R.png').convert_alpha()]
    imagesB = [pygame.image.load('images/characters/Gimbo/Gimbo_B.png').convert_alpha()]

    speed = 2
    weapon = g_shot(spawn, handler)
    handler.objects.add(weapon)
    handler.weapon_group.add(weapon)
    name = "Gimbo"
    player = Player(name, spawn, weapon, [imagesF, imagesL, imagesR, imagesB], speed, handler)
    weapon.owner = player
    return player
