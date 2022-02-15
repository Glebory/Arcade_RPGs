import scene
import created_items

class SceneTwo(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "scene2"
        self._description = "You enter the next area, the door you passed through is to your <u>North</u> now." \
                            "There is a <u>man</u> sitting under a tree. <br>"
        self._exits["north"] = "scene1"
        self._objects = [created_items.stick]
        self._locations = {}
        self._npcs = {"man": "You talk to the man, he tells you to <u>search</u> the area.<br>"}

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