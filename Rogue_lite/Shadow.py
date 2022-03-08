import pygame
from GameObject import *
import pygame.gfxdraw

class Shadow(GameObject):
    def __init__(self, owner):
        super().__init__(owner)
        self._x = owner._x+(owner.rect.width//4)
        self._y = owner._y + owner.rect.height
        self._xr = owner._rect.width//4
        self._yr = 4
        self.color = pygame.Color(1,1,1,a=200)
        self.rect = self.image.get_rect()
        self.rect.center = [self._x, self._y]

    def render(self, screen):
        pygame.gfxdraw.filled_ellipse(screen, self._x, self._y, self._xr, self._yr, self.color)
