import scene

class SceneOne(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "scene1"
        self._description = "You find yourself in a small and empty room. There is a door in the South wall. <br>"
        self._exits["south"] = "scene2"

    def get_name(self):
        return super().get_name()

    def get_description(self):
        return super().get_description()

    def get_exits(self):
        return super().get_exits()

    def get_scene_by_name(self, name):
        return super().get_scene_by_name(name)