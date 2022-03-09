import random

import pygame
from Player import *
from Arcade_RPGs.Rogue_lite.Gui import Gui
from Arcade_RPGs.Rogue_lite.all_characters import gimbo
from Arcade_RPGs.Rogue_lite.enemy import Enemy
import TileMap
import all_tiles
import maps

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
        self.unmovable_group = pygame.sprite.Group()
        self.enemy_group_shadow = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        self.set_up_room()
        self._gui = Gui(self._screen, self._objects, 480, 640)
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
        pygame.mouse.set_visible(False)


    def set_up_room(self):
        player = gimbo((25,25), self)
        self.player_group.add(player)
        enemies = [Enemy("Plastic Bottle Boy", (random.randint(0, 640 - 16),
                         random.randint(0, 480 - 16)), self, 20) for enemy in range(5)]
        self._objects.add(player)
        for enemy in enemies:
            self.enemy_group.add(enemy)
            self._objects.add(enemy)
        TileMap.set_up_room(all_tiles.beach_images(), maps.beach_level,self)

    def render(self):
        self._screen.blit(self._background, (0, 0))
        self.collide_check()
        self._objects.update()
        self.unmovable_group.update()
        for object in self._objects:
            object.render(self._screen)
        for object in self.unmovable_group:
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
            if object.rect.y < 0:
                object.rect.y = 0
            elif object.rect.x < 0:
                object.rect.x = 0
            if object.rect.x > 640 - object.rect.width:
                object.rect.x = 640 - object.rect.width
            elif object.rect.y > 480 - object.rect.height:
                object.rect.y= 480 - object.rect.height
            if isinstance(object, Player):
                pygame.draw.rect(self._screen, "yellow", object._shadow.rect)
                for enemy in self.enemy_group:
                    if pygame.sprite.collide_rect(enemy.shadow,object):
                        pygame.draw.rect(self._screen, "Red", object._shadow.rect)
                        object.health -= enemy.damage

        for enemy in self.enemy_group:
            for bullet in self.player_bullets:
                pygame.draw.rect(self._screen, "red", bullet.rect)
                if pygame.sprite.collide_rect(enemy.shadow, bullet):
                    enemy.health -= bullet.damage
                    bullet.destroy()
            for enemy2 in self.enemy_group:
                if pygame.sprite.collide_rect(enemy.shadow,enemy2.shadow):
                    self.soft_colision(enemy,enemy2)

    def soft_colision(self, object1, object2):
        collision_tolerance = 8
        if abs(object1.rect.top - object2.rect.bottom) < collision_tolerance:
            object2.rect.y = object1.rect.y - object2.rect.height - 1
        if abs(object1.rect.bottom - object2.rect.top) < collision_tolerance:
            object2.rect.y = object1.rect.y + object1.rect.height + 1
        if abs(object1.rect.right - object2.rect.left) < collision_tolerance:
            object2.rect.x = object1.rect.x + object1.rect.width + 1
        if abs(object1.rect.left - object2.rect.right) < collision_tolerance:
            object2.rect.x = object1.rect.x - object2.rect.width - 1