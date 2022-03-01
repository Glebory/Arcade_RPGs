import scene
import created_items
import npc
import enemies as e

class SceneTwo(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "scene2"
        self._description = "You enter a small room from the <a href='north'>North</a> door."\
                            " There is a <a href='man'>man</a> sitting near a door to the <a href='west'>West</a>.<br>"
        self._exits["north"] = "scene1"
        self._exits["west"] = "scene2part2"
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

class SceneTwoPartTwo(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "scene2part2"
        self._description = "You see a door leading to <a href='north'>North</a> with a <a href='window'>window</a>"\
                            " next to it. You sense that there may be something valuable around.<br>"
        self._exits["north"] = "scene1"
        self._objects = [created_items.coin]
        self._locations = {"window": "You peek through the window and see the village.<br>"}
        self._npcs = {}
        self._enemy = e.slime

