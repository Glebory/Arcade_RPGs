#class representing attacks, both spells and melee attacks

class Attacks:
    def __init__(self, name, base_damage, damage_type, mana_cost):
        self._name = name
        self._base_damage = base_damage
        self._damage_type = damage_type
        self._mana_cost = mana_cost
    
class Melee(Attacks):
    def __init__(self, name, base_damage):
        super().__init__(name, base_damage)
        self._damage_type = "Melee"
        self._mana_cost = 0

class Fire(Attacks):
    def __init__(self, name, base_damage, mana_cost):
        super().__init__(name, base_damage, mana_cost)
        self._damage_type = "Fire"
        self._mana_cost = 5

class Ranged(Attacks):
    def __init__(self, name, base_damage):
        super().__init__(name, base_damage)
        self._damage_type = "Ranged"
        self._mana_cost = 5   



#examples
bite = Melee("Bite", 5)
fireball = Fire("Fireball", 10, 5)
