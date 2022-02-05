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
        self._health = health
        self._strength = self._level * 1.5
        self._mana = self._level*5
        self._resistances = []
        self._weaknesses = []
        self._image = "image"
    
    def __str__(self):
        return self._name

    def set_health(self, amount):
        self._health = amount
    
    def get_health(self):
        return self._health
    
    def set_current_health(self, amount):
        self._health = amount
    
    def set_current_health(self):
        return self._health

    def get_strength(self):
        return self._strength

    def set_strength(self, amount):
        self._strength = amount

    def get_mana(self):
        return self._mana
    
    def set_mana(self, amount):
        self._mana = amount
    
    def get_current_mana(self):
        return self._current_mana
    
    def set_current_mana(self, amount):
        self._current_mana = amount 

    def get_resistances(self):
        return self._resistances
    
    def set_resistances(self, resistances):
        self._resistances = resistances
    
    def get_weaknesses(self):
        return self._weaknesses
    
    def set_weaknesses(self, weaknesses):
        self._weaknesses = weaknesses

class Player_swordsman(Character):
    #either the only player option or one of many, bard, mage, etc
    def __init__(self, name, level, health, resistances=[]):
        super().__init__(name, level, health)
        self._resistances = ["Melee"]



knight1 = Player_swordsman("Bertrand", 1, 10)
