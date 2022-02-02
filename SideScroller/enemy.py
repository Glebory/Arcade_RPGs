import pygame

class Enemy:
    def __init__(self, size, position, health):
        character.__init__(self, size, position, health)

    def __str__(self):
        return "%s %s %s" % (self.size, self.position, self.health)

    def create_enemy(self):
        default_enemy = pygame.image.load("char.png")
