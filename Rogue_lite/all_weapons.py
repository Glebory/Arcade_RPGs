import pygame
import Weapon
import all_bullets

def g_shot(spawn, handler):
    imagesF = [(pygame.image.load('images/weapons/G_shot/G_shot_F.png').convert_alpha()),
               (pygame.image.load('images/weapons/G_shot/G_shot_FL.png').convert_alpha()),
               (pygame.image.load('images/weapons/G_shot/G_shot_F.png').convert_alpha()),
               (pygame.image.load('images/weapons/G_shot/G_shot_FR.png').convert_alpha())]
    imagesR = [pygame.image.load('images/weapons/G_shot/G_shot_R.png').convert_alpha()]
    imagesL = [pygame.image.load('images/weapons/G_shot/G_shot_L.png').convert_alpha()]
    imagesB = [pygame.image.load('images/weapons/G_shot/G_shot_F.png').convert_alpha()]
    name = "G-Shot"
    sound = "sounds/shotgun_shot.wav"
    weapon = Weapon.Weapon(name, spawn, [imagesF, imagesR, imagesL, imagesB], handler, sound)
    return weapon
