import pygame


class Tile():
    def __init__(self, x, y, image=None):
        if image is None:
            image = [pygame.image.load('images/Error.png').convert_alpha()]
        self._x = x
        self._y = y
        self._image = image

    def tick(self):
        return

    def render(self,screen):
        screen.blit(self._image, (self._x, self._y))