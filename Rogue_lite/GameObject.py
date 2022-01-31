import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, images=[pygame.image.load('images/Error.png')]):
        pygame.sprite.Sprite.__init__(self)
        self._x = x
        self._y = y
        self._images = images
        self._index = 0
        self._image = self._images[self._index]
        self._speed = 0
        self._x_change = 0
        self._y_change = 0

    def get_x(self):
        return self._x

    def set_x(self, val):
        self._x = val
        return
    x_coord= property(get_x,set_x)

    def get_y(self):
        return self._y

    def set_y(self, val):
        self._y = val
        return
    y_coord = property(get_y, set_y)

    def get_image(self):
        return self._image

    def set_image(self, image):
        self._image = image
        return
    image = property(get_image, set_image)

    def get_x_change(self):
        return self._x_change

    def set_x_change(self, val):
        self._x_change = val
        return

    x_change = property(get_x_change, set_x_change)

    def get_y_change(self):
        return self._y_change

    def set_y_change(self, val):
        self._y_change = val
        return

    y_change = property(get_y_change, set_y_change)

    def get_speed(self):
        return self._speed

    def set_speed(self, val):
        self._speed = val
        return

    speed = property(get_speed, set_speed)

    def tick(self, h, w):
        self.x_coord += self._x_change
        self.y_coord += self._y_change
        if self._x < 0:
            self._x = 0
        elif self._y < 0:
            self._y = 0

        if self._x > w:
            self._x = w
        elif self._y > h:
            self._y = h


    def render(self, screen):
        screen.blit(self._image, (self._x, self._y))
