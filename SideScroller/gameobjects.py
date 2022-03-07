import pygame

class GameObjects(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self._position = position
        self._image = None

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, new_image):
        self._image = new_image

    def check_player_collision(self, player):
        if self.rect.colliderect(player):
            player._health -= 1
            if player._health == self._segment:
                self._segment -= 25
                player.del_health()
