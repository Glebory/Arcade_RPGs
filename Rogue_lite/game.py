import pygame
import sys
import controls
from all_characters import *


from enemy import *
import random
from handler import *

def game():
    handler = Handler()

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                controls.check_keypress(event, handler)
            if event.type == pygame.KEYUP:
                controls.key_up(event,handler)
        handler.render()




game()
