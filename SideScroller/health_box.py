import pygame
from gameobjects import GameObjects

class HealthBox(GameObjects):
    def __init__(self, position):
        super().__init__(position)
        self._health_image = pygame.image.load("images/tiles/tile30.png").convert_alpha()
        self._health_image = pygame.transform.scale(self._health_image, (self._size * 1, self._size * 1))
        self.rect = self._health_image.get_rect()
        self.rect.center = (position[0], position[1])

    def draw(self, window, scroll):
        window.blit(self._health_image, self.rect)
        self.rect.x += scroll

    def get_box(self, player):
        if self.rect.colliderect(player):
            if player._health <= 75 and player._max_health <= 3:
                player._health += 25
                player._max_health += 1
                player.update_health(player._max_health)
                self._health_image = pygame.image.load("images/tiles/tile6.png").convert_alpha()
                self._health_image = pygame.transform.scale(self._health_image, (self._size * 1, self._size * 1))
