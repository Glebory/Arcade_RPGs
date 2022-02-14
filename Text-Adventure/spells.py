import math


class Spell:
    """
    Class for spells which are not attacks, like healing and buffing spells.
    """
    def __init__(self, name, points, mana_cost):
        self._name = name
        self._points = points
        self._mana_cost = mana_cost
        self._flavour_text = ""

    def get_name(self):
        return self._name

    def get_points(self):
        return self._points

    def get_mana_cost(self):
        return self._mana_cost

    def get_flavour_text(self):
        return self._flavour_text


class Heal(Spell):
    """
    Heals the user for an amount of health.
    """
    def __init__(self, name, points, mana_cost):
        super().__init__(name, points, mana_cost)
        self._flavour_text = "heals themselves for %i health" % self._points

    def cast(self, character):
        character.take_healing(self._points)
        character.use_mana(self._mana_cost)

    def __str__(self):
        return "%s - Heals the user for %i health" % (self._name, self._points)


class TimedSpell(Spell):
    """
    Spell with a turn limit for how long it lasts on the user.
    """
    def __init__(self, name, points, mana_cost, turns):
        super().__init__(name, points, mana_cost)
        self._turns = turns

    def get_turns(self):
        return self._turns


class ResistanceBuff(TimedSpell):
    """
    Gives user a resistance for a set amount of turns.
    """
    def __init__(self, name, points, mana_cost, turns, resistance):
        super().__init__(name, points, mana_cost, turns)
        self._resistance = resistance
        self._flavour_text = "gives themselves %s resistance for %i turns" % (self._resistance, self._turns)

    def get_resistance(self):
        return self._resistance

    def cast(self, character):
        character.give_resistance(self._resistance)
        return self._turns

    def timeout(self, character):
        character.remove_resistance(self._resistance)

    def __str__(self):
        return "%s - Grants the user %s resistance for %i turns" % (self._name, self._resistance, self._turns)


class StrengthBuff(TimedSpell):
    """
    Gives user strength for a set amount of turns.
    """
    def __init__(self, name, points, mana_cost, turns):
        super().__init__(name, points, mana_cost, turns)
        self._flavour_text = "gives themselves %i strength for %i turns" % (self._points, self._turns)

    def cast(self, character):
        old_strength = character.get_strength()
        character.set_strength(old_strength + self._points)
        return self._turns

    def timeout(self, character):
        old_strength = character.get_strength()
        character.set_strength(old_strength - self._points)

    def __str__(self):
        return "%s - Enrages the user, giving %i strength for %i " \
               "turns" % (self._name, self._points, self._turns)


class StrengthDeBuff(TimedSpell):
    """
    Takes strength away from the target for a set amount of turns.
    """
    def __init__(self, name, points, mana_cost, turns):
        super().__init__(name, points, mana_cost, turns)
        self._flavour_text = "removes %i strength from the target for %i turns" % (self._points, self._turns)

    def cast(self, character):
        old_strength = character.get_strength()
        character.set_strength(old_strength - self._points)
        return self._turns

    def timeout(self, character):
        old_strength = character.get_strength()
        character.set_strength(old_strength + self._points)

    def __str__(self):
        return "%s - Weakens the target, removing %i strength for %i " \
               "turns" % (self._name, self._points, self._turns)
