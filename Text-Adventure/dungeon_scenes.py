import scene
import enemies as e
import created_items as ci


class SceneDungeonOne(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "dungeon1"
        self._description = "You reach the dungeon entrance. The entrance is dimly lit with the occasional"\
                            " torch here and there. There is a musty, rotten smell, as if the area has"\
                            " been unoccupied for many years. There is a pathway deeper inside to your"\
                            " <a href='north'>North</a>. The exit is to your <a href='west'>West</a>.<br>"
        self._exits["west"] = "scene1"  # link back to village/hub here
        self._exits["north"] = "dungeon2"
        self._objects = [ci.mana_potion]
        self._locations = {}
        self._npcs = {}
        self._enemy = None


class SceneDungeonTwo(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "dungeon2"
        self._description = "You enter the main hall. There is a sealed, sturdy door to your" \
                            " <a href='north'>North</a>, There are corridors both <a href='east'>East</a> and" \
                            " <a href='west'>West</a>. The exit is to your <a href='south'>South</a>.<br>"
        self._exits["south"] = "dungeon1"
        self._exits["north"] = "dungeon7"  # locked door?
        self._exits["east"] = "dungeon4"
        self._exits["west"] = "dungeon3"
        self._objects = [ci.coin]
        self._locations = {"door": "The giant stone door is locked shut. Only a key could open it.<br>"}
        self._npcs = {}
        self._enemy = e.goblin


class SceneDungeonThree(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "dungeon3"
        self._description = "You walk through the corridor. It continues on going <a href='north'>North</a>, and"\
                            " the exit is towards the <a href='east'>East</a>.<br>"
        self._exits["north"] = "dungeon5"
        self._exits["east"] = "dungeon2"
        self._objects = []
        self._locations = {}
        self._npcs = {}  # enemy here?
        self._enemy = scene.generate([e.zombie, e.slime], [1, 1])


class SceneDungeonFour(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "dungeon4"
        self._description = "You walk through the corridor. It continues on going <a href='north'>North</a>, and"\
                            " the exit is towards the <a href='west'>West</a>.<br>"
        self._exits["north"] = "dungeon6"
        self._exits["west"] = "dungeon2"
        self._objects = []
        self._locations = {}
        self._npcs = {}
        self._enemy = scene.generate([e.zombie, e.slime], [1, 1])


class SceneDungeonFive(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "dungeon5"
        self._description = "You enter a small room. It is mostly empty, except in front of" \
                            " you are two chests, one to the left and one to the right. " \
                            "The exit is towards your <a href='south'>South</a>.<br>"
        self._exits["south"] = "dungeon3"
        self._objects = [ci.iron_armour]
        self._locations = {"right": "This chest has seen some wear and tear. There is an odd smell coming from it.",
                           "left": "This chest is rather dusty. It hasn't been touched in a while."}
        self._npcs = {}
        self._enemy = e.mimic


class SceneDungeonSix(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "dungeon6"
        self._description = "You enter a room. A long time ago this may have been someone's" \
                            " office, as there is a large table in the middle and some barrels" \
                            " against the wall. The exit is towards your <a href='south'>South</a>.<br>"
        self._exits["south"] = "dungeon4"
        self._objects = [scene.generate([ci.heal_potion, ci.str_tonic], [1, 1]), ci.coin, ci.d_key]
        self._locations = {"table": "The table is covered in dust, dirt and rotted papers. Among the mess you"
                                    " see a rusty key.",
                           "barrels": "Wooden storage barrels, built to last."}
        self._npcs = {}
        self._enemy = None


class SceneDungeonSeven(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "dungeon7"
        self._description = "You enter a room. At the back of the room is a single chest. " \
                            "The exit is towards your <a href='south'>South</a>.<br>"
        self._exits["south"] = "dungeon2"
        self._objects = [ci.flame_sword, ci.coin]
        self._locations = {"chest": "A fine looking chest with hints of gold in its design."}
        self._npcs = {}
        self._enemy = e.goblin_brute
