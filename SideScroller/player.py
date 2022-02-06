import pygame

import weapon
from gameobjects import GameObjects
from character import Character
import health


class Player(Character):
    def __init__(self, position, health):
        super().__init__(position, health)
        self.image = pygame.image.load("images/player11.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.3, self.image.get_height() * 0.3))
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0], self.position[1])
        self._left = False
        self._right = False
        self._jump = False
        self._direction = 1
        self._mass = 1
        self._velocity = 8
        self._speed = 4
        self._weapon = pygame.sprite.Group()
        self._remaining_health = pygame.sprite.Group()
        self._shot_direction = ""
        self._counter = 0
        self._max_health = 4

    def __str__(self):
        return "%s" % self._position

    def attack(self):
        if self._counter == 0:
            self._counter = 17
            if self._shot_direction == "R":
                shoot = weapon.Weapon([self.rect.x + 40, self.rect.y + 18], 1)
            if self._shot_direction == "L":
                shoot = weapon.Weapon([self.rect.x + 40, self.rect.y + 18], -1)
            self._weapon.add(shoot)

    def update_health(self, life):
        origin = 30
        for i in range(life):
            heart_collection = health.Health([origin, 30])
            origin += 60
            self._remaining_health.add(heart_collection)


    def add_health(self):
        pass

    def del_health(self):
        #if self._max_health > 2:
        self._remaining_health.empty()
        self._max_health -= 1
        print(self._max_health)
        self.update_health(self._max_health)


    def move(self):
        self._xSpeed = 0
        self._ySpeed = 0
        self.boundaries()
        if self._right and not self._left:
            self._xSpeed = self._speed
        if self._left and not self._right:
            self._xSpeed -= self._speed
        self.rect.x += self._xSpeed
        self.rect.y += self._ySpeed

    def jump(self):
        # 32
        force = (1 / 2) * self._mass * (self._velocity ** 2)
        if self._jump:
            self.rect.y -= force
            self.rect.x += 0.5
            self._velocity -= 1
            if self._velocity < 0:
                self._mass = -1
            if self._velocity == -9:
                self._jump = False
                self._velocity = 8
                self._mass = 1
        pygame.time.delay(20)
