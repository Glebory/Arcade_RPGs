import pygame
from gameobjects import GameObjects

class BossAttack(GameObjects):
    def __init__(self, position, target):
        super().__init__(position)
        self._target = target
        self.image = pygame.image.load("images/boss_attack.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.6, self.image.get_height() * 0.6))
        self._speed = 5
        self._state = False
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0], self.position[1])

    def update(self, player, items):
        self.rect.y -= self._speed * self._target
        self.rect.x += self._speed * self._target
        if self.rect.right <= 500 or self.rect.left >= 1160:
            self.kill()
        if self.rect.colliderect(player):
            player._health -= 25
        for item in items:
            if item[1].colliderect(self):
                self.kill()
