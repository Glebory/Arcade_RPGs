import inventory


class Character:
    """
    Class representing characters, parent class to players and enemies. Maybe npc's
    level will alter health and strength so battles scale with player
    resistances is a list of dmage type resistances current options being melee, fire, water, earth, ranged
    """

    def __init__(self, name, level, health):
        self._name = name
        self._level = level
        self._total_health = health
        self._current_health = self._total_health
        self._strength = self._level * 1.5
        self._total_mana = self._level * 5
        self._current_mana = self._total_mana
        self._resistances = []
        self._weaknesses = []
        self._image = "image"

    def __str__(self):
        return self._name

    # keeps current health within bounds of total health
    def health_check(self):
        if self._current_health > self._total_health:
            self._current_health = self._total_health

    def set_total_health(self, amount):
        self._total_health = amount

    def get_total_health(self):
        return self._total_health

    def set_current_health(self, amount):
        self._current_health = amount
        self.health_check()

    def get_current_health(self):
        return self._current_health

    def take_damage(self, amount):
        self._current_health -= amount

    def take_healing(self, amount):
        self._current_health += amount
        self.health_check()

    def get_strength(self):
        return self._strength

    def set_strength(self, amount):
        self._strength = amount

    # keeps current mana within bounds of total mana
    def mana_check(self):
        if self._current_mana > self._total_mana:
            self._current_mana = self._total_mana
        elif self._current_mana < 0:
            self._current_mana = 0

    def get_total_mana(self):
        return self._total_mana

    def set_total_mana(self, amount):
        self._total_mana = amount

    def get_current_mana(self):
        return self._current_mana

    def set_current_mana(self, amount):
        self._current_mana = amount
        self.mana_check()

    def use_mana(self, amount):
        self._current_mana -= amount
        self.mana_check()

    def gain_mana(self, amount):
        self._current_mana += amount
        self.mana_check()

    def get_resistances(self):
        return self._resistances

    def give_resistance(self, resistance):
        if resistance not in self._resistances:
            self._resistances.append(resistance)

    def remove_resistance(self, resistance):
        if resistance in self._resistances:
            self._resistances.remove(resistance)

    def get_weaknesses(self):
        return self._weaknesses

    def give_weakness(self, weakness):
        if weakness not in self._weaknesses:
            self._weaknesses.append(weakness)

    def remove_weakness(self, weakness):
        if weakness in self._weaknesses:
            self._weaknesses.remove(weakness)


class Player_swordsman(Character):
    # either the only player option or one of many, bard, mage, etc
    def __init__(self, name, level, health, resistances=[]):
        super().__init__(name, level, health)
        self._resistances = ["Melee"]


knight1 = Player_swordsman("Bertrand", 1, 10)