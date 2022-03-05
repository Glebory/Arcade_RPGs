import pygame
import pygame_gui
from character import *
from inventory import *
import npc
import combat as c
import enemies as e
import item as i

import character_scene as cs
import scene_one as s1
import scene_two as s2
import forest_scenes as fs
import dungeon_scenes as ds

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Text Adventure")
ui_manager = pygame_gui.UIManager((640, 480))

output_text = ""
textbox = pygame_gui.elements.UITextBox("Enter your name to begin <br>", pygame.Rect((10, 10), (620, 400)), ui_manager)
text_entry = pygame_gui.elements.UITextEntryLine(pygame.Rect((10, 420), (620, 40)), ui_manager)
ui_manager.set_focus_set(text_entry)

clock = pygame.time.Clock()
running = True

# keywords for moving between scenes
movement = ("go", "move", "exit", "leave", "travel", "walk")
# keywords for interacting with scene objects
action = ("talk", "fight", "search", "take", "inventory", "items", "equip")
trading = ("buy", "sell", "browse")
inventory_keywords = ("equipped", "weapons", "armour", "throwables", "consumables", "misc")

scenes = [cs.CharSel(), s1.SceneOne(), s2.SceneTwo(), s2.SceneTwoPartTwo(), fs.SceneForestOne(),
          fs.SceneForestTwo(), fs.SceneForestThree(), fs.SceneForestFour(),
          fs.SceneForestFive(), fs.SceneForestSix(), fs.SceneForestSeven(), 
          fs.SceneForestEight(), fs.SceneForestNine(), fs.SceneForestTen(), ds.SceneDungeonOne(),
          ds.SceneDungeonTwo(), ds.SceneDungeonThree(), ds.SceneDungeonFour(),
          ds.SceneDungeonFive(), ds.SceneDungeonSix(), ds.SceneDungeonSeven()]

current_scene = cs.CharSel()
# if we add other classes easier to assign as player. this is for picking up items etc
player = knight1


