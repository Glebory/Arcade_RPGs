import csv
import os
import pygame
import player
import enemy
import stairs
import water

class TileMap:
    def __init__(self):
        self._level = 1
        self._rows = 19
        self._cols = 150
    #    self._size = 1160 // self._rows
        self._size = 48
        self._types = 25  # NUMBER OF DIFFERENT TILES USED
        self.images = []
        self._map = []
        self._items = []
        self._obstacles = []
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
                    if tile >= 0 and tile <= 6 or tile == 21: # ground tiles ..
                        self._items.append(self._data)
                    elif tile >= 7 and tile <= 12: # stairs
                        self._stairs = stairs.Stairs([self._size * x, self._size * y])
                    elif tile >= 13 and tile <= 16: # water
                        self._water = water.Water([self._size * x, self._size *y], pygame.image.load("images/tiles/tile13.png"))
                        self._coffin_water = water.Water([self._size * x, self._size *y], pygame.image.load("images/tiles/tile14.png"))
                        self._mid_water = water.Water([self._size * x, self._size *y], pygame.image.load("images/tiles/tile15.png"))
                        self._water_floor = water.Water([self._size * x, self._size *y], pygame.image.load("images/tiles/tile16.png"))
                    elif tile == 17 or tile == 18:
                        self._items.append(self._data)
                    elif tile == 19 or tile == 20:
                        pass #cave
                    elif tile == 22:
                        pass # end of level
                    elif tile == 23:
                        self._player1 = player.Player([49.5 * x, 45.8 * y], 100) # player movements
                        self._player1.update_health(self._player1._max_health)
                        self._player1.move(self._items)
                    elif tile == 24:
                        self._enemy1 = enemy.Enemy([self._size * x, self._size * y], 100)
                        
