import player
import enemy
import pygame
import weapon
import health
import tilemap

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1160, 650))
        self._background = pygame.image.load("images/background4.jfif")
        self._clock = pygame.time.Clock()
        self._state = False
        self._cooldown = 10000
        self._pause = pygame.time.get_ticks()
        self._tilemap = tilemap.TileMap()
        self._tilemap.parse_data(self._tilemap._map)

    def game_loop(self):
        game_loop = True
        while game_loop:
            if self._tilemap._player1._counter > 0:
                self._tilemap._player1._counter -= 1
            self.window.fill((192, 68, 143))
            self.window.blit(self._background, [0,0])
            self._tilemap.draw()
            for water in self._tilemap._water:
                water[1][0] += self._tilemap._player1._screen_scroll
                self.window.blit(water[0], water[1])
            for respawn in self._tilemap._respawnpt:
                respawn[1][0] += self._tilemap._player1._screen_scroll
                self.window.blit(respawn[0], respawn[1])
            for tile in self._tilemap._items:
                tile[1][0] += self._tilemap._player1._screen_scroll
                self.window.blit(tile[0], tile[1])
            for tile in self._tilemap._coffin:
                tile[1][0] += self._tilemap._player1._screen_scroll
                self.window.blit(tile[0], tile[1])

            if self._tilemap._player1.health > 0:
                self.window.blit(self._tilemap._player1.image, self._tilemap._player1.rect)
                self._tilemap._player1._screen_scroll = self._tilemap._player1.move(self._tilemap._items, self._tilemap._water, self._tilemap._respawnpt, self._tilemap._coffin)
                self._tilemap._player1._remaining_health.draw(self.window)

                self._tilemap._player1.update_left()
                self._tilemap._player1.update_right()

            for enemy in self._tilemap._enemy_group:
                if enemy.health > 0:
                    enemy.draw(self.window, self._tilemap._player1._screen_scroll)
                    enemy.move()
                    enemy.check_player_collision(self._tilemap._player1)

            for coin in self._tilemap._coin_group:
                coin.draw(self.window, self._tilemap._player1._screen_scroll)
                coin.update()
                coin.add_coin(self._tilemap._player1)

            if self._state == True:
                self._tilemap._player1.attack()
            self._tilemap._player1._weapon.update(self._tilemap._enemy_group)
            self._tilemap._player1._weapon.draw(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_loop = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self._tilemap._player1._right = True
                        self._tilemap._player1.check_moving_right()
                    if event.key == pygame.K_a:
                        self._tilemap._player1._left = True
                        self._tilemap._player1.check_moving_left()
                    if event.key == pygame.K_w:
                        self._tilemap._player1._jump = True
                    if event.key == pygame.K_RIGHT:
                        self._state = True
                        self._tilemap._player1._shot_direction = "R"
                    if event.key == pygame.K_LEFT:
                        self._state = True
                        self._tilemap._player1._shot_direction = "L"
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self._tilemap._player1._right = False
                        self._tilemap._player1._moving_right = False
                    if event.key == pygame.K_a:
                        self._tilemap._player1._left = False
                        self._tilemap._player1._moving_left = False
                    if event.key == pygame.K_RIGHT:
                        self._state = False
                    if event.key == pygame.K_LEFT:
                        self._state = False
            self._clock.tick()
            pygame.display.update()
            print(self._clock)
        pygame.quit()

game = Game()
game.game_loop()
