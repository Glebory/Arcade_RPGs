import pygame
from GameObject import *


class Enemy(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._imagesF = [pygame.image.load('images/enemies/Bottle_F.png').convert_alpha()]
        self._imagesF.append(pygame.image.load('images/enemies/Bottle_FR.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/enemies/Bottle_F.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/enemies/Bottle_FL.png').convert_alpha())

        self.images = self._imagesF
        self.image = self.images[0]
        self.state = "moving"
        self.frames = 50
        self.speed = 0.2

    def move(self, player):
        if self.index//self.frames == 1 or self.index//self.frames == 3:
            if (player.x_coord - self.x_coord) > 0:
                self.x_change = self.speed
            else:
                self.x_change = -self.speed

            if (player.y_coord - self.y_coord+10) > 0:
                self.y_change = self.speed
            else:
                self.y_change = -self.speed
        else:
            self.x_change, self.y_change = 0, 0
