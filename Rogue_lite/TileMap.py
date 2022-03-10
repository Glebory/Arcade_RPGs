from all_tiles import *
import random

def set_up_room(room_imgs, matrix, handler):
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j] != 0:
                tile = Tile(j*32,i*32, room_imgs[matrix[i][j]])
                handler.unmovable_group.add(tile)
                handler._objects.add(tile)
            j+=1
        i+=1

