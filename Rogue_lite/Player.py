from GameObject import *
import pygame

class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load('images/Gimbo.png').convert_alpha()
        self.imageF = []
        self.speed = 0.3

    def mv_up(self):
        self.y_change = -self.speed
        self.image = pygame.image.load('images/Gimbo_B.png').convert_alpha()

    def mv_down(self):
        self.y_change = self.speed
        self.image = pygame.image.load('images/Gimbo.png').convert_alpha()

    def mv_left(self):
        self.x_change = -self.speed
        self.image = pygame.image.load('images/Gimbo_L.png').convert_alpha()

    def mv_right(self):
        self.x_change = self.speed
        self.image = pygame.image.load('images/Gimbo_R.png').convert_alpha()






