import pygame
import sys
import controls
from Player import *
from Gui import *

def game(height, width):
    pygame.init()
    # Set up screen
    # Find the size of the screen
    info = pygame.display.Info()
    size = w,h = info.current_w, info.current_h
    window = pygame.display.set_mode(size)
    screen = pygame.Surface((640,480))
    pygame.display.set_caption("Rogue_lite")
    icon = pygame.image.load('images/Heart.png')
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial",11)


    player = Player(25, 25)
    objects = [player]
    gui = Gui(screen, objects,640,480)

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
