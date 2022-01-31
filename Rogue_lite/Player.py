from GameObject import *
import pygame

class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._imagesF = [pygame.image.load('images/Gimbo.png').convert_alpha()]
        self._imagesF.append(pygame.image.load('images/Gimbo_FL.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/Gimbo.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/Gimbo_FR.png').convert_alpha())

        self._imagesL = [pygame.image.load('images/Gimbo_L.png').convert_alpha()]
        self._imagesR = [pygame.image.load('images/Gimbo_R.png').convert_alpha()]
        self._imagesB = [pygame.image.load('images/Gimbo_B.png').convert_alpha()]
        self.images = self._imagesF
        self.image = self._images[self._index]
        self.speed = 0.3

    def mv_up(self):
        self.y_change = -self.speed
        self.images = self._imagesB

    def mv_down(self):
        self.y_change = self.speed
        self.images = self._imagesF

    def mv_left(self):
        self.x_change = -self.speed
        self.images = self._imagesL

    def mv_right(self):
        self.x_change = self.speed
        self.images = self._imagesR






