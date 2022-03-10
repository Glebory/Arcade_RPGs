import pygame.sprite


class Ui(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image

    def render(self, screen):
        screen.blit(self._image, (self.x,self.y))
