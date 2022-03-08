import pygame
import weapon
from gameobjects import GameObjects
from character import Character
import health
import tilemap


class Player(Character):
    def __init__(self, position, health):
        super().__init__(position, health)
        self._images = []
        self._images2 = []
        self._size = 48
        for x in range(1, 10):
            self.image = pygame.image.load(f'images/GirlWalkCycle/girl{x}.png')
            self.image = pygame.transform.scale(self.image, (self._size * 1, self._size * 1.5))
            self._images.append(self.image)
        for x in range(1, 10):
            self.image = pygame.image.load(f'images/GirlWalkCycle2/girl{x}.png')
            self.image = pygame.transform.scale(self.image, (self._size * 1, self._size * 1.5))
            self._images2.append(self.image)
        self._current = 1
        self.image = self._images2[self._current]
        self.image = self._images[self._current]
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0], self.position[1])
        self._moving_left = False
        self._moving_right = False
        self._w = self.image.get_width()
        self._h = self.image.get_height()
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
        self._xSpeed = 0
        self._ySpeed = 0
        self._gravity = 0.75
        self._in_air = False

    def __str__(self):
        return "%s" % self._position

    def check_moving_right(self):
        self._moving_right = True

    def update_right(self):
        if self._moving_right == True:
            self._current += 0.78
            if self._current >= 9:
                self._current = 1
            self.image = self._images[int(self._current)]

    def check_moving_left(self):
        self._moving_left = True

    def update_left(self):
        if self._moving_left == True:
            self._current += 0.78
            if self._current >= 9:
                self._current = 1
            self.image = self._images2[int(self._current)]

    def attack(self):
        if self._counter == 0:
            self._counter = 17
            if self._shot_direction == "R":
                shoot = weapon.Weapon([self.rect.x + 20, self.rect.y + 18], 1)
            if self._shot_direction == "L":
                shoot = weapon.Weapon([self.rect.x + 20, self.rect.y + 18], -1)
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
        self._remaining_health.empty()
        self._max_health -= 1
        self.update_health(self._max_health)

    def move(self, items):
        self._xSpeed = 0
        self._ySpeed = 0
        self.boundaries()
        self.jump()
        if self._right and not self._left:
            self._xSpeed = self._speed
        if self._left and not self._right:
            self._xSpeed -= self._speed
        for item in items:
            if item[1].colliderect(self.rect.x + self._xSpeed, self.rect.y, self._w, self._h):
                self._xSpeed = 0
            if item[1].colliderect(self.rect.x, self.rect.y + self._ySpeed, self._w, self._h):
                self._ySpeed = 0
        self.rect.x += self._xSpeed
        self.rect.y += self._ySpeed

    def jump(self):
        if self._jump and self._in_air == False:
            self._mass = -11
            self._jump = False
            self._in_air = True
        self._mass += self._gravity
        if self._mass > 10:
            self._mass
            self._in_air = False
        self._ySpeed += self._mass

    def add_inventory(self, item):
        if item not in self._inventory:
            self._inventory.append(item)