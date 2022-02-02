from GameObject import *
from Swing import *
from bullet import *
import pygame

class Player(GameObject):
    def __init__(self, x, y, weapon, img_matrix, speed):
        super().__init__(x, y)
        self._imagesF = img_matrix[0]
        self._imagesL = img_matrix[1]
        self._imagesR = img_matrix[2]
        self._imagesB = img_matrix[3]
        self.images = self._imagesF
        self.image = self._images[self._index]
        self._weapon = weapon
        self.speed = speed
        self.last_images = self._imagesF

    def mv_up(self):
        self.y_change = -self.speed
        self.weapon.y_change = -self.speed
        self.weapon.last_images = self.weapon.images
        self.weapon.images = self.weapon.imagesF
        self.weapon.x_coord = self.x_coord
        self.last_images = self.images
        self.images = self._imagesB

    def mv_down(self):
        self.y_change = self.speed
        self.weapon.y_change = self.speed
        self.weapon.last_images = self.weapon.images
        self.weapon.images = self.weapon.imagesF
        self.weapon.x_coord = self.x_coord
        self.last_images = self.images
        self.images = self._imagesF

    def mv_left(self):
        self.x_change = -self.speed
        self.weapon.x_change = -self.speed
        self.weapon.last_images = self.weapon.images
        self.weapon.images = self.weapon.imagesL
        self.weapon.x_coord = self.x_coord -16
        self.last_images = self.images
        self.images = self._imagesL

    def mv_right(self):
        self.x_change = self.speed
        self.weapon.x_change = self.speed
        self.weapon.last_images = self.weapon.images
        self.weapon.images = self.weapon.imagesR
        self.weapon.x_coord = self.x_coord
        self.last_images = self.images
        self.images = self._imagesR

    def attack_up(self):
        self.last_images = self.images
        self.images = self._imagesB

    def attack_down(self):

        self.last_images = self.images
        self.images = self._imagesF

    def attack_left(self):
        self.last_images = self.images
        self.images = self._imagesL

    def attack_right(self):
        self.last_images = self.images
        self.images = self._imagesR

    def get_weapon(self):
        return self._weapon

    def set_weapon(self, weapon):
        self._weapon = weapon
        return

    weapon = property(get_weapon, set_weapon)


    def stop(self):
        self.images = self.last_images
        self.weapon.images = self.weapon.last_images
        self.image = self.images[0]
        self.state = "stopped"
        self.weapon.state = "stopped"
        self.weapon.image = self.weapon.images[0]

