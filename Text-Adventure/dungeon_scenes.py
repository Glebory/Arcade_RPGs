import scene
import enemies as e
import created_items as ci


class SceneDungeonOne(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "dungeon1"
        self._description = "You enter the dungeon. the entrance is dimly lit with the occasional"\
                            " torch here and there. There is a musty, rotton smell, as if the area has"\
                            " been unoccupied for many years. There is a pathway deeper inside to your"\
                            " <u>North</u>.<br>"
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
                            " <u>North</u>, There are corridors both <u>East</u> and" \
                            " <u>West</u>. The entrance is to your South.<br>"
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
        self._description = "You walk through the corridor. It continues on going <u>North</u>, and"\
                            " the entrance is towards the <u>East</u>.<br>"
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
        self._description = "You walk through the corridor. It continues on going <u>North</u>, and"\
                            " the entrance is towards the <u>West</u>.<br>"
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
                            " you are two chests, one to the left and one to the right. <br>"
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
                            " against the wall. <br>"
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
        self._description = "You enter a room. At the back of the room is a single chest. <br>"
        self._exits["south"] = "dungeon4"
        self._objects = [ci.flame_sword, ci.coin]
        self._locations = {"chest": "A fine looking chest with hints of gold in its design."}
        self._npcs = {}
        self._enemy = e.goblin_brute
