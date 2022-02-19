import scene
import created_items
from character import *

class SceneForestOne(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest1"
        self._description = "You arrive at the forest, you can barely see the moon peek through the thick canopy above."\
                            " There is a smaller path leading <u>West</u> which splits off the main path. " \
                            "The main path continues <u>North</u>. To the <u>East</u> is rugged forest terrain with no path<br>"
        self._exits["north"] = "forest3"
        self._exits["east"] = "forest4"
        self._exits["west"] = "forest2"

        self._objects = [created_items.rock]
        self._locations = {}
        self._npcs = {}

    def get_name(self):
        return super().get_name()

    def get_description(self):
        return super().get_description()

    def get_exits(self):
        return super().get_exits()

    def get_objects(self):
        return super().get_objects()

    def get_locations(self):
        return super().get_locations()

    def get_npcs(self):
        return super().get_npcs()


class SceneForestTwio(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest2"
        self._description = "You follow the path <u>West</u> and arrive at a small grove. " \
                            "The main path continues <u>North</u>. To the <u>East</u> is rugged forest terrain with no path<br>"
        self._exits["north"] = "forest3"
        self._exits["south"] = ""
        self._exits["east"] = "forest4"
        self._exits["west"] = "forest2"

        self._objects = [created_items.stick]
        self._locations = {}
        self._npcs = {}

    def get_name(self):
        return super().get_name()

    def get_description(self):
        return super().get_description()

    def get_exits(self):
        return super().get_exits()

    def get_objects(self):
        return super().get_objects()

    def get_locations(self):
        return super().get_locations()

    def get_npcs(self):
        return super().get_npcs()