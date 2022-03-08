import pygame
from gameobjects import GameObjects
import player


class Stairs(GameObjects):
    def __init__(self, position, image):
        super().__init__(position)
        self.image = image
    #    self.image = pygame.transform.scale(self.image, (self._size * 1, self._size * 1))

    #    self.rect = self.image.get_rect()
    #    self.rect.center = (self.position[0], self.position[1])

#    def draw(self, window, scroll):
#        window.blit(self.image, self.rect)
#    #    self.rect.x += scroll
#
#    def detect_stairs(self, character):
#        pass
