from GameObject import *
import pygame
import all_weapons

class Weapon(GameObject):
    def __init__(self, x, y, images_matrix):
        super().__init__(x, y)
        self._imagesF = images_matrix[0]
        self._imagesR = images_matrix[1]
        self._imagesL = images_matrix[2]
        self._imagesB = images_matrix[3]
        self.images = self._imagesF
        self.image = self.images[0]
        self.last_images = self._imagesF

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
