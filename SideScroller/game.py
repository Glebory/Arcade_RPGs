import player
import enemy
import pygame
import weapon
import health
import tiles
import tilemap
import leveldesign


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1160, 610))
        self._clock = pygame.time.Clock()
        self._player1 = player.Player([500, 500], 100)
        self._player1.update_health(self._player1._max_health)
        self._enemy1 = enemy.Enemy([750, 475], 100)
        self._state = False
        self._cooldown = 10000
        self._pause = pygame.time.get_ticks()
        self._tilemap = tilemap.TileMap()
        self._tilemap.parse_data(self._tilemap._map)

    #    s = levelsprites.LevelSprites("images/black-ground.png")
    #    self._level = tilemap.TileMap("alpha.csv", s)

    def game_loop(self):
        game_loop = True
        while game_loop:
            if self._player1._counter > 0:
                self._player1._counter -= 1
            self.window.fill((48, 51, 53))
            self._tilemap.draw()
            for tile in self._tilemap._items:
                self.window.blit(tile[0], tile[1])
            #self._level.draw(self.window)

            if self._player1.health > 0:
                self.window.blit(self._player1.image, self._player1.rect)
                self._player1.move()
                self._player1.jump()
                self._player1._remaining_health.draw(self.window)

            if self._enemy1._health > 0:
                self.window.blit(self._enemy1.image, self._enemy1.rect)
                self._enemy1.move()
                self._enemy1.check_player_collision(self._player1)

            if self._state == True:
                self._player1.attack()

            self._player1._weapon.update(self._enemy1)
            self._player1._weapon.draw(self.window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_loop = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_loop = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        self._player1._right = True
                    if event.key == pygame.K_a:
                        self._player1._left = True
                    if event.key == pygame.K_w:
                        self._player1._jump = True
                    if event.key == pygame.K_RIGHT:
                        self._state = True
                        self._player1._shot_direction = "R"
                    if event.key == pygame.K_LEFT:
                        self._state = True
                        self._player1._shot_direction = "L"

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self._player1._right = False
                    if event.key == pygame.K_a:
                        self._player1._left = False
                    if event.key == pygame.K_RIGHT:
                        self._state = False
                    if event.key == pygame.K_LEFT:
                        self._state = False

            #self._level.draw(self.window)
            self._clock.tick(70)
            pygame.display.update()
            print(self._clock)

        pygame.quit()


game = Game()
game.game_loop()
