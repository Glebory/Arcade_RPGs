from character import *

class Slime(Character):
    #basic slime, no resistances or weaknesses
    def __init__(self, level, health):
        super().__init__(level, health)
        self._name = "Slime"
        
class Zombie(Character):
    #basic zombie, weak to fire
    def __init__(self, level, health):
        super().__init__(level, health)
        self._weaknesses = ["Fire"]
        self._name = "Zombie"