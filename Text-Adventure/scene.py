import random


# takes a list of objects (items/enemies) and list of numbers (equal lengths between lists)
# each object corresponds to a number
# e.g. in [a, b, c] [1, 2, 3], a -> 1, b -> 2, c -> 3
# the list of numbers are the chances for each choice when put over the total
# e.g. [1,2,3] total = 6, chance for a = 1/6, chance for b = 2/6, chance for c = 3/6
def generate(object_list, chance_list):
    chosen_object = random.choices(object_list, weights=chance_list)
    return chosen_object[0]  # returns a list... need to get [0] index for object


class Scene:
    def __init__(self):
        self._name = ""
        self._description = ""
        self._exits = {"north": None, "south": None, "east": None, "west": None}
        self._objects = []
        self._locations = {}
        self._npcs = {}
        self._enemy = None
        self._loot = None
        self._requirements = None

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def get_exits(self):
        return self._exits

    def get_objects(self):
        return self._objects

    def add_object(self, obj):
        self._objects.append(obj)

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

    def get_loot(self):
        return self._loot

    def remove_loot(self, string):
        self._loot.pop(string)

    def get_requirements(self):
        return self._requirements
