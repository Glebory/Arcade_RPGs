import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, image=None):
        super().__init__()
        if image is None:
            image = [pygame.image.load('images/Error.png').convert_alpha()]
        self._image = image
        self.rect = self._image.get_rect(topleft=(x,y))

    def update(self):
        return

    def render(self, screen):
        screen.blit(self._image, (self.rect))