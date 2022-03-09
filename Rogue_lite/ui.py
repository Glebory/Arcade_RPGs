class Ui:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def render(self, screen):
        screen.blit(self._image, (self.x,self.y))
