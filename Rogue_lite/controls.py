import pygame
def check_keypress(event, handler):
    if handler.state == "running":
        player = handler.player_group.sprites()[0]
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

    if handler.state == "main menu":
        if event.key == pygame.K_w:
            handler.menu.select_button_above()
        if event.key == pygame.K_s:
            handler.menu.select_button_below()
        if event.key == pygame.K_SPACE:
            handler.menu.press()
    if event.key == pygame.K_p:
        handler.pause()


def key_up(event, handler):
    if handler.state == "running":
        player = handler.player_group.sprites()[0]
        if event.key == pygame.K_w or event.key == pygame.K_s:
            player.y_change = 0
            player.weapon.y_change = 0

        if event.key == pygame.K_a or event.key == pygame.K_d:
            player.x_change = 0
            player.weapon.x_change = 0

        if player.x_change == 0 and player.y_change == 0:
            player.stop()

        if event.key == pygame.K_UP and event.key == pygame.K_DOWN and event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
            player.weapon.state = "standby"



