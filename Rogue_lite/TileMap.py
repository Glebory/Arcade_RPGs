from all_tiles import *
import random
from PIL import Image


class TileMap:
    def __init__(self, size):
        self.size = size
        self.map = self.random_map()
        self.room_imgs = beach_images()


    def random_tile(self, x, y, matrix, row):
        return

    def render(self, screen):
        screen.blit(self.image, (0, 0))
        return

    def return_map(self):
        for line in self.map:
            print(str(line) + "\n")
        return self.map

    # def render(self, screen):


def main():
    import pygame
    pygame.init()
    info = pygame.display.Info()
    size = w, h = info.current_w, info.current_h
    screen = pygame.display.set_mode(size)
    tilemap = TileMap(size)
    tilemap.return_map()
    tilemap.render(screen)


if __name__ == '__main__':
    main()
