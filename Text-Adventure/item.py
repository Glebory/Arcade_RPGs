class Item:
    """
    A simple class to create basic items, each having a name, description and monetary value.
    """
    def __init__(self, name, description, value):
        self._name = name
        self._description = description
        self._value = value

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_value(self):
        return self._value

    def __str__(self):
        return "%s: %s" % (self._name, self._description)


class Equipment(Item):
    """
    A class to create wearable equipment, which give a character stats.
    Sometimes have bonus damage types.
    """
    def __init__(self, name, description, value, bonus=None):
        Item.__init__(self, name, description, value)
        self._bonus = bonus

    def get_bonus(self):
        return self._bonus


class Weapon(Equipment):
    """
    A class to create weapons a character can wield, each having their own attack stat.
    The bonus changes the damage type of the weapon.
    """
    def __init__(self, name, description, value, bonus, attack):
        Equipment.__init__(self, name, description, value, bonus)
        self._attack = attack

    def get_attack(self):
        return self._attack

    def __str__(self):
        return"%s - %i Attack: %s" % (self._name, self._attack, self._description)


class Armour(Equipment):
    """
    A class to create sets of armour a character can wear, each having their own defense stat.
    The bonus adds a damage type resistance.
    """
    def __init__(self, name, description, value, bonus, defense):
        Equipment.__init__(self, name, description, value, bonus)
        self._defense = defense

    def get_defense(self):
        return self._defense

    def __str__(self):
        return"%s - %i Defense: %s" % (self._name, self._defense, self._description)


class Throwable(Item):
    """
    A class to create throwable items, which do flat damage and can have a damage type (usually ranged).
    """
    def __init__(self, name, description, value, damage, damage_type="Ranged"):
        Item.__init__(self, name, description, value)
        self._damage = damage
        self._damage_type = damage_type

    def get_damage(self):
        return self._damage

    def get_damage_type(self):
        return self._damage_type

    def __str__(self):
        return"%s - %i Damage: %s" % (self._name, self._damage, self._description)


class Consumable(Item):
    """
    A class to create consumable items that a character can eat or drink.
    Grants an effect based on the provided points value, like 10 points of Health or
    3 points of Attack.
    """
    def __init__(self, name, description, value, points=None, effect=None):
        Item.__init__(self, name, description, value)
        self._points = points
        self._effect = effect

    def get_points(self):
        return self._points

    def get_effect(self):
        return self._effect


class HealthGiver(Consumable):
    """
    A class to create consumable items which restore a character's health.
    """
    def __init__(self, name, description, value, points):
        Consumable.__init__(self, name, description, value, points)

    def consume(self, character):
        character.take_healing(self._points)

    def __str__(self):
        return"%s - Restores %i health: %s" % (self._name, self._points, self._description)


class TemporaryBuffer(Consumable):
    """
    A class to create consumable items which give a character a temporary bonus
    for a given number of turns.
    """

    def __init__(self, name, description, value, points, turns):
        Consumable.__init__(self, name, description, value, points)
        self._turns = turns

    def get_turns(self):
        return self._turns


class StrengthGiver(TemporaryBuffer):
    """
    A class to create consumable items which give a character a temporary bonus
    to their strength for a given number of turns.
    """
    def __init__(self, name, description, value, points, turns):
        TemporaryBuffer.__init__(self, name, description, value, points, turns)

    def consume(self, character):
        character._strength += self._points
        # code isnt correct/finished need to figure out turn count in combat will work and
        # how to give strength stat to a char (char.give_strength function?)

    def __str__(self):
        return"%s - Gives %i strength for %i turns: %s" % (self._name, self._points,
                                                          self._turns, self._description)


class ResistanceGiver(TemporaryBuffer):
    """
    A class to create consumable items which give a character a temporary resistance for
    a given number of turns.
    """

    def __init__(self, name, description, value, points, turns, resistance):
        TemporaryBuffer.__init__(self, name, description, value, points, turns)
        self._resistance = resistance

    def get_resistance(self):
        return self._resistance

    def consume(self, character):
        character._resistances.append(self._resistance)
        # same issues as StrengthGiver

    def __str__(self):
        return "%s - Gives %s resist for %i turns: %s" % (self._name, self._resistance,
                                                          self._turns, self._description)
