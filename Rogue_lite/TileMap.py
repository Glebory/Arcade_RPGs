from all_tiles import *


class TileMap():
    def __init__(self,size,screen):
        self.size = size
        #self.random_map()
        self.screen = screen



    def random_map(self):
        i = 32
        while i < (self.size[0]-64):
            j = 32
            while j < (self.size[1]-64):
                tile = create_random_tile(i,j)
                tile.render(self.screen)

    def border_tile(self):
        i = 0
        while i < self.size[0]-32:
            tile = beach_tile(i, self.size[1])
            tile.render(self.screen)
            i += 32
            print("success?")

    #def render(self, screen):

