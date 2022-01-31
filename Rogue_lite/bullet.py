import GameObject
import pygame

class Bullet(GameObject):
    def __init__(self,x, y, image):
        super().__init__(x, y, image)
        self._type = "normal"
        self._speed = 0.1

