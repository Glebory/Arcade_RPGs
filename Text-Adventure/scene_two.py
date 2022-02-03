import scene

class SceneTwo(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "scene2"
        self._description = "You enter the next area, the door you passed through is to your North now. <br>"
        self._exits["north"] = "scene1"

    def get_name(self):
        return super().get_name()

    def get_description(self):
        return super().get_description()

    def get_exits(self):
        return super().get_exits()

    def get_scene_by_name(self, name):
        return super().get_scene_by_name(name)