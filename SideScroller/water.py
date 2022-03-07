import pygame
from gameobjects import GameObjects

class Water(GameObjects):
    def __init__(self, position, image):
        super().__init__(position)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (self.position[0], self.position[1])

    def check_collision(self, player):
        self.check_player_collision()
        self.reset_position()

    def reset_position(self):
        pass # TODO reset player pos after water damage...