def process_input(input_text):
    global current_scene
    global output_text
    global running
    global player
    input_words = input_text.split()
    if not input_words:
        return
    command = input_words[0]
    if current_scene.get_name() == "char_select":
        if command == "knight":
            player = knight1
        elif command == "wizard":
            player = wizard1
        elif command == "archer":
            player = archer1
        output_text =  "You chose " + player.get_name() + ".<br>Type 'go north' to walk into the mist"\
                        " and begin your adventure<br>"
        player.set_name(playername) #sets the playername a second time after class is assigned 
        
    if command == "help":
        output_text = "Available commands:<br>" \
                      "go/move/exit/leave/travel/walk (direction)- movement<br>" \
                      "talk (character)- to characters<br>" \
                      "search - the surroundings<br>" \
                      "search (point of interest) - searches a specific place e.g. a box<br>" \
                      "take (item name)- an item<br>" \
                      "inventory/items - items you have<br>"\
                      "equip (item name) - equip an item to yourself<br>"\
                      "browse - trader's items<br>" \
                      "buy/sell (item name) - trade with a trader<br>"
    # action within a scene
    if command in action:
        if command == "search":
            if len(input_words) == 2:
                target_location = input_words[1]
                locations = current_scene.get_locations()
                if target_location == "ground" or target_location == "floor":
                    sceneObjects = current_scene.get_objects()
                    if len(sceneObjects) == 0:
                        output_text = "You look around but don't find anything interesting.<br>"
                        return
                    output_text = "You can see: <br>"
                    for obj in sceneObjects:
                        output_text += obj.get_name() + " - " + obj.get_description() + "<br>"
                    return

                if target_location not in locations:
                    output_text = "You don't find that here.<br>"
                    return
                output_text = "%s<br>" % locations[target_location]
                if target_location in current_scene.get_loot().keys():
                    # can be either an item or an enemy in hiding
                    found_object = current_scene.get_loot()[target_location]
                    if isinstance(found_object, i.Item):
                        output_text += "You found a: <br>"
                        output_text += "%s<br>" % found_object
                        current_scene.add_object(found_object)
                        current_scene.remove_loot(target_location)
                        return
                    # else it's an enemy
                    else:
                        outcome = c.combat(player, found_object, ui_manager, screen)
                        ui_manager.set_focus_set(text_entry)
                        if outcome == "FLEE":
                            current_scene = s1.SceneOne()
                            output_text = "You escape the area...<br>"
                            return
                        elif outcome == "LOSE":
                            output_text = "Game Over<br>"
                            # game over stuff (client closes?)
                            running = False
                            return
                        else:
                            output_text = ("You defeated the %s!<br>" % found_object) \
                                          + output_text
                            current_scene.remove_loot(target_location)
                            return

            if output_text:
                return
            sceneObjects = current_scene.get_objects()
            if len(sceneObjects) == 0:
                output_text += "You look around but don't find anything interesting.<br>"
                return
            output_text += "You can see: <br>"
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
                    output_text = npcs[target].get_speech()
        
        if command == "take":
            target_object = ""
            if len(input_words) == 2:
                target_object = input_words[1]
            if len(input_words) > 2:
                for word in input_words:
                    if word == input_words[0]:
                        continue
                    target_object += word + " "
                target_object = target_object.rstrip()
            objects = current_scene.get_objects()
            for item in objects:
                if target_object == item.get_name().lower():
                    player.add_item(item)
                    output_text = "You got a " + target_object + "!<br>"
                    current_scene.remove_object(item)
                else:
                    output_text = "That item isn't here! <br>"

        if command == "items" or command == "inventory":
            output_text = "What would you like to see? <br>  Equipped, Weapons, " \
                          "Armour, Throwables, Consumables, Misc<br>"

        if command == "equip":
            item = ""
            if len(input_words) == 1:
                output_text = "Equip what item?<br>"
                return
            if len(input_words) == 2:
                item = input_words[1]
            if len(input_words) > 2:
                for word in input_words:
                    if word == input_words[0]:
                        continue
                    item += word + " "
                item = item.rstrip()
            player_inv = player.get_inventory()
            if get_item_object(player_inv.get_weapons(), item.upper()):
                weapon = get_item_object(player_inv.get_weapons(), item.upper())
                old_weapon = player.get_weapon()
                player.set_weapon(weapon)
                player.add_item(old_weapon)
                player.remove_item(weapon)
                output_text = "You have equipped " + weapon.get_name() + ".<br>" + old_weapon.get_name() + " has been" \
                              " moved to your inventory.<br>"
            if get_item_object(player_inv.get_armour(), item.upper()):
                armour = get_item_object(player_inv.get_armour(), item.upper())
                old_armour = player.get_armour()
                player.set_armour(armour)
                player.add_item(old_armour)
                player.remove_item(armour)
                output_text = "You have equipped " + armour.get_name() + ".<br>" + old_armour.get_name() + " has been" \
                              " moved to your inventory.<br>"
            else:
                output_text = "You cannot equip that!<br>"

    if command in inventory_keywords:
        inv = player.get_inventory()
        if command == "equipped":
            output_text = "You are wearing: <br>"
            output_text += str(player.get_weapon()) + "<br>"
            output_text += str(player.get_armour()) + "<br>"
        if command == "weapons":
            output_text = "Weapons you have: <br>"
            for weapon in inv.get_weapons().values():
                output_text += str(weapon[0]) + ". Amount: " + str(weapon[1]) + "<br>"
        if command == "armour":
            output_text = "Armour you have: <br>"
            for armour in inv.get_armour().values():
                output_text += str(armour[0]) + ". Amount: " + str(armour[1]) + "<br>"
        if command == "throwables":
            output_text = "Throwing items you have: <br>"
            for throwable in inv.get_throwables().values():
                output_text += str(throwable[0]) + ". Amount: " + str(throwable[1]) + "<br>"
        if command == "consumables":
            output_text = "Consumable items you have: <br>"
            for consumable in inv.get_consumables().values():
                output_text += str(consumable[0]) + ". Amount: " + str(consumable[1]) + "<br>"
        if command == "misc":
            output_text = "Other items you have: <br>"
            for other in inv.get_other().values():
                output_text += str(other[0]) + ". Amount: " + str(other[1]) + "<br>"

    if command in trading:
        if "merchant" not in current_scene.get_npcs().keys():
            output_text = "There is nobody around to trade with. <br>"
            return
        trader = current_scene.get_npcs()["merchant"]
        if command == "browse":
            output_text += trader.merchant_browse()
        if command == "buy":
            item = ""
            if len(input_words) == 1:
                output_text = "Buy what item?<br>"
                return
            if len(input_words) == 2:
                item = input_words[1]
            if len(input_words) > 2:
                for word in input_words:
                    if word == input_words[0]:
                        continue
                    item += word + " "
                item = item.rstrip()
            output_text = trader.buy_from_merchant(item, player)
        if command == "sell":
            item = ""
            if len(input_words) == 1:
                output_text = "Sell what item?<br>"
                return
            if len(input_words) == 2:
                item = input_words[1]
            if len(input_words) > 2:
                for word in input_words:
                    if word == input_words[0]:
                        continue
                    item += word + " "
                item = item.rstrip()
            output_text = trader.sell_to_merchant(item, player)

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
                            if scene.get_requirements() is not None:
                                if player.get_inventory().find_item(scene.get_requirements().get_name()) is None:
                                    output_text = "It's locked!<br>"
                                    return
                            current_scene = scene
                            output_text = current_scene.get_description()
                            if current_scene.get_enemy():
                                outcome = c.combat(player, current_scene.get_enemy(), ui_manager, screen)
                                ui_manager.set_focus_set(text_entry)
                                if outcome == "FLEE":
                                    current_scene = s1.SceneOne()
                                    output_text = "You escape the area...<br>"
                                elif outcome == "LOSE":
                                    output_text = "Game Over<br>"
                                    # game over stuff (client closes?)
                                    running = True
                                else:
                                    output_text = ("You defeated the %s!<br>" % current_scene.get_enemy()) \
                                                  + output_text
                                    current_scene.remove_enemy()
            elif direction in locations:
                output_text = "%s<br>" % locations[direction]
            else:
                output_text = "There is no exit there! <br>"
        else:
            output_text = command + " where? <br>"


def process_clicks(target):
    global current_scene
    global output_text
    global running
    global player

    if target in ("north", "south", "east", "west"):
        exits = current_scene.get_exits()
        exitName = exits.get(target)
        if exitName is not None:
            for scene in scenes:
                if exitName == scene.get_name():
                    if scene.get_requirements() is not None:
                        if player.get_inventory().find_item(scene.get_requirements().get_name()) is None:
                            output_text = "It's locked!<br>"
                            return
                    current_scene = scene
                    output_text = current_scene.get_description()
                    if current_scene.get_enemy():
                        outcome = c.combat(player, current_scene.get_enemy(), ui_manager, screen)
                        ui_manager.set_focus_set(text_entry)
                        if outcome == "FLEE":
                            current_scene = s1.SceneOne()
                            output_text = "You escape the area...<br>"
                        elif outcome == "LOSE":
                            output_text = "Game Over<br>"
                            running = False
                            # game over stuff (client closes?)
                        else:
                            output_text = ("You defeated the %s!<br>" % current_scene.get_enemy()) \
                                          + output_text
                            current_scene.remove_enemy()
    if target in current_scene.get_locations().keys():
        output_text = current_scene.get_locations().get(target)

    if target in current_scene.get_npcs().keys():
        output_text = current_scene.get_npcs().get(target).get_speech()
    if target in trading:
        if target == "browse":
            trader = current_scene.get_npcs()["merchant"]
            output_text = trader.merchant_browse()
        if target == "buy" or target == "sell":
            output_text = "use: '" + str(target) + " item name'<br>"


def main():
    global current_scene
    global output_text
    global running
    global playername
    global player

    started = True
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
                    player.set_name(playername)
                    textbox.append_html_text(current_scene.get_description())
                    textbox.rebuild()
                    continue

                process_input(event.text.lower())
                textbox.append_html_text(output_text)
                output_text = ""

            if textbox.process_event(event):
                pass
            if event.type == pygame_gui.UI_TEXT_BOX_LINK_CLICKED:
                textbox.append_html_text("> " + event.link_target + "<br>")
                process_clicks(event.link_target)

                textbox.append_html_text(output_text)
                output_text = ""
                textbox.rebuild()

        ui_manager.update(time_delta)
        ui_manager.draw_ui(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
    pygame.quit()
