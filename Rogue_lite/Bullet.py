from GameObject import *


class Bullet(GameObject):
    def __init__(self, name, spawn, image, damage, speed, x_change, y_change, handler):
        print(spawn)
        super().__init__(name, spawn)
        self.handler = handler
        self.type = type
        self._x_change = x_change
        self._y_change = y_change
        self.speed = speed
        self.image = image
        self.damage = damage
        print('bullet made')

        def update(self, h, w):
            self.x_coord += self._x_change
            self.y_coord += self._y_change
            if self._x < 0 or self._y < 0 or self._x > w or self._y > h:
                self.destroy()

        def destroy(self):
            self.handler._objects.remove(self)

