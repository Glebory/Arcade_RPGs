import pygame
import Weapon

def g_shot(x,y):
    imagesF = [(pygame.image.load('images/weapons/G_shot/G_shot_F.png').convert_alpha()),
               (pygame.image.load('images/weapons/G_shot/G_shot_FL.png').convert_alpha()),
               (pygame.image.load('images/weapons/G_shot/G_shot_F.png').convert_alpha()),
               (pygame.image.load('images/weapons/G_shot/G_shot_FR.png').convert_alpha())]
    imagesR = [pygame.image.load('images/weapons/G_shot/G_shot_R.png').convert_alpha()]
    imagesL = [pygame.image.load('images/weapons/G_shot/G_shot_L.png').convert_alpha()]
    imagesB = [pygame.image.load('images/weapons/G_shot/G_shot_F.png').convert_alpha()]
    weapon = Weapon.Weapon(x, y, [imagesF, imagesR, imagesL, imagesB])
    return weapon
