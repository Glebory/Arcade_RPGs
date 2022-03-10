from GameObject import *
import pygame
import all_weapons
import all_bullets
from Bullet import  *

class Weapon(GameObject):
    def __init__(self, name, spawn, images_matrix, handler, sound, type=None):
        super().__init__(name, spawn)
        self.owner = None
        self.handler = handler
        self._imagesF = images_matrix[0]
        self._imagesR = images_matrix[1]
        self._imagesL = images_matrix[2]
        self._imagesB = images_matrix[3]
        self.images = self._imagesF
        self.image = self.images[0]
        self.sound = pygame.mixer.Sound(sound)
        self.spread = False
        self.cooldown = 0
        self.direction = (0,0)
        self._rect = self.image.get_rect(topleft=(spawn))
        self.damage = 5
        if type is None:
            self.type = ('gun', 'reg')

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

    def get_owner(self):
        return self._owner

    def set_owner(self, owner):
        self._owner = owner

    owner = property(get_owner, set_owner)

    def shoot(self):
        print("weapon shoot is called")
        if self.cooldown == 0:
            if self.type[0] == 'gun':
                if self.type[1] == 'reg':
                    bullet = all_bullets.reg_bullet(self.direction,(self.rect.x,self.rect.y), self.handler, self.damage)
                    self.sound.play()
                    self.handler._objects.add(bullet)
                    self.handler.player_bullets.add(bullet)
                    self.cooldown = 20
        else:
            self.cooldown -= 1

        return

    def update(self):
        self.rect.x = self.owner.rect.x
        self.rect.y = self.owner.rect.y
        if self.state == "shooting":
            self.shoot()
        #if self.owner.state == "moving":



    def get_owner(self):
        return self._owner

    def set_owner(self, owner):
        self._owner = owner

    owner = property(get_owner, set_owner)


