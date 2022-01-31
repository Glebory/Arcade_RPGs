from GameObject import *
import pygame


class Weapon(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._imagesF = []
        self._imagesF.append(pygame.image.load('images/G_shot_F.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/G_shot_FL.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/G_shot_F.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/G_shot_FR.png').convert_alpha())
        self.images = self._imagesF
        self.image = self.images[0]

