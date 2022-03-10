import pygame
from gameobjects import GameObjects

class Weapon(GameObjects):
    def __init__(self, position, target):
        super().__init__(position)
        self._target = target
        self.image = pygame.image.load("images/attack.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.35, self.image.get_height() * 0.35))
        self._speed = 5
        self._state = False
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0], self.position[1])

    def update(self, player, enemy_group, bat_group, butterfly_group):
        self.rect.x += self._speed * self._target

        if self.rect.right <= 0 or self.rect.left >= 1160:
            self.kill()
        for enemy in enemy_group:
            if self.rect.colliderect(enemy):
                enemy._health -= 25
                player._score += 40
                self.kill()
        for bat in bat_group:
            if self.rect.colliderect(bat):
                bat._health -= 25
                player._score += 30
                self.kill()
        for butterfly in butterfly_group:
            if self.rect.colliderect(butterfly):
                butterfly._health -= 25
                player._score += 30
                self.kill()
