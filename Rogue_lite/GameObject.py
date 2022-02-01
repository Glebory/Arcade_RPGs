import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, images=None):
        pygame.sprite.Sprite.__init__(self)
        if images is None:
            images = [pygame.image.load('images/Error.png').convert_alpha()]
        self._x = x
        self._y = y
        self._images = images
        self._index = 0
        self._image = self._images[self._index]
        self._speed = 0
        self._x_change = 0
        self._y_change = 0
        self._state = "stopped"
        self._frames = 20

    def get_x(self):
        return self._x

    def set_x(self, val):
        self._x = val
        return

    x_coord = property(get_x, set_x)

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

    def get_images(self):
        return self._images

    def set_images(self, image_list):
        self._images = image_list
        return

    images = property(get_images, set_images)

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

    def get_index(self):
        return self._index

    def set_index(self, index):
        self._index = index
        return

    index = property(get_index, set_index)

    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state
        return

    state = property(get_state, set_state)

    def get_frames(self):
        return self._frames

    def set_frames(self, frames):
        self._frames = frames
        return

    frames = property(get_frames, set_frames)

    def tick(self, h, w):
        self.x_coord += self._x_change
        self.y_coord += self._y_change
        if self.state == "moving":
            self.index += 1

            if self.index >= len(self.images) * self.frames:
                self.index = 0

            self.image = self.images[self.index // self.frames]

        if self._x < 0:
            self._x = 0
        elif self._y < 0:
            self._y = 0

        if self._x > w - 16:
            self._x = w - 16
        elif self._y > h - 32:
            self._y = h - 32

    def render(self, screen):
        screen.blit(self._image, (self._x, self._y))
