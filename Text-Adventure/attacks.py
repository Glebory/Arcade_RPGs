class Attacks:
    """
    Class representing attacks, both spells and melee attacks
    """
    def __init__(self, name, flavour_text, damage, damage_type, mana_cost):
        self._name = name
        self._flavour_text = flavour_text
        self._damage = damage
        self._damage_type = damage_type
        self._mana_cost = mana_cost

    def get_name(self):
        return self._name

    def get_flavour_text(self):
        return self._flavour_text

    def get_damage(self):
        return self._damage

    def get_damage_type(self):
        return self._damage_type

    def get_mana_cost(self):
        return self._mana_cost


class Melee(Attacks):
    def __init__(self, name, flavour_text, damage):
        super().__init__(name, flavour_text, damage, "Melee", 0)


class Fire(Attacks):
    def __init__(self, name, flavour_text, damage, mana_cost):
        super().__init__(name, flavour_text, damage, "Fire", mana_cost)


class Water(Attacks):
    def __init__(self, name, flavour_text, damage, mana_cost):
        super().__init__(name, flavour_text, damage, "Water", mana_cost)


class Earth(Attacks):
    def __init__(self, name, flavour_text, damage, mana_cost):
        super().__init__(name, flavour_text, damage, "Earth", mana_cost)


class Ranged(Attacks):
    def __init__(self, name, flavour_text, damage):
        super().__init__(name, flavour_text, damage, "Ranged", 0)


#examples
bite = Melee("Bite", "bites", 5)
fireball = Fire("Fireball", "casts a fireball", 10, 5)
shard = Water("Shards of Ice", "shoots shards of ice", 8, 5)
rock_throw = Earth("Rock Throw", "throws chunks of rock", 10, 5)
spit = Ranged("Spit", "spits green goo", 3)
