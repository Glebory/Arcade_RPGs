import scene

class SceneOne(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "scene1"
        self._description = "You find yourself in a small and empty room. There is a door in the <u>South</u> wall with a " \
                            "<u>window</u> next to it. <br>"
        self._exits["south"] = "scene2"
        self._exits["north"] = "forest1"
        self._objects = []
        self._locations = {"window": "You peek through the window and find a tree.<br>"}
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