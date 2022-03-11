import pygame
from enemy import Enemy
import bossattack

class ArmMan(Enemy):
    def __init__(self, position, health):
        super().__init__(position, health)
        self._images = []
        self._size = 48
        for x in range(1, 9):
            self.image = pygame.image.load(f'images/ArmManCycle/handman{x}.png')
            self.image = pygame.transform.scale(self.image, (self._size * 2.5, self._size * 4.5))
            self._images.append(self.image)
        self._images2 = self._images
        self._current = 1
        self.image = self._images[self._current]
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0], self.position[1])
        self._max = 6
        self._weapon = pygame.sprite.Group()
        self._counter = 0

    def attack(self):
        if self._counter == 0:
            self._counter = 17
            shoot = bossattack.BossAttack([self.rect.x + 20, self.rect.y + 50], -1)
            self._weapon.add(shoot)
