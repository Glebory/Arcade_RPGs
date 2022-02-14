from character import *


class Slime(Character):
    # basic slime, no resistances or weaknesses
    def __init__(self, level, health):
        super().__init__("Slime", level, health)


class Zombie(Character):
    # basic zombie, weak to fire
    def __init__(self, level, health):
        super().__init__("Zombie", level, health)
        self._weaknesses = ["Fire"]


class Mimic(Character):
    # chest brought to life, resists melee but weak to fire
    def __init__(self, level, health):
        super().__init__("Mimic", level, health)
        self._resistances = ["Melee"]
        self._weaknesses = ["Fire"]