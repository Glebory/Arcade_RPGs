from GameObject import *
from Swing import *
from Bullet import *
import pygame
from Shadow import *

class Player(GameObject):
    def __init__(self, name, spawn, weapon, img_matrix, speed, handler):
        super().__init__(name, spawn)
        self._imagesF = img_matrix[0]
        self._imagesL = img_matrix[1]
        self._imagesR = img_matrix[2]
        self._imagesB = img_matrix[3]
        self.images = self._imagesF
        self.image = self._images[self._index]
        self._rect = self.image.get_rect(topleft=(spawn))
        self._weapon = weapon
        self.speed = speed
        self.handler = handler
        self._shadow = Shadow(self,0, self.rect.height +3)
        handler.unmovable_group.add(self._shadow)
        self.health = 3



    def mv_up(self):
        self.y_change = -self.speed
        self.weapon.y_change = -self.speed
        self.turn_up()


    def mv_down(self):
        self.y_change = self.speed
        self.weapon.y_change = self.speed
        self.turn_down()


    def mv_left(self):
        self.x_change = -self.speed
        self.weapon.x_change = -self.speed
        self.turn_left()


    def mv_right(self):
        self.x_change = self.speed
        self.weapon.x_change = self.speed
        self.turn_right()


    def turn_up(self):
        self.weapon.images = self.weapon.imagesF
        self.weapon.x_coord = self.rect.x
        self.images = self._imagesB

    def turn_down(self):
        self.weapon.images = self.weapon.imagesF
        self.weapon.x_coord = self.rect.x
        self.images = self._imagesF

    def turn_left(self):
        self.weapon.images = self.weapon.imagesL
        self.weapon.x_coord = self.rect.x -16
        self.images = self._imagesL

    def turn_right(self):
        self.weapon.images = self.weapon.imagesR
        self.weapon.x_coord = self.rect.x
        self.images = self._imagesR

    def attack_up(self):
        self.turn_up()
        self.weapon.direction = (0,-1)
        self.weapon.state = "shooting"

    def attack_down(self):
        self.turn_down()
        self.weapon.direction = (0,1)
        self.weapon.state = "shooting"

    def attack_left(self):
        self.turn_left()
        self.weapon.direction = (-1,0)
        self.weapon.state = "shooting"

    def attack_right(self):
        self.turn_right()
        self.weapon.direction = (1,0)
        self.weapon.state = "shooting"
        print("player attack OK")

    def get_weapon(self):
        return self._weapon

    def set_weapon(self, weapon):
        self._weapon = weapon
        return

    weapon = property(get_weapon, set_weapon)

    def update(self):
        self.rect.x += self._x_change
        self.rect.y += self._y_change
        if self.health < 0:
            print("dead")
    def stop(self):
        self.image = self.images[0]
        self.state = "stopped"
        self.weapon.state = "stopped"
        self.weapon.image = self.weapon.images[0]

