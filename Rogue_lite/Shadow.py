import pygame
from GameObject import *


class Shadow(GameObject):
    def __init__(self, owner):
        super().__init__(owner)
        self._x = owner._x
        self._y = owner._y + owner.rect.height + 3
        self.image = pygame.image.load("images/shadow.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [self._x, self._y]

    def stop_x(self):
        self.x_change = 0
    def stop_y(self):
        self.y_change = 0

