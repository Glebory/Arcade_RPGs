import random

import pygame


class Button:
    def __init__(self, word, action, topleft, font_size, color=None, border=0):
        self._buffer = 6
        self._action = action
        self.topleft = topleft
        self._font_size = font_size
        self._size = self.make_size(word)
        self.border = border
        self.selected = False
        if color is None:
            self._color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        else:
            self._color = color
        self._rect = pygame.Rect(topleft[0],topleft[1], self._size[0], self._size[1])
        font = pygame.font.Font("images/256BYTES.ttf", self._font_size)
        self._word = font.render(word, True, "black")

    def select(self):
        self.selected = True

    def render(self, screen):
        if self.selected is True:
            self.border = 1
        else:
            self.border = 0
        if self.border == 0:
            pygame.draw.rect(screen, self._color, self._rect)
        else:
            pygame.draw.rect(screen, self._color, self._rect)
            pygame.draw.rect(screen, "black", self._rect, self.border)
        screen.blit(self._word, (self._rect.x + self._buffer, self._rect.y + self._buffer))

    def press(self):
        self._action()

    def make_size(self, word):
        size = ((self._font_size * len(word) + (self._buffer*2)), (self._font_size + (self._buffer*2)))
        print(size)
        return size

