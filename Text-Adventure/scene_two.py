import scene
import created_items
import npc

class SceneTwo(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "scene2"
        self._description = "You enter the next area, the door you passed through is to your <a href='north'>North</a>"\
                            " now. There is a <a href='merchant'>merchant</a> sitting near a tree. <br>"
        self._exits["north"] = "scene1"
        self._objects = [created_items.stick]
        self._locations = {}
        self._npcs = {"merchant": npc.merchant}

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