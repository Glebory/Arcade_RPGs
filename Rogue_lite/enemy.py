import pygame
from GameObject import *


class Enemy(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._imagesF = [pygame.image.load('images/enemies/Bottle_F.png').convert_alpha()]
        self._imagesF.append(pygame.image.load('images/enemies/Bottle_FR.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/enemies/Bottle_FL.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/enemies/Bottle_F.png').convert_alpha())

        self.images = self._imagesF
        self.image = self.images[0]
        self.state = "moving"
        self.frames = 40