class Scene:
    def __init__(self):
        self._name = ""
        self._description = ""
        self._exits = {"north": None, "south": None, "east": None, "west": None}
        self._objects = []
        self._locations = {}
        self._npcs = {}
        self._enemy = None

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_exits(self):
        return self._exits

    def get_objects(self):
        return self._objects

    def remove_object(self, item):
        self._objects.remove(item)

    def get_locations(self):
        return self._locations

    def get_npcs(self):
        return self._npcs

    def get_enemy(self):
        return self._enemy

    def remove_enemy(self):
        self._enemy = None
