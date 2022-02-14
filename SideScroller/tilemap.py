import csv
import os
import pygame

class TileMap:
    def __init__(self):
        self._level = 1
        self._rows = 19
        self._cols = 150
        self._size = 1160 // self._rows
        self._types = 1  # NUMBER OF DIFFERENT TILES USED
        self._images = []
        self._map = []
        self._items = []
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
            print(self._map)

    def draw(self):
        for x in range(self._types):
            self._image = pygame.image.load(f'images/tiles/tile{x}.png')
            self._image = pygame.transform.scale(self._image, (self._size, self._size))
            self._images.append(self._image)

    def parse_data(self, data):
        for x, row in enumerate(data):
            for y, tile in enumerate(row):
                if tile != -1:
                    self._image = self._images[tile]
                    self.rect = self._image.get_rect()
                    self.rect.center = (x * self._size, y * self._size)
                    self._data = (self._image, self.rect)
                    if tile >= 0 and tile <= 4:   #different ground tiles
                        self._items.append(self._data)
                    elif tile >= 5:  # check for water tile
                        pass

                    # TODO: check for boxes e.g. cages, item boxes ect..
                    # TODO:  check for characters ...
                    # e.g. elif tile == x:
            #        self._player1 = player.Player([x * self._size, y * self._size], 100)
            #        self._player1.update_health(self._player1._max_health)
#        return self._player1
