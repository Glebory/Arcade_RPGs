import pygame


class Character:
    def __init__(self, position):
        self._position = position

    def __str__(self):
        return "%s" % self._position

    @property 
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position
