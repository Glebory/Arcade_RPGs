import pygame
from Player import *
from Gui import *

def game(height, width):
    pygame.init()
    # Set up screen
    screen = pygame.display.set_mode((height, width))
    pygame.display.set_caption("Rogue_lite")
    icon = pygame.image.load('images/Heart.png')
    pygame.display.set_icon(icon)


    playerImg = pygame.image.load('images/Gimbo.png')
    playerImg = pygame.transform.scale(playerImg, (32,64))
    player = Player(25, 25, playerImg)
    objects = [player]
    gui = Gui(screen, objects, height, width)

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gui.render()
        pygame.display.update()

game(800, 600)
