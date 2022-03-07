from character import *
import item as i
from created_items import *
from enemies import *
import inventory as inv
import spells as s
import attacks as a
import random
import math
import pygame
import pygame_gui

player_buffs = {}
enemy_buffs = {}
clock = pygame.time.Clock()
time_delta = clock.tick(60) / 1000.0


# checks if a buff's time has ran out
def buffChecker(character, buff_dict):
    timed_out_buffs = []
    for buff in buff_dict:
        timer = buff_dict[buff] - 1
        # timed out
        if timer < 0:
            timed_out_buffs.append(buff)
        buff_dict[buff] = timer
    for buff in timed_out_buffs:
        buff.timeout(character)
        buff_dict.pop(buff)


# remove all buffs from the player and enemy
def clearBuffs(player, enemy):
    for buff in player_buffs:
        buff.timeout(player)
    for buff in enemy_buffs:
        buff.timeout(enemy)
    player_buffs.clear()
    enemy_buffs.clear()


# returns true if the character has the given weakness
def weaknessChecker(damage_type, character):
    if damage_type in character.get_weaknesses():
        return True
    return False


# returns true if the character has the given resistance
def resistanceChecker(damage_type, character):
    if damage_type in character.get_resistances():
        return True
    return False


# calculates the damage based on if its very/not very effective
def damageChecker(damage, damage_type, character):
    if damage_type:
        if resistanceChecker(damage_type, character):
            # half damage (rounded up)
            damage = math.ceil(damage / 2)
        elif weaknessChecker(damage_type, character):
            # double damage
            damage = damage * 2
    return damage


# takes input and checks if its part of the given command list
def playerInput(command_list, ui_manager, screen, textbox, text_entry):
    while True:
        for event in pygame.event.get():
            ui_manager.process_events(event)
            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                textbox.append_html_text("> " + event.text + "<br>")
                text_entry.set_text("")
                if event.text.upper() in command_list:
                    return event.text.upper()
                else:
                    textbox.append_html_text("Please select a valid action!<br>")
        ui_manager.update(time_delta)
        ui_manager.draw_ui(screen)
        pygame.display.flip()
        if text_entry not in ui_manager.get_focus_set():
            text_entry.set_text("")
            ui_manager.set_focus_set(text_entry)


# calculates overall damage when a character attacks its enemy
def attack(attacker, defender, textbox):
    # change when there is more classes
    if isinstance(attacker, Player_swordsman) or isinstance(attacker, Player_wizard) or isinstance(attacker, Player_archer):
        base_damage = attacker.get_strength() + attacker.get_weapon().get_attack()
        damage_type = attacker.get_weapon().get_bonus()
    else:
        base_damage = attacker.get_strength() - defender.get_armour().get_defense()
        damage_type = "Melee"
    damage = damageChecker(base_damage, damage_type, defender)
    if damage < 1:
        damage = 1
    defender.take_damage(damage)
    textbox.append_html_text("%s attacks, %s takes %i %s damage<br>" % (attacker, defender, damage, damage_type))


# takes input from the player
def playerAction(player, enemy, ui_manager, screen, textbox, text_entry):
    action = playerInput(["ATTACK", "SPELL", "ITEM", "FLEE"], ui_manager, screen, textbox, text_entry)
    if action == "ATTACK":
        attack(player, enemy, textbox)

    elif action == "SPELL":
        textbox.append_html_text("Choose a spell from:<br>")
        choices = []
        spell_reference = []
        choices_str = ""
        # sets list of spells up for use in playerInput(), with names in upper case
        for spell in player.get_spells():
            name = spell.get_name().upper()
            choices.append(name)
            spell_reference.append([name, spell])
        for spell in choices:
            choices_str += "%s, " % spell
        textbox.append_html_text("%s<br><br>" % choices_str[:-2])
        chosen_spell_str = playerInput(choices, ui_manager, screen, textbox, text_entry)
        chosen_spell = ""

        # finds chosen spell
        for reference in spell_reference:
            if reference[0] == chosen_spell_str:
                chosen_spell = reference[1]

        # if player has enough mana
        if chosen_spell.get_mana_cost() <= player.get_current_mana():
            # different for each type of spell
            if isinstance(chosen_spell, a.Attacks):
                damage = damageChecker(chosen_spell.get_damage(), chosen_spell.get_damage_type(), enemy)
                enemy.take_damage(damage)
                textbox.append_html_text(
                    "%s %s, dealing %i %s damage to %s<br>" % (player, chosen_spell.get_flavour_text(),
                                                               damage, chosen_spell.get_damage_type(), enemy))
            elif isinstance(chosen_spell, s.StrengthDeBuff):
                if chosen_spell not in enemy_buffs:
                    chosen_spell.cast(enemy)
                enemy_buffs[chosen_spell] = chosen_spell.get_turns()
                textbox.append_html_text("%s %s<br>" % (player, chosen_spell.get_flavour_text()))
            elif isinstance(chosen_spell, s.TimedSpell):
                if chosen_spell not in player_buffs:
                    chosen_spell.cast(player)
                player_buffs[chosen_spell] = chosen_spell.get_turns()
                textbox.append_html_text("%s %s<br>" % (player, chosen_spell.get_flavour_text()))
            else:
                chosen_spell.cast(player)
                textbox.append_html_text("%s %s<br>" % (player, chosen_spell.get_flavour_text()))
            player.use_mana(chosen_spell.get_mana_cost())
        # not enough mana -> spell fails
        else:
            textbox.append_html_text("%s doesn't have enough mana to cast %s<br>" % (player, chosen_spell.get_name()))

    elif action == "ITEM":
        textbox.append_html_text("Choose an item from:<br>")
        throwables = player.get_inventory().get_throwables()
        consumables = player.get_inventory().get_consumables()
        choices = []
        choices_str = ""
        # player chooses item from consumables and throwables
        for item in throwables:
            choices.append(item.upper())
        for item in consumables:
            choices.append(item.upper())
        for item in choices:
            choices_str += "%s, " % item
        textbox.append_html_text("%s<br><br>" % choices_str[:-2])
        chosen_item_str = playerInput(choices, ui_manager, screen, textbox, text_entry)
        # checks from which inventory the chosen item is from
        if inv.get_item_object(throwables, chosen_item_str):
            chosen_item = inv.get_item_object(throwables, chosen_item_str)
        else:
            chosen_item = inv.get_item_object(consumables, chosen_item_str)

        # different for each type of item
        if isinstance(chosen_item, i.Throwable):
            damage = damageChecker(chosen_item.get_damage(), chosen_item.get_damage_type(), enemy)
            enemy.take_damage(damage)
            textbox.append_html_text(
                "%s throws their %s, dealing %i %s damage to %s<br>" % (player, chosen_item.get_name(),
                                                                        damage, chosen_item.get_damage_type(), enemy))

        if isinstance(chosen_item, i.HealthGiver):
            chosen_item.consume(player)
            textbox.append_html_text(
                "%s drinks their %s, healing %i HP<br>" % (player, chosen_item.get_name(), chosen_item.get_points()))

        if isinstance(chosen_item, i.ManaGiver):
            chosen_item.consume(player)
            textbox.append_html_text(
                "%s drinks their %s, restoring %i Mana<br>" % (player, chosen_item.get_name(), chosen_item.get_points()))

        if isinstance(chosen_item, i.ResistanceGiver):
            item_turns = chosen_item.consume(player)
            player_buffs[chosen_item] = item_turns
            textbox.append_html_text("%s drinks their %s, gaining %s "
                                     "resistance for %i turns<br>" % (player,
                                                                      chosen_item.get_name(),
                                                                      chosen_item.get_resistance(),
                                                                      chosen_item.get_turns()))
        if isinstance(chosen_item, i.StrengthGiver):
            item_turns = chosen_item.consume(player)
            player_buffs[chosen_item] = item_turns
            textbox.append_html_text("%s drinks their %s, gaining %i "
                                     "strength for %i turns<br>" % (player,
                                                                    chosen_item.get_name(),
                                                                    chosen_item.get_points(),
                                                                    chosen_item.get_turns()))
        player.get_inventory().remove(chosen_item)

    else:
        textbox.append_html_text("You attempt to flee...<br>")
        return True


