from GameObject import *

class MovingObject(GameObject):
    def __init__(self, x, y, image):
        super().__init__(x, y, image)
        self._x_change = 0.1
        self._y_change = 0

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