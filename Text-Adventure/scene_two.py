import scene
import created_items
import npc

class SceneTwo(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "scene2"
        self._description = "You find yourself in a small room. There is a door to the <a href='north'>North</a>."\
                            " There is a <a href='man'>man</a> sitting near the door. <br>"
        self._exits["north"] = "scene1"
        self._objects = [created_items.stick]
        self._locations = {}
        self._npcs = {"man": npc.man}

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