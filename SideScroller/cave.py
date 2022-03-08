import pygame
from gameobjects import GameObjects

class Cave(GameObjects):
    def __init__(self, position, image):
        super().__init__(position)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0], self.position[1])

#    def draw(self, window):
#        window.blit(self.image, self.rect)
