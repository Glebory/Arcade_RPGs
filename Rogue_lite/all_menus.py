from Menu import *
from button import *


def main_menu(handler):
    menu = Menu(handler, (handler._size[0] / 2, handler._size[1] / 2),"white", 8)
    play_button = Button("Begin", handler.pause, (menu._rect.left + menu.buffer, menu._rect.top + menu.buffer), 24, "yellow")
    quit_button = Button("Quit", handler.quit, (menu._rect.left + menu.buffer, play_button._rect.bottom + menu.buffer), 24, "yellow")
    menu.add_button(play_button)
    menu.add_button(quit_button)
    return menu
