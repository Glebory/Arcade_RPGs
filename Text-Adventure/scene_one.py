import scene
import npc
import enemies as e

class SceneOne(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "scene1"
        self._description = "You look around and see a <a href='merchant'>merchant</a>. You came from the door in the"\
                            " <a href='south'>South</a> wall with a <a href='window'>window</a> next to it. There is" \
                            " also a hole in the wall to the <a href='north'>North</a>. To your " \
                            "<a href='east'>East</a> there are stairs leading underground. <br>"
        self._exits["south"] = "scene2"
        self._exits["north"] = "forest1"
        self._exits["east"] = "dungeon1"
        self._objects = []
        self._locations = {"window": "You peek through the window and find a tree.<br>"}
        self._npcs = {"merchant": npc.merchant}
        self._enemy = e.slime

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