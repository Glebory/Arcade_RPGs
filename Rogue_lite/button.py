import random

import pygame


class Button:
    def __init__(self, word, action, topleft, font_size, color=None, border=0):
        self._word = word
        self._action = action
        self.topleft = topleft
        self._font_size = font_size
        self._size = self.make_size()
        self.border = border
        if color is None:
            self._color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            self._color = color
        self._rect = pygame.Rect(topleft, self._size)

    def render(self, screen):
        if self.border == 0:
            pygame.draw.rect(screen, self.color, self._rect, self.border)
        else:
            pygame.draw.rect(screen, self.color, self._rect)
            pygame.draw.rect(screen, "black", self._rect, self.border)

    def make_size(self):
        buffer = 6
        size = self._font_size * len(self._word) + buffer, self._font_size + buffer
        return size

