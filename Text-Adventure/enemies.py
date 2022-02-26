from character import *
import attacks as a
import spells as s


class Enemy(Character):
    def __init__(self, name, level, health, spell_list):
        super().__init__(name, level, health)
        self._spell_list = spell_list

    def get_spell_list(self):
        return self._spell_list


class Slime(Enemy):
    # basic slime, no resistances or weaknesses
    def __init__(self, level, health, spell_list):
        super().__init__("Slime", level, health, spell_list)


class Zombie(Enemy):
    # basic zombie, weak to fire
    def __init__(self, level, health, spell_list):
        super().__init__("Zombie", level, health, spell_list)
        self._weaknesses = ["Fire"]


class Mimic(Enemy):
    # chest brought to life, resists melee but weak to fire
    def __init__(self, level, health, spell_list):
        super().__init__("Mimic", level, health, spell_list)
        self._resistances = ["Melee"]
        self._weaknesses = ["Fire"]


zombie = Zombie(1, 12, [a.bite])
slime = Slime(2, 10, [a.spit])
mimic = Mimic(2, 20, [a.bite, a.spit])
