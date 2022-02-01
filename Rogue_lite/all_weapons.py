import pygame

def choose_weapon(name, weapon):
    if name == "G-Shot":
        weapon.imagesF.append(pygame.image.load('images/weapons/G_shot/G_shot_F.png').convert_alpha())
        weapon.imagesF.append(pygame.image.load('images/weapons/G_shot/G_shot_FL.png').convert_alpha())
        weapon.imagesF.append(pygame.image.load('images/weapons/G_shot/G_shot_F.png').convert_alpha())
        weapon.imagesF.append(pygame.image.load('images/weapons/G_shot/G_shot_FR.png').convert_alpha())
        weapon.imagesR = [pygame.image.load('images/weapons/G_shot/G_shot_R.png').convert_alpha()]
        weapon.imagesL = [pygame.image.load('images/weapons/G_shot/G_shot_L.png').convert_alpha()]
        weapon.imagesB = [pygame.image.load('images/weapons/G_shot/G_shot_F.png').convert_alpha()]