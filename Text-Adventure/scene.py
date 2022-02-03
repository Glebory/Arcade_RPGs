class Scene:
    def __init__(self):
        self._name = ""
        self._description = ""
        self._exits = {"north": None, "south": None, "east": None, "west": None}

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_exits(self):
        return self._exits

    def get_scene_by_name(self, name):
        if name == self._name:
            return self
