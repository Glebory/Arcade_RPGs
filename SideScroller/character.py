import pygame
from gameobjects import GameObjects

class Character(GameObjects):
    def __init__(self, position, health):
        super().__init__(position)
        self._health = health

    def __str__(self):
        return "%s" % self._position

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        self._health = new_health

    def boundaries(self):
        if self._position[0] <= 0:
            self._position[0] = 0
        elif self._position[0] >= 1100:
            self._position[0] = 1100
