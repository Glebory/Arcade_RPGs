import pygame
from gameobjects import GameObjects
from character import Character


class Enemy(Character):
    def __init__(self, position, health):
        super().__init__(position, health)
        self._images = []
        self._images2 = []
        self._size = 48
        for x in range(1, 9):
            self.image = pygame.image.load(f'images/BagManCycle/bagguy{x}.png')
            self.image = pygame.transform.scale(self.image, (self._size * 1, self._size * 1.5))
            self._images.append(self.image)
        for x in range(1, 9):
            self.image = pygame.image.load(f'images/BagManCycle2/bagguy{x}.png')
            self.image = pygame.transform.scale(self.image, (self._size * 1, self._size * 1.5))
            self._images2.append(self.image)
        self._current = 6
        self.image = self._images[self._current]
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0], self.position[1])
        self._direction = 1
        self._speed = 2
        self._data = (self.image, self.rect)


    def __str__(self):
        return "%s" % (self._position)

    def draw(self, window):
        window.blit(self.image, self.rect)

    def move(self, screen_scroll): #84
        if self._direction == 1:
            if self.rect.x + self._speed <= self._position[0] + 60:
                self.rect.x += self._speed
                self._current += 0.25
                if self._current >= 8:
                    self._current = 1
                self.image = self._images[int(self._current)]
                self.rect.x += screen_scroll
            else:
                self._direction = -1
        if self._direction == -1:
            if self.rect.x - self._speed >= self._position[0] - 60:
                self.rect.x -= self._speed
                self._current += 0.25
                if self._current >= 8:
                    self._current = 1
                self.image = self._images2[int(self._current)]
            else:
                self._direction = 1

        self.rect.x += screen_scroll
