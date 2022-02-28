from character import *
import attacks as a
import spells as s


class Enemy(Character):
    def __init__(self, name, level, health, spell_list, image):
        super().__init__(name, level, health)
        self._spell_list = spell_list
        self._image = image

    def get_spell_list(self):
        return self._spell_list

    def get_image(self):
        return self._image


class Slime(Enemy):
    # basic slime, no resistances or weaknesses
    def __init__(self, level, health, spell_list):
        super().__init__("Slime", level, health, spell_list, "images/slime.png")


class Zombie(Enemy):
    # basic zombie, weak to fire
    def __init__(self, level, health, spell_list):
        super().__init__("Zombie", level, health, spell_list, "images/zombie.png")
        self._weaknesses = ["Fire"]


class Mimic(Enemy):
    # chest brought to life, resists melee but weak to fire
    def __init__(self, level, health, spell_list):
        super().__init__("Mimic", level, health, spell_list, "images/mimic.png")
        self._resistances = ["Melee"]
        self._weaknesses = ["Fire"]


class Goblin(Enemy):
    # basic goblin, weak to water
    def __init__(self, level, health, spell_list):
        super().__init__("Goblin", level, health, spell_list, "images/goblin.png")
        self._weaknesses = ["Water"]


class GoblinBrute(Enemy):
    # larger goblin in armour, resists melee
    def __init__(self, level, health, spell_list):
        super().__init__("Goblin Brute", level, health, spell_list, "images/goblinbrute.png")
        self._resistances = ["Melee"]
        self._weaknesses = ["Water"]


zombie = Zombie(1, 12, [a.bite])
slime = Slime(2, 10, [a.spit])
mimic = Mimic(2, 20, [a.bite, a.spit])
goblin = Goblin(2, 13, [a.stab, a.shoot])
goblin_brute = GoblinBrute(3, 25, [a.slam, a.rock_throw, s.StrengthBuff("Bulk", 2, 0, 2)])
