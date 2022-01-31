class GameObject:
    def __init__(self, x, y, image):
        self._x = x
        self._y = y
        self._image = image

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

    def tick(self):
        return

    def render(self, screen):

        screen.blit(self._image, (self._x, self._y))
