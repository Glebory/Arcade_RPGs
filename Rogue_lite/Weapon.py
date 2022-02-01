from GameObject import *
import pygame


class Weapon(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self._imagesF = []
        self._imagesF.append(pygame.image.load('images/weapons/G_shot/G_shot_F.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/weapons/G_shot/G_shot_FL.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/weapons/G_shot/G_shot_F.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/weapons/G_shot/G_shot_FR.png').convert_alpha())
        self._imagesR = [pygame.image.load('images/weapons/G_shot/G_shot_R.png').convert_alpha()]
        self._imagesL = [pygame.image.load('images/weapons/G_shot/G_shot_L.png').convert_alpha()]
        self._imagesB = [pygame.image.load('images/weapons/G_shot/G_shot_F.png').convert_alpha()]
        self.images = self._imagesF
        self.image = self.images[0]

    def get_imagesF(self):
        return self._imagesF

    def set_imagesF(self, images):
        self._imagesF = images

    imagesF = property(get_imagesF, set_imagesF)

    def get_imagesR(self):
        return self._imagesR

    def set_imagesR(self, images):
        self._imagesR = images

    imagesR = property(get_imagesR, set_imagesR)

    def get_imagesL(self):
        return self._imagesL

    def set_imagesL(self, images):
        self._imagesL = images

    imagesL = property(get_imagesL, set_imagesL)

    def get_imagesB(self):
        return self._imagesB

    def set_imagesB(self, images):
        self._imagesB = images

    imagesB = property(get_imagesB, set_imagesB)
