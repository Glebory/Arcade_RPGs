import pygame

class GameObjects(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self._position = position
        self._image = None
        self._scroll = 200
        self._size = 48
        self._vertical_scroll = 50
        self._screen_scroll = 0
        self._wallpaper_scroll = 0
    #    pygame.font.init()
        self._font = pygame.font.Font("C:\WINDOWS\FONTS\AGENCYR.TTF", 32)
        self._score = 0

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

    def display_score(self, window):
        current_score = self._font.render("Score: " + str(self._score), True, (0, 0, 0))
        window.blit(current_score, (500, 0))
