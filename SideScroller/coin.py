import pygame
from gameobjects import GameObjects

class Coin(GameObjects):
    def __init__(self, position):
        super().__init__(position)
        self._images = []
        for x in range(1, 5):
            self.image = pygame.image.load(f'images/coins/coin{x}.png')
            self.image = pygame.transform.scale(self.image, (self._size * 1, self._size * 1))
            self._images.append(self.image)
        self._current = 1
        self.image = self._images[self._current]
        if self._current >= 4:
            self._current = 1
        self.image = self._images[int(self._current)]

        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0], self.position[1])

    def draw(self, window, scroll):
        window.blit(self.image, self.rect)
        self.rect.x += scroll

    def update(self):
        self._current += 0.12
        if self._current >= 4:
            self._current = 1
        self.image = self._images[int(self._current)]

    def add_coin(self, player):
        if self.rect.colliderect(player):
            player._score += 15
            self.kill()
            
