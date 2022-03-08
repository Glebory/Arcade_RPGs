import pygame
import Bullet

def reg_bullet(direction, spawn, handler):
    type = 'reg'
    x_change = 3 * direction[0]
    y_change = 3 * direction[1]
    image = pygame.image.load('images/bullet.png')
    damage = 2
    print('Spawn vvv')
    bullet = Bullet.Bullet('regular bullet', spawn, image, type, damage, x_change, y_change, handler)
    return bullet
