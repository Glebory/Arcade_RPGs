import pygame
import pygame_gui
from character import *

import scene_one as s1
import scene_two as s2
import forest_scenes as fs

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Text Adventure")
ui_manager = pygame_gui.UIManager((640, 480))

output_text = ""
textbox = pygame_gui.elements.UITextBox("Enter your name to begin <br>", pygame.Rect((10, 10), (620, 400)), ui_manager)
text_entry = pygame_gui.elements.UITextEntryLine(pygame.Rect((10, 420), (620, 40)), ui_manager)
ui_manager.set_focus_set(text_entry)

clock = pygame.time.Clock()

# keywords for moving between scenes
movement = ("go", "move", "exit", "leave", "travel", "walk")
# keywords for interacting with scene objects
action = ("talk", "fight", "search", "take")

scenes = [s1.SceneOne(), s2.SceneTwo(), fs.SceneForestOne()]
current_scene = s1.SceneOne()
#if we add other classes easier to assign as player. this is for picling up items etc
player = knight1

def process_input(input_text):
    global current_scene
    global output_text
    input_words = input_text.split()
    command = input_words[0]
    # action within a scene
    if command in action:
        if command == "search":
            sceneObjects = current_scene.get_objects()
            if len(sceneObjects) == 0:
                output_text = "You look around but don't find anything interesting.<br>"
                return
            output_text = "You can see: <br>"
            for obj in sceneObjects:
                output_text += obj.get_name() + " - " + obj.get_description() + "<br>"

        if command == "talk":
            npcs = current_scene.get_npcs()
            if len(npcs) == 0:
                output_text = "There is nobody to talk to here. <br>"
                return
            if len(input_words) > 1:
                target = input_words[1]
                if target in npcs:
                    output_text = npcs[target]
        
        if command == "take":
                if len(input_words) > 1:
                    target_object = input_words[1].lower()
                    objects = current_scene.get_objects()
                    for item in objects:
                        if target_object == item.get_name().lower():
                            knight1.add_item(item)
                            output_text = "You got a " + target_object + "!<br>"
                            current_scene.remove_object(item)
                        else:
                            output_text = "That item isn't here! <br>"
                else:
                    output_text = command + " what? <br>"


    # Movement between scenes
    if command in movement:
        if len(input_words) > 1:
            direction = input_words[1]
            exits = current_scene.get_exits()
            locations = current_scene.get_locations()
            if direction in exits:
                exitName = exits.get(direction)
                if exitName is not None:
                    for scene in scenes:
                        if exitName == scene.get_name():
                            current_scene = scene
                            output_text = current_scene.get_description()
            elif direction in locations:
                output_text = locations[direction]
            else:
                output_text = "There is no exit there! <br>"
        else:
            output_text = command + " where? <br>"

def main():
    global output_text
    started = True
    running = True
    time_delta = clock.tick(60) / 1000.0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            ui_manager.process_events(event)
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                textbox.append_html_text("> " + event.text + "<br>")
                text_entry.set_text("")
                if started is True:
                    playername = event.text
                    started = False
                    textbox.append_html_text("Welcome, " + playername + "<br>")
                    textbox.append_html_text(current_scene.get_description())
                    continue

                process_input(event.text.lower())
                textbox.append_html_text(output_text)
                output_text = ""

        ui_manager.update(time_delta)
        ui_manager.draw_ui(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
    pygame.quit()
