import player
import enemy
import pygame
import weapon

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((1160, 610))
        self._clock = pygame.time.Clock()
        self._player1 = player.Player([500, 500], 100)
        self._enemy1 = enemy.Enemy([750, 475], 100)
        self._state = False
        self._enemies = pygame.sprite.Group()


    def game_loop(self):
        game_loop = True
        while game_loop:
            if self._player1._counter > 0:
                self._player1._counter -= 1
            self.window.fill((100, 100, 100))

            if self._enemy1._health > 0 and self._player1._health > 0:
                self.window.blit(self._player1.image, self._player1.rect)
                self._player1.move()
                self._player1.jump()
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

            self._clock.tick(60)
            pygame.display.update()
        #    print(self._clock)

        pygame.quit()


game = Game()
game.game_loop()
