import pygame
from gameobjects import GameObjects
from character import Character


class Enemy(Character):
    def __init__(self, position, health):
        super().__init__(position, health)
        self.image = pygame.image.load("images/char.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 2, self.image.get_height() * 2))
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0], self.position[1])
        self._direction = 1
        self._speed = 2


    def __str__(self):
        return "%s" % (self._position)

    def move(self):
        if self._direction == 1:
            if self.rect.x + self._speed <= self._position[0] + 80:
                self.rect.x += self._speed
            else:
                self._direction = -1
        else:
            if self.rect.x - self._speed > self._position[0] - 80:
                self.rect.x -= self._speed
            else:
                self._direction = 1

    def check_player_collision(self, player):
        if self.rect.colliderect(player):
            player._health -= 1
            if player._health == self._segment:
                self._segment -= 25
                player.del_health()
