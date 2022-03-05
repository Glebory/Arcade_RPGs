import pygame
from gameobjects import GameObjects
import player


class Stairs(GameObjects):
    def __init__(self, position):
        super().__init__(position)
    #    self.image = pygame.image.load("images/tiles/tile7.png")
    #    self.rect = self.image.get_rect()
    #    self.rect.center = (self.position[0], self.position[1])

    def detect_stairs(self, char):
        if player.Player._left and not player.Player._right:
            char.rect.x += 20
            char.rect.y -= 20
