import pygame


class Menu:
    def __init__(self, handler, topleft,color = "white", buffer=6, border=0):
        self.buttons = []
        self.handler = handler
        self._size = [20, 10]
        self.buffer = buffer
        self._rect = pygame.Rect(topleft, self._size)
        self.border = border
        self.color = color

    def add_button(self, button):
        self.buttons.append(button)
        if button.rect.width + self.buffer > self._size[0]:
            self._size[0] = button.rect.width + self.buffer
        if button._font_size + self.buffer > self._size[1]:
            self._size[1] = button._font_size + self.buffer

    def render(self, screen):
        if self.border == 0:
            pygame.draw.rect(screen, self.color, self._rect, self.border)
        else:
            pygame.draw.rect(screen, self.color, self._rect)
            pygame.draw.rect(screen, "black", self._rect, self.border)
        for button in self.buttons:
            button.render(screen)