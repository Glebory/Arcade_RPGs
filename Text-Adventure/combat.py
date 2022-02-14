from character import *
import item as i
from created_items import *
from enemies import *
import inventory as inv
import spells as s
import attacks as a
import random
import math

'''
stuff to do:
    enemy ai
'''

player_buffs = {}
enemy_buffs = {}


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
def playerInput(command_list):
    while True:
        player_command = (input(" > ")).upper()
        if player_command in command_list:
            return player_command
        print("Please select a valid action!")


# calculates overall damage when a character attacks its enemy
def attack(attacker, defender):
    # change when there is more classes
    if isinstance(attacker, Player_swordsman):
        base_damage = attacker.get_strength() + attacker.get_weapon().get_attack()
        damage_type = attacker.get_weapon().get_bonus()
    else:
        base_damage = attacker.get_strength() - defender.get_armour().get_defense()
        if base_damage < 1:
            base_damage = 1
        damage_type = None
    damage = damageChecker(base_damage, damage_type, defender)
    defender.take_damage(damage)
    print("%s attacks, %s takes %i damage" % (attacker, defender, damage))


# takes input from the player
def playerAction(player, enemy):
    action = playerInput(["ATTACK", "SPELL", "ITEM", "FLEE"])
    if action == "ATTACK":
        attack(player, enemy)

    elif action == "SPELL":
        print("Choose a spell from:")
        choices = []
        spell_reference = []
        # sets list of spells up for use in playerInput(), with names in upper case
        for spell in player.get_spells():
            name = spell.get_name().upper()
            choices.append(name)
            spell_reference.append([name, spell])
        print(choices)
        chosen_spell_str = playerInput(choices)
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
                print("%s %s, dealing %i damage to %s" % (player, chosen_spell.get_flavour_text(), damage, enemy))
            elif isinstance(chosen_spell, s.TimedSpell):
                spell_turns = chosen_spell.cast(player)
                player_buffs[chosen_spell] = spell_turns
                print("%s %s" % (player, chosen_spell.get_flavour_text()))
            else:
                chosen_spell.cast(player)
                print("%s %s" % (player, chosen_spell.get_flavour_text()))
            player.use_mana(chosen_spell.get_mana_cost())
        # not enough mana -> spell fails
        else:
            print("%s doesn't have enough mana to cast %s" % (player, chosen_spell.get_name()))

    elif action == "ITEM":
        print("Choose an item from:")
        throwables = player.get_inventory().get_throwables()
        consumables = player.get_inventory().get_consumables()
        choices = []
        # player chooses item from consumables and throwables
        for item in throwables:
            choices.append(item.upper())
        for item in consumables:
            choices.append(item.upper())
        print(choices)
        chosen_item_str = playerInput(choices)
        # checks from which inventory the chosen item is from
        if inv.get_item_object(throwables, chosen_item_str):
            chosen_item = inv.get_item_object(throwables, chosen_item_str)
        else:
            chosen_item = inv.get_item_object(consumables, chosen_item_str)

        # different for each type of item
        if isinstance(chosen_item, i.Throwable):
            damage = damageChecker(chosen_item.get_damage(), chosen_item.get_damage_type(), enemy)
            enemy.take_damage(damage)
            print("%s throws their %s, dealing %i damage to %s" % (player, chosen_item.get_name(), damage, enemy))

        if isinstance(chosen_item, i.HealthGiver):
            chosen_item.consume(player)
            print("%s drinks their %s, healing %i HP" % (player, chosen_item.get_name(), chosen_item.get_points()))

        if isinstance(chosen_item, i.ResistanceGiver):
            item_turns = chosen_item.consume(player)
            player_buffs[chosen_item] = item_turns
            print("%s drinks their %s, gaining %s resistance for %i turns" % (player,
                                                                              chosen_item.get_name(),
                                                                              chosen_item.get_resistance(),
                                                                              chosen_item.get_turns()))
        if isinstance(chosen_item, i.StrengthGiver):
            item_turns = chosen_item.consume(player)
            player_buffs[chosen_item] = item_turns
            print("%s drinks their %s, gaining %i strength for %i turns" % (player,
                                                                              chosen_item.get_name(),
                                                                              chosen_item.get_points(),
                                                                              chosen_item.get_turns()))
        player.get_inventory().remove(chosen_item)

    else:
        print("You attempt to flee...")
        return True


def enemyAction(player, enemy):
    # wip, there should be a list of actions the enemy can do and there's a percent chance for each
    # just doing attack for now until we sort out spell lists and inventories
    attack(enemy, player)


# overall combat function. makes use of lots of functions
def combat(player, enemy):
    turn_count = 0
    # checks if player wants to flee
    fleeCheck = False
    # combat will keep going until this is false, theres a few ways to do this
    continue_combat = True
    while continue_combat:
        # both alive
        if player.get_current_health() > 0 and enemy.get_current_health() > 0:
            turn_count += 1
            # info, will probably be changed for pygame version rather than just printing
            print("%s HP: %i / %i" % (player, player.get_current_health(), player.get_total_health()))
            print("%s Mana: %i / %i" % (player, player.get_current_mana(), player.get_total_mana()))
            print("%s HP: %i / %i" % (enemy, enemy.get_current_health(), enemy.get_total_health()))
            print("Player turn...")
            fleeCheck = playerAction(player, enemy)
            if enemy.get_current_health() > 0:
                enemyAction(player, enemy)
                # buffs are checked to see if theyre still active
                buffChecker(player, player_buffs)
                buffChecker(enemy, enemy_buffs)
                if fleeCheck:
                    continue_combat = False
            else:
                continue_combat = False
        else:
            continue_combat = False

    # battle over and player alive = win
    if player.get_current_health() > 0:
        clearBuffs(player, enemy)
        print("Player wins!")
        # win/lose/flee for use outside of combat to determine outcome
        return "WIN"
    elif fleeCheck:
        clearBuffs(player, enemy)
        print("Player flees...")
        return "FLEE"
    # battle over and player not alive = lose
    else:
        clearBuffs(player, enemy)
        print("Enemy wins, Game Over!")
        return "LOSE"


"""
slime = Slime(1, 8)
zombie = Zombie(1, 20)
mimic = Mimic(1, 20)
minorheal = s.Heal("Minor Healing", 10, 5)
fireball = a.Fire("Fireball", "casts a fireball", 10, 5)
fireres = s.ResistanceBuff("Flame Body", None, 5, 3, "Fire")
strup = s.StrengthBuff("Bulk", 3, 5, 3)
strdown = s.StrengthDeBuff("Weaken", 3, 5, 3)
knight1.add_spell(minorheal)
knight1.add_spell(fireball)
knight1.add_spell(fireres)
knight1.add_spell(strup)
knight1.add_spell(strdown)
combat(knight1, mimic)
"""