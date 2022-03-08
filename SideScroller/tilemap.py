import csv
import os
import pygame
import player
import enemy
import stairs
import cave


class TileMap:
    def __init__(self):
        self._level = 2
        self._rows = 15
        self._cols = 150
    #    self._size = 1160 // self._rows
        self._size = 48
        self._types = 27  # NUMBER OF DIFFERENT TILES USED
        self.images = []
        self._map = []
        self._items = []
        self._water = []
        self._coffin = []
        self._respawnpt = []
        self._cave_group = pygame.sprite.Group()
        self._enemy_group = pygame.sprite.Group()
        self.update()
        self.draw()

    def update(self):
        for row in range(self._rows):
            row = [-1] * self._cols
            self._map.append(row)
        with open(f'level{self._level}.csv') as f:
            file = csv.reader(f, delimiter=',')
            for x, row in enumerate(file):
                for y, tile in enumerate(row):
                    self._map[x][y] = int(tile)

    def draw(self):
        for x in range(self._types):
            self.image = pygame.image.load(f'images/tiles/tile{x}.png')
            self.image = pygame.transform.scale(self.image, (self._size, self._size))
            self.images.append(self.image)

    def parse_data(self, data):
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile != -1:
                    self.image = self.images[tile]
                    self.rect = self.image.get_rect()
                    self.rect.center = (x * self._size, y * self._size)
                    self._data = (self.image, self.rect)
                    if tile >= 0 and tile <= 6 and tile != 4 or tile == 21 or tile == 26: # ground tiles ..
                        self._items.append(self._data)
                    elif tile == 4:
                        self._coffin.append(self._data)
                    elif tile >= 7 and tile <= 12: # stairs
                        self._items.append(self._data)
                    elif tile >= 13 and tile <= 16: # water
                        self._water.append(self._data)
                    elif tile == 17 or tile == 18:
                        self._items.append(self._data)
                    elif tile == 19 or tile == 20: # cave
                        self._upper_cave = cave.Cave([self._size * x, self._size * y], pygame.image.load("images/tiles/tile19.png"))
                        self._lower_cave = cave.Cave([self._size * x, self._size * y], pygame.image.load("images/tiles/tile20.png"))
                        self._items.append(self._data)
                    elif tile == 22:
                        pass # end of level
                    elif tile == 23:
                        self._player1 = player.Player([49.5 * x, 46.8 * y], 100) # player movements
                        self._player1.update_health(self._player1._max_health)
                        self._player1.move(self._items, self._water, self._respawnpt, self._coffin)
                    elif tile == 24: # enemy
                        self._enemy1 = enemy.Enemy([49.5 * x, 46.8 * y], 100)
                        self._enemy_group.add(self._enemy1)
                    elif tile == 25: # spawn point
                        self._respawnpt.append(self._data)
