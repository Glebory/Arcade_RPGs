import pygame
from gameobjects import GameObjects

class Character(GameObjects):
    def __init__(self, position, health):
        super().__init__(position)
        self._health = health
        self._segment = 75

    def __str__(self):
        return "%s" % self._position

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        self._health = new_health

    def draw(self, window, screen_scroll):
        window.blit(self.image, self.rect)
        self.rect.x += screen_scroll

    def boundaries(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= 1100:
            self.rect.x = 1100
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= 650:
            self.rect.y = 500

    def jump(self):
        if self._jump and self._in_air == False:
            self._mass = -11
            self._jump = False
            self._in_air = True
        self._mass += self._gravity
        if self._mass > 10:
            self._mass
        self._ySpeed += self._mass

    def damage(self):
        self._health -= 25
        self._score += 50
