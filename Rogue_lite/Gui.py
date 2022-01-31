class Gui:
    def __init__(self,screen, objects, h, w ):
        self._screen = screen
        self._objects = objects
        self._h = h
        self._w = w

    def render(self):
        self._screen.fill((255,255,255))
        for object in self._objects:
            object.tick(self._h, self._w)
            object.render(self._screen)