def enemyAction(player, enemy, textbox):
    # 50/50 chance to attack or use a spell
    choice = random.randint(0, 1)
    if choice == 0:
        attack(enemy, player, textbox)
    else:
        # equal chance for each spell
        spell_list = enemy.get_spell_list()
        spell_choice = random.randint(0, len(spell_list) - 1)
        # picks spell at random from its own list
        chosen_spell = spell_list[spell_choice]
        if isinstance(chosen_spell, a.Attacks):
            damage = damageChecker(chosen_spell.get_damage(), chosen_spell.get_damage_type(), player)
            player.take_damage(damage)
            textbox.append_html_text(
                "%s %s, dealing %i %s damage to %s<br>" % (enemy, chosen_spell.get_flavour_text(),
                                                           damage, chosen_spell.get_damage_type(), player))
        elif isinstance(chosen_spell, s.StrengthDeBuff):
            # only casts if not already buffed or debuffed, as otherwise
            # it would cause strength to not be put back to normal
            if chosen_spell not in player_buffs:
                chosen_spell.cast(player)
            player_buffs[chosen_spell] = chosen_spell.get_turns()
            textbox.append_html_text("%s %s<br>" % (enemy, chosen_spell.get_flavour_text()))
        elif isinstance(chosen_spell, s.TimedSpell):
            if chosen_spell not in enemy_buffs:
                chosen_spell.cast(enemy)
            enemy_buffs[chosen_spell] = chosen_spell.get_turns()
            textbox.append_html_text("%s %s<br>" % (enemy, chosen_spell.get_flavour_text()))
        else:
            chosen_spell.cast(enemy)
            textbox.append_html_text("%s %s<br>" % (enemy, chosen_spell.get_flavour_text()))


# overall combat function. makes use of lots of above functions
def combat(player, enemy, ui_manager, screen):
    # creates new ui elements only for combat use
    textbox = pygame_gui.elements.UITextBox("A %s approaches! <br>" % enemy, pygame.Rect((10, 10), (620, 400)),
                                            ui_manager)
    text_entry = pygame_gui.elements.UITextEntryLine(pygame.Rect((10, 420), (620, 40)), ui_manager)
    image = pygame.image.load(enemy.get_image())
    imagebox = pygame_gui.elements.UIImage(pygame.Rect((492, 10), (128, 128)), image, ui_manager)
    ui_manager.set_focus_set(text_entry)

    turn_count = 0
    # checks if player wants to flee
    fleeCheck = False
    # combat will keep going until this is false, theres a few ways to do this
    continue_combat = True
    while continue_combat:
        # both alive
        if player.get_current_health() > 0 and enemy.get_current_health() > 0:
            turn_count += 1
            # info about players stats
            textbox.append_html_text(
                "%s HP: %i / %i" % (player, player.get_current_health(), player.get_total_health()))
            textbox.append_html_text(", Mana: %i / %i<br>" % (player.get_current_mana(), player.get_total_mana()))
            textbox.append_html_text(
                "%s HP: %i / %i<br>" % (enemy, enemy.get_current_health(), enemy.get_total_health()))
            textbox.append_html_text("Player turn... Attack, Spell, Item or Flee?<br><br>")
            ui_manager.update(time_delta)
            ui_manager.draw_ui(screen)
            pygame.display.flip()
            fleeCheck = playerAction(player, enemy, ui_manager, screen, textbox, text_entry)
            if enemy.get_current_health() > 0:
                enemyAction(player, enemy, textbox)
                # buffs are checked to see if theyre still active
                buffChecker(player, player_buffs)
                buffChecker(enemy, enemy_buffs)
                if fleeCheck:
                    continue_combat = False
            else:
                continue_combat = False
        else:
            continue_combat = False

    if fleeCheck and player.get_current_health() > 0:
        clearBuffs(player, enemy)
        textbox.append_html_text("Player flees...<br>")
        outcome = "FLEE"

    # battle over and player alive = win
    elif player.get_current_health() > 0:
        clearBuffs(player, enemy)
        textbox.append_html_text("Player wins!<br>")
        # win/lose/flee for use outside of combat to determine outcome
        outcome = "WIN"

    # battle over and player not alive = lose
    else:
        clearBuffs(player, enemy)
        textbox.append_html_text("Enemy wins, Game Over!<br>")
        outcome = "LOSE"
    ui_manager.update(time_delta)
    ui_manager.draw_ui(screen)
    pygame.display.flip()

    pygame.time.wait(2000)
    textbox.kill()
    text_entry.kill()
    imagebox.kill()
    return outcome
