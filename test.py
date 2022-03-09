from all_tiles import *
import random
from PIL import Image


class TileMap:
    def __init__(self, size):
        self.size = size
        self.map = self.random_map()
        self.room_imgs = beach_images()
        self.image = self.stitch_map()

    def merge_images_r(self, file1, file2):
        """Merge two images into one, displayed side by side
        :param file1: path to first image file
        :param file2: path to second image file
        :return: the merged Image object
        """
        image1 = Image.open(file1)
        image2 = Image.open(file2)

        (width1, height1) = image1.size
        (width2, height2) = image2.size

        result_width = width1 + width2
        result_height = max(height1, height2)

        result = Image.new('RGB', (result_width, result_height))
        result.paste(im=image1, box=(0, 0))
        result.paste(im=image2, box=(width1, 0))
        return result

    def merge_images_d(self, file1, file2):
        """Merge two images into one, displayed side by side
        :param file1: path to first image file
        :param file2: path to second image file
        :return: the merged Image object
        """
        image1 = Image.open(file1)
        image2 = Image.open(file2)

        (width1, height1) = image1.size
        (width2, height2) = image2.size

        result_width = max(width1, width2)
        result_height = height1 + height2

        result = Image.new('RGB', (result_width, result_height))
        result.paste(im=image1, box=(0, 0))
        result.paste(im=image2, box=(0, height1))
        return result

    def random_map(self):
        matrix = []
        for y in range(self.size[1] // 32 + 1):
            row = []
            for x in range(self.size[0] // 32 + 1):
                if y == 0 or x == 0 or x == (self.size[0] // 32):
                    tile = 1
                elif y == (self.size[1] // 32):
                    tile = 2
                else:
                    tile = 0
                row.append(tile)
            matrix.append(row)
        return matrix

    def stitch_map(self):
        j = 0
        for line in self.map:
            partial_image = None
            i = 0
            for val in line:
                if i == 0:
                    merged = self.room_imgs[val]
                else:
                    merged = self.merge_images_r(merged, self.room_imgs[val])
                i += 1
            if j == 0:
                partial_image = merged
            else:
                partial_image = self.merge_images_d(partial_image, merged)
            j += 1
        return partial_image

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
