import pygame
from gameobjects import GameObjects

class End(GameObjects):
    def __init__(self, position):
        super().__init__(position)
        self.image = self.image = pygame.image.load('images/tiles/tile22.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2.2, self.image.get_height() * 2.7))

        self.rect = self.image.get_rect()
        self.rect.center = (self._position[0], self._position[1])

    def draw(self, window, scroll):
        window.blit(self.image, self.rect)
        self.rect.x += scroll

    def end_level(self, player, level):
        if self.rect.colliderect(player):
            level = 3
            print("HELP")
            print(level)
