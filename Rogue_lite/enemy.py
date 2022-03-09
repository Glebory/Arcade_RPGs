import pygame
from GameObject import *
from Shadow import *
from math import *
import random

class Enemy(GameObject):
    def __init__(self,name, spawn, handler, health):
        super().__init__(name, spawn)
        self._imagesF = [pygame.image.load('images/enemies/Bottle_F.png').convert_alpha()]
        self._imagesF.append(pygame.image.load('images/enemies/Bottle_FR.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/enemies/Bottle_F.png').convert_alpha())
        self._imagesF.append(pygame.image.load('images/enemies/Bottle_FL.png').convert_alpha())
        self.shadow = Shadow(self,-3.5,9)
        self.handler = handler
        handler.enemy_group_shadow.add(self.shadow)
        handler.unmovable_group.add(self.shadow)
        self.images = self._imagesF
        self.image = self.images[0]
        self.state = "chilling"
        self.frames = 50
        self.speed = 1
        self.aggro_radius = 100
        self.health = health
        self.damage = 1

    def aggro(self, player):
        if (player.rect.x - self.rect.x) > 0:
            self.x_change = self.speed
            self.shadow.x_change = self.speed
        else:
            self.x_change = -self.speed
            self.shadow.x_change = -self.speed

        if (player.rect.y - self.rect.y+10) > 0:
            self.y_change = self.speed
            self.shadow.y_change = self.speed
        else:
            self.y_change = -self.speed
            self.shadow.y_change = -self.speed

    def update(self):
        self.check_aggro(self.handler.player_group.sprites()[0])
        if self.state == "aggro":
            self.aggro(self.handler.player_group.sprites()[0])
        elif self.index == 0:
            self.chill()
        if self.index-30 < 0:
            self.rect.x += self._x_change
            self.rect.y += self._y_change
            self.shadow.x_change = self.x_change
            self.shadow.y_change = self._y_change
        else:
            self.shadow.x_change = 0
            self.shadow.y_change = 0
        self.index += 1
        if self.index > 90:
            self.index = 0
        if self.health < 0:
            self.kill()



    def check_aggro(self, player):
        player_x_distance = player.rect.x + (player.rect.width // 2) - self.rect.x
        player_y_distance = player.rect.y + (player.rect.height // 2) - self.rect.y
        player_distance = sqrt(player_x_distance**2 + player_y_distance**2)
        if player_distance < self.aggro_radius:
            self.state = "aggro"

    def chill(self):
        self.x_change = random.randint(-self.speed,self.speed)
        self.y_change = random.randint(-self.speed,self.speed)
