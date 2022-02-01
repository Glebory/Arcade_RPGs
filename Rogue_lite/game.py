import pygame
import sys
import controls
from Weapon import *
from Player import *
from Gui import *
from enemy import *
import random

def game(height, width):
    pygame.init()
    flags = pygame.FULLSCREEN | pygame.DOUBLEBUF

    # Set up screen
    # Find the size of the screen
    info = pygame.display.Info()
    size = w,h = info.current_w, info.current_h
    window = pygame.display.set_mode(size,flags, 16)
    screen = pygame.Surface((640,480))
    pygame.display.set_caption("Rogue_lite")
    icon = pygame.image.load('images/ui/Heart.png')
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial",11)
    weapon = Weapon(25,25, "G-Shot")

    player = Player(25, 25, weapon)
    enemy = Enemy(random.randint(0,size[0]-16),random.randint(0, size[1]-16))
    objects = [weapon, player, enemy]
    gui = Gui(screen, objects,480,640)
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                controls.check_keypress(event,player)
            if event.type == pygame.KEYUP:
                controls.key_up(event,player)

        gui.render()
        clock.tick()
        screen.blit(font.render(str(clock.get_fps()),1,pygame.Color("Green")),(0,0))
        window.blit(pygame.transform.scale(screen,size),(0,0))
        pygame.display.update()

game(800, 600)
