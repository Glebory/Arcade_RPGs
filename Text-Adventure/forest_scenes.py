import scene
import created_items
from character import *
import enemies as e

class SceneForestOne(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest1"
        self._description = "You arrive at the forest, you can barely see the moon peek through the thick canopy above."\
                            " There is a smaller path leading <a href='west'>West</a> which splits off the main path. " \
                            "The main path continues <a href='north'>North</a>. To the <a href='east'>East</a> is rugged forest terrain with no path<br>"
        self._exits["north"] = "forest3"
        self._exits["east"] = "forest4"
        self._exits["west"] = "forest2"

        self._objects = [created_items.rock]
        self._locations = {}
        self._npcs = {}
        self._enemy=None

class SceneForestTwo(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest2"
        self._description = "You follow the smaller path west and arrive at a small grove. " \
                            "There is no path leading forward only back <a href='east'>East</a> from where you came"\
                            "In the centre of the grove you see the skeleton of a man "\
                            "suddenly a goblin springs from the brush!<br>"
        self._exits["north"] = ""
        self._exits["south"] = ""
        self._exits["east"] = "forest1"
        self._exits["west"] = ""

        self._objects = [created_items.stick] #after the fight teh skeleton will have something on him 
        self._locations = {}
        self._npcs = {}
        self._enemy=e.goblin


class SceneForestThree(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest3"
        self._description = "You follow the main path north you see nothing of notice " \
                            "until you arrive at a split in the roads, one path leads"\
                            "<a href='west'>West</a> and the other splits <a href='east'>East</a> "
        self._exits["north"] = ""
        self._exits["south"] = ""
        self._exits["east"] = "forest1"
        self._exits["west"] = ""

        self._objects = [created_items.coin]
        self._locations = {}
        self._npcs = {}
        self._enemy=None   