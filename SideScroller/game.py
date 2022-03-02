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
        self._background = pygame.image.load("images/background3.png")
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
            for tile in self._tilemap._items:
                self.window.blit(tile[0], tile[1])

            if self._tilemap._player1.health > 0:
                self.window.blit(self._tilemap._player1.image, self._tilemap._player1.rect)
                self._tilemap._player1.move()
                self._tilemap._player1.jump()
                self._tilemap._player1._remaining_health.draw(self.window)

            if self._tilemap._enemy1._health > 0:
                self.window.blit(self._tilemap._enemy1.image, self._tilemap._enemy1.rect)
                self._tilemap._enemy1.move()
                self._tilemap._enemy1.check_player_collision(self._tilemap._player1)

            if self._state == True:
                self._tilemap._player1.attack()

            self._tilemap._player1._weapon.update(self._tilemap._enemy1)
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
                    if event.key == pygame.K_a:
                        self._tilemap._player1._left = True
                    if event.key == pygame.K_w:
                        self._tilemap._player1._jump = True
                    if event.key == pygame.K_RIGHT:
                        self._state = True
                        self._tilemap._player1._shot_direction = "R"
                    if event.key == pygame.K_LEFT:
                        self._state = True
                        self._tilemap._player1._shot_direction = "L"
                    if event.key == pygame.K_e:
                        self._tilemap._player1.add_inventory()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self._tilemap._player1._right = False
                    if event.key == pygame.K_a:
                        self._tilemap._player1._left = False
                    if event.key == pygame.K_RIGHT:
                        self._state = False
                    if event.key == pygame.K_LEFT:
                        self._state = False

            self._clock.tick()
            pygame.display.update()
#            print(self._clock)
        pygame.quit()

game = Game()
game.game_loop()
