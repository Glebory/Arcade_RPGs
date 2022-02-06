import pygame
from gameobjects import GameObjects

class Health(GameObjects):
    def __init__(self, position):
        super().__init__(position)
        self.image = pygame.image.load("images/full_health.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.22, self.image.get_height() * 0.22))
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0], self.position[1])

    def update(self, player):
        pass
