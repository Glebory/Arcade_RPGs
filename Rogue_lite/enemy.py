import pygame
from GameObject import *
from Shadow import *

class Enemy(GameObject):
    def __init__(self,name, spawn, handler):
        super().__init__(name, spawn)
        self._imagesF = [pygame.image.load('images/enemies/Bottle_F.png').convert_alpha()]
        self._imagesF.append(pygame.image.load('images/enemies/Bottle_FR.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/enemies/Bottle_F.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/enemies/Bottle_FL.png').convert_alpha())
        self.shadow = Shadow(self)
        self.handler = handler
        handler.enemy_group.add(self.shadow)
        self.images = self._imagesF
        self.image = self.images[0]
        self.state = "moving"
        self.frames = 50
        self.speed = 2

    def move(self, player):
        if (player.x_coord - self.x_coord) > 0:
            self.x_change = self.speed
            self.shadow.x_change = self.speed
        else:
            self.x_change = -self.speed
            self.shadow.x_change = -self.speed

        if (player.y_coord - self.y_coord+10) > 0:
            self.y_change = self.speed
            self.shadow.y_change = self.speed
        else:
            self.y_change = -self.speed
            self.shadow.y_change = -self.speed

        self.x_change, self.y_change = 0, 0
