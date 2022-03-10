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
        self.damage = 5
        self._rect = self.image.get_rect(topleft=(spawn))

    def update(self):
        self.rect.x += self._x_change
        self.rect.y += self._y_change
        if self.rect.x < 0 or self.rect.y < 0 or self.rect.x > self.handler._size[0] or self.rect.y > self.handler._size[1]:
            self.destroy()
        self._rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))

    def destroy(self):
        self.kill()
