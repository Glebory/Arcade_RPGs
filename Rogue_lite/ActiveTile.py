from tile import *


class ActiveTile(Tile):
    def __init__(self, x, y, images):
        super().__init__( x, y)
        self._images = images
        self._index = 0
        self._image = images[self._index]
        self._frames = 40

    def tick(self):
        self._index += 1

        if self._index >= len(self._images) * self._frames:
            self._index = 0

        self._image = self._images[self._index // self._frames]
