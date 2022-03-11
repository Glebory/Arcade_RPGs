import pygame
from enemy import Enemy

class Butterfly(Enemy):
    def __init__(self, position, health):
        super().__init__(position, health)
        self._images = []
        self._size = 48
        for x in range(1, 7):
            self.image = pygame.image.load(f'images/ButterflyCycle/butterfly{x}.png')
            self.image = pygame.transform.scale(self.image, (self._size * 0.75, self._size * 0.75))
            self._images.append(self.image)
        self._images2 = self._images
        self._current = 1
        self.image = self._images[self._current]
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0], self.position[1])
        self._max = 6
