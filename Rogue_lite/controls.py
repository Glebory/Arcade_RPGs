import pygame
def check_keypress(event, player):
    if event.key == pygame.K_w:
        player.mv_up()
        player.state = "moving"
        player.weapon.state = "moving"
    if event.key == pygame.K_s:
        player.mv_down()
        player.state = "moving"
        player.weapon.state = "moving"
    if event.key == pygame.K_a:
        player.mv_left()
        player.state = "moving"
        player.weapon.state = "moving"
    if event.key == pygame.K_d:
        player.mv_right()
        player.state = "moving"
    player.weapon.state = "moving"

    if event.key == pygame.K_UP:
        player.attack_up()
    if event.key == pygame.K_DOWN:
        player.attack_down()
    if event.key == pygame.K_LEFT:
        player.attack_left()
    if event.key == pygame.K_RIGHT:
        player.attack_right()
    if event.key == pygame.K_SPACE:
        player.use_item()


def key_up(event, player):
    if event.key == pygame.K_w or event.key == pygame.K_s:
        player.y_change = 0
        player.weapon.y_change = 0

    if event.key == pygame.K_a or event.key == pygame.K_d:
        player.x_change = 0
        player.weapon.x_change = 0

    if player.x_change == 0 and player.y_change == 0:
        player.stop()

    if event.key == pygame.K_UP:
        player.attack_up()
    if event.key == pygame.K_DOWN:
        player.attack_down()
    if event.key == pygame.K_LEFT:
        player.attack_left()
    if event.key == pygame.K_RIGHT:
        player.attack_right()
    if event.key == pygame.K_SPACE:
        player.use_item()


