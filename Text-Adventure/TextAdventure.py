import pygame
import pygame_gui

import scene_one as s1
import scene_two as s2

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Text Adventure")
ui_manager = pygame_gui.UIManager((640, 480))

output_text = ""
textbox = pygame_gui.elements.UITextBox("Enter your name to begin <br>", pygame.Rect((10, 10), (620, 400)), ui_manager)
text_entry = pygame_gui.elements.UITextEntryLine(pygame.Rect((10, 420), (620, 40)), ui_manager)
ui_manager.set_focus_set(text_entry)

clock = pygame.time.Clock()

movement = ["go", "move", "exit", "leave", "travel", "walk"]

scenes = [s1.SceneOne(), s2.SceneTwo()]
current_scene = s1.SceneOne()

def process_input(input_text):
    global current_scene
    global output_text
    input_words = input_text.split()
    command = input_words[0]

    if len(input_words) > 1:
        # Movement between scenes
        direction = input_words[1]
        exits = current_scene.get_exits()
        if (command in movement) and (direction in exits):
            exitName = exits.get(direction)
            if exitName is not None:
                for scene in scenes:
                    if exitName == scene.get_name():
                        current_scene = scene
                        output_text = current_scene.get_description()
        else:
            output_text = "There is no exit there! <br>"

def main():
    running = True
    time_delta = clock.tick(60) / 1000.0
    started = True

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
        ui_manager.update(time_delta)
        ui_manager.draw_ui(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()
    pygame.quit()
