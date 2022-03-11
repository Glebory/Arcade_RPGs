import pygame


class Menu:
    def __init__(self, handler, topleft,color="white", buffer=6, border=0):
        self.buttons = []
        self.handler = handler
        self._size = [20, 10]
        self.buffer = buffer
        self._rect = pygame.Rect(topleft, self._size)
        self.border = border
        self.color = color
        self.selected_button = None
        self.sound = pygame.mixer.Sound("sounds/select.wav")

    def add_button(self, button):
        self.buttons.append(button)
        if button._rect.width + (self.buffer*2) > self._size[0]:
            self._size[0] = button._rect.width + (self.buffer*2)
        self._size[1] += button._rect.height + (self.buffer*2)
        self._rect.size = self._size
        if len(self.buttons) == 1:
            self.selected_button = button
        print(len(self.buttons))

    def select_button_below(self):
        if self.buttons.index(self.selected_button) == len(self.buttons)-1:
            self.selected_button.selected = False
            self.selected_button = self.buttons[0]
        else:
            self.selected_button.selected = False
            self.selected_button = self.buttons[self.buttons.index(self.selected_button)+1]
        self.sound.play()

    def select_button_above(self):
        if self.buttons.index(self.selected_button) == 0:
            self.selected_button.selected = False
            self.selected_button = self.buttons[len(self.buttons) - 1]
        else:
            self.selected_button.selected = False
            self.selected_button = self.buttons[self.buttons.index(self.selected_button) - 1]

        self.sound.play()

    def press(self):
        self.selected_button.press()
        self.sound.play()

    def render(self, screen):
        if self.border == 0:
            pygame.draw.rect(screen, self.color, self._rect, self.border)
        else:
            pygame.draw.rect(screen, self.color, self._rect)
            pygame.draw.rect(screen, "blue", self._rect, self.border)
        
        for button in self.buttons:
            button.render(screen)
        if self.selected_button is not None:
            self.selected_button.select()
