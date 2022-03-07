import scene
import npc

class CharSel(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "char_select"
        self._description = "You can choose to play as one of the following classes by typing the class-name below: <br>"\
                            "Knight: Expert in the sword<br>Wizard: Master of Magic<br>Archer: Adept with the bow <br>"
        self._exits["south"] = ""
        self._exits["north"] = "scene1"
        self._exits["east"] = ""
        self._objects = []
        self._locations = {}
        self._npcs = {}