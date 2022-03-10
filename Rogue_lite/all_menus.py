from Menu import *
from button import *

def main_menu(handler, topleft):
    menu = Menu(handler, (handler._size[0]/2, handler._size[1]/2), 8, 1)
    play_button = Button("Begin",handler.pause(),(menu.buffer,menu.buffer),11,)
