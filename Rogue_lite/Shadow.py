import pygame
from GameObject import *


class Shadow(GameObject):
    def __init__(self, owner, buffer_x, buffer_y):
        super().__init__(owner)
        self.buffer_x = buffer_x
        self.owner = owner
        self.buffer_y = buffer_y
        self.image = pygame.image.load("images/shadow.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = owner._rect.x + buffer_x
        self.rect.y = owner._rect.y + buffer_y


    def update(self):
        self.rect.x = self.owner.rect.x + self.buffer_x
        self.rect.y = self.owner.rect.y + self.buffer_y

    def render(self, screen):
        screen.blit(self._image, self._rect)
        pygame.draw.rect(screen, "yellow", self.rect, 1)

