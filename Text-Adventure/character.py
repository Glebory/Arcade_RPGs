import inventory

class Character:
    #class representing characters, parent class to players and enemies. maybe npc's
    #level will alter health and strength so battles scale with player
    #resistances is a list of dmage type resistances current options being melee, fire, water, earth, ranged

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

    def take_damage(self, amount):
        self._health -= amount
    
    def take_healing(self, amount):
        self._health += amount

class Player_swordsman(Character):
    #either the only player option or one of many, bard, mage, etc
    def __init__(self, name, level, health, resistances=[]):
        super().__init__(name, level, health)
        self._resistances = ["Melee"]



knight1 = Player_swordsman("Bertrand", 1, 10)
