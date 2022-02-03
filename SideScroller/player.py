import pygame

import weapon
from gameobjects import GameObjects


class Player(GameObjects):
    def __init__(self, position):
        super().__init__(position)
        self.image = pygame.image.load("images/player11.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.3, self.image.get_height() * 0.3))
        self._left = False
        self._right = False
        self._jump = False
        self._direction = 1
        self._mass = 1
        self._velocity = 8
        self._speed = 4
        self._weapon = pygame.sprite.Group()
        self._shot_direction = ""
        self._counter = 0

    def __str__(self):
        return "%s" % self._position

    def attack(self):
        if self._counter == 0:
            self._counter = 17
            if self._shot_direction == "R":
                shoot = weapon.Weapon([self.position[0] + 40, self.position[1] + 18], 1)
            if self._shot_direction == "L":
                shoot = weapon.Weapon([self.position[0] + 40, self.position[1] + 18], -1)
            self._weapon.add(shoot)

    def move(self):
        self._xSpeed = 0
        self._ySpeed = 0
        if self._position[0] <= 0:
            self._position[0] = 0
        elif self._position[0] >= 1100:
            self._position[0] = 1100
        if self._right and not self._left:
            self._xSpeed = self._speed
        if self._left and not self._right:
            self._xSpeed -= self._speed
        self._position[0] += self._xSpeed
        self._position[1] += self._ySpeed


    def jump(self):
        # 32
        force = (1 / 2) * self._mass * (self._velocity ** 2)
        if self._jump:
            self._position[1] -= force
            self._position[0] += 0.5
            self._velocity -= 1
            if self._velocity < 0:
                self._mass = -1
            if self._velocity == -9:
                self._jump = False
                self._velocity = 8
                self._mass = 1
        pygame.time.delay(20)
