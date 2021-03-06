import inventory as inv
import created_items as ci
import item
import attacks as a
import spells as s


# if adding a class, add in combat and textadventure as options

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
        self._strength = self._level * 2
        self._total_mana = self._level * 5
        self._current_mana = self._total_mana
        self._resistances = []
        self._weaknesses = []
        self._image = "image"

    def __str__(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_name(self):
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
    # either the only player option or one of many, archer, mage, etc
    def __init__(self, name, level, health, weapon, armour, resistances=[]):
        super().__init__(name, level, health)
        self._resistances = ["Earth"]
        self._weapon = weapon
        self._armour = armour
        self._inv = inv.Inventory()
        self._spells = []

    def get_weapon(self):
        return self._weapon

    def set_weapon(self, weapon):
        self._weapon = weapon

    def get_armour(self):
        return self._armour

    def set_armour(self, armour):
        self._armour = armour

    def get_inventory(self):
        return self._inv

    def add_item(self, item):
        self._inv.add(item)

    def remove_item(self, item):
        self._inv.remove(item)

    def get_spells(self):
        return self._spells

    def add_spell(self, spell):
        if spell not in self._spells:
            self._spells.append(spell)


class Player_wizard(Character):
    def __init__(self, name, level, health, weapon, armour, resistances=[]):
        super().__init__(name, level, health)
        self._resistances = ["Fire"]
        self._weapon = weapon
        self._armour = armour
        self._inv = inv.Inventory()
        self._spells = []

    def get_weapon(self):
        return self._weapon

    def set_weapon(self, weapon):
        self._weapon = weapon

    def get_armour(self):
        return self._armour

    def set_armour(self, armour):
        self._armour = armour

    def get_inventory(self):
        return self._inv

    def add_item(self, item):
        self._inv.add(item)

    def remove_item(self, item):
        self._inv.remove(item)

    def get_spells(self):
        return self._spells

    def add_spell(self, spell):
        if spell not in self._spells:
            self._spells.append(spell)


class Player_archer(Character):
    def __init__(self, name, level, health, weapon, armour, resistances=[]):
        super().__init__(name, level, health)
        self._resistances = ["Ranged"]
        self._weapon = weapon
        self._armour = armour
        self._inv = inv.Inventory()
        self._spells = []

    def get_weapon(self):
        return self._weapon

    def set_weapon(self, weapon):
        self._weapon = weapon

    def get_armour(self):
        return self._armour

    def set_armour(self, armour):
        self._armour = armour

    def get_inventory(self):
        return self._inv

    def add_item(self, item):
        self._inv.add(item)

    def remove_item(self, item):
        self._inv.remove(item)

    def get_spells(self):
        return self._spells

    def add_spell(self, spell):
        if spell not in self._spells:
            self._spells.append(spell)


knight1 = Player_swordsman("Swordsman", 1, 20, ci.longsword, ci.cloth_armour)
knight1.add_item(ci.heal_potion)
knight1.add_item(ci.heal_potion)
knight1.add_item(ci.heal_potion)
knight1.add_item(ci.mana_potion)
knight1.add_item(ci.bomb)
knight1.add_item(ci.bomb)
knight1.add_item(ci.str_tonic)
knight1.add_item(ci.fire_resist)

knight1.add_item(ci.coin)
knight1.add_item(ci.coin)
knight1.add_item(ci.coin)
knight1.add_item(ci.coin)
knight1.add_item(ci.coin)

knight1.add_spell(s.StrengthBuff("Enrage", 3, 5, 3))
knight1.add_spell(a.rock_throw)
knight1.add_spell(a.ice_fist)
knight1.set_total_mana(15)
knight1.set_current_mana(15)

wizard1 = Player_wizard("Wizard", 1, 15, ci.staff, ci.cloth_armour)
wizard1.add_item(ci.heal_potion)
wizard1.add_item(ci.heal_potion)
wizard1.add_item(ci.heal_potion)
wizard1.add_item(ci.mana_potion)
wizard1.add_item(ci.mana_potion)
wizard1.add_item(ci.mana_potion)

wizard1.add_item(ci.coin)
wizard1.add_item(ci.coin)
wizard1.add_item(ci.coin)
wizard1.add_item(ci.coin)
wizard1.add_item(ci.coin)

wizard1.add_spell(a.fireball)
wizard1.add_spell(a.shard)
wizard1.add_spell(a.earth_fist)
wizard1.add_spell(s.Heal("Minor Heal", 10, 5))

wizard1.set_total_mana(30)
wizard1.set_current_mana(30)

archer1 = Player_archer("Archer", 1, 18, ci.dagger, ci.leather_armour)
archer1.add_item(ci.heal_potion)
archer1.add_item(ci.heal_potion)
archer1.add_item(ci.heal_potion)
archer1.add_item(ci.mana_potion)
archer1.add_item(ci.mana_potion)

archer1.add_item(ci.coin)
archer1.add_item(ci.coin)
archer1.add_item(ci.coin)
archer1.add_item(ci.coin)
archer1.add_item(ci.coin)

archer1.add_spell(a.shoot1)
archer1.add_spell(a.fire_arrow)
archer1.add_spell(a.ice_arrow)
archer1.add_spell(s.Heal("Minor Heal", 10, 5))

archer1.set_total_mana(20)
archer1.set_current_mana(20)
