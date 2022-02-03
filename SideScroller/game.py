import player
import enemy
import pygame
import weapon


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1160, 610))
        self._clock = pygame.time.Clock()
        self._player1 = player.Player([500, 500])
        self._state = False
        self._weapon = pygame.sprite.Group()


    def game_loop(self):
        game_loop = True
        while game_loop:
            self.window.fill((100, 100, 100))

            self.window.blit(self._player1.image, self._player1.position)

            self._player1.move()
            self._player1.jump()

            self._player1._weapon.update()
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
                    if event.key == pygame.K_RIGHT:
                        self._state = True
                        self._player1._shot_direction = "R"
                    if event.key == pygame.K_LEFT:
                        self._state = True
                        self._player1._shot_direction = "L"
                    if event.key == pygame.K_UP:
                        self._state = True
                        self._player1._shot_direction = "U"

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self._player1._right = False
                    if event.key == pygame.K_a:
                        self._player1._left = False
                    if event.key == pygame.K_RIGHT:
                        self._state = False
                    if event.key == pygame.K_LEFT:
                        self._state = False
                    if event.key == pygame.K_UP:
                        self._state = False

            if self._state == True:
                self._player1.attack()

            self._clock.tick()
            pygame.display.update()
            #print(self._clock)

        pygame.quit()


game = Game()
game.game_loop()
