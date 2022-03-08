import random

import pygame

from Arcade_RPGs.Rogue_lite.Gui import Gui
from Arcade_RPGs.Rogue_lite.all_characters import gimbo
from Arcade_RPGs.Rogue_lite.enemy import Enemy


class Handler():
    def __init__(self):
        pygame.init()
        flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
        # Set up screen
        # Find the size of the screen
        info = pygame.display.Info()
        self._background = pygame.image.load('images/beachBG.png')
        self._objects = pygame.sprite.Group()
        self._size = info.current_w, info.current_h
        self._window = pygame.display.set_mode(self._size, flags, 16)
        self._screen = pygame.Surface((640, 480))
        pygame.display.set_caption("Rogue_lite")
        icon = pygame.image.load('images/ui/Heart.png')
        pygame.display.set_icon(icon)
        self._clock = pygame.time.Clock()
        self._font = pygame.font.SysFont("Arial", 11)
        self.player_group = pygame.sprite.GroupSingle()
        self.enemy_group = pygame.sprite.Group()
        self.set_up_room()
        self._gui = Gui(self._screen, self._objects, 480, 640)
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
        pygame.mouse.set_visible(False)


    def set_up_room(self):
        player = gimbo((25,25), self)
        self.player_group.add(player)
        enemies = [Enemy("Plastic Bottle Boy", (random.randint(0, self._size[0] - 16),
                         random.randint(0, self._size[1] - 16)), self) for enemy in range(5)]
        self._objects.add(player)
        for enemy in enemies:
            self.enemy_group.add(enemy)
            self._objects.add(enemy)

    def render(self):
        self._screen.blit(self._background, (0, 0))
        self.collide_check()
        self._objects.update(self._size[1], self._size[0])
        for object in self._objects:
            object.render(self._screen)
        self._clock.tick()
        self._screen.blit(self._font.render(str(self._clock.get_fps()),1,pygame.Color("Green")),(0,0))
        self._window.blit(pygame.transform.scale(self._screen,self._size),(0,0))
        pygame.display.update()

    def get_objects(self):
        return self._objects

    def set_objects(self, objects):
        self._objects = objects

    objects = property(get_objects, set_objects)

    def collide_check(self):
        for object in self._objects:
            if object._y < 0:
                object._y = 0
            elif object._x < 0:
                object._x = 0
            if object._x > self._size[0] - 16:
                object._x = self._size[0] - 16
            elif object._y > self._size[1] - 32:
                object._y= self._size[1] - 32

