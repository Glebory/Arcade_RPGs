import pygame
from enemy import Enemy

class Bat(Enemy):
    def __init__(self, position, health):
        super().__init__(position, health)
        self._images = []
        self._size = 48
        for x in range(1, 9):
            self.image = pygame.image.load(f'images/BatCycle/bat{x}.png')
            self.image = pygame.transform.scale(self.image, (self._size * 1, self._size * 1))
            self._images.append(self.image)
        self._images2 = self._images
        self._current = 6
        self.image = self._images[self._current]
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0], self.position[1])
