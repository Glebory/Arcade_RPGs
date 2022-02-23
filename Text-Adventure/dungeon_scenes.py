import scene


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
        self._objects = []
        self._locations = {}
        self._npcs = {}  # enemy here?


class SceneDungeonTwo(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "dungeon2"
        self._description = "You enter the main hall. There is a sealed, sturdy door to your" \
                            " <u>North</u>, There are corridors both <u>East</u> and" \
                            " <u>West</u>. In front of you there is a shadowy figure...<br>"
        self._exits["south"] = "dungeon1"
        self._exits["north"] = "dungeon7"  # locked door?
        self._exits["east"] = "dungeon4"
        self._exits["west"] = "dungeon3"
        self._objects = []
        self._locations = {"door": "The giant stone door is locked shut. Only a key could open it.<br>"}
        self._npcs = {}  # enemy here?


class SceneDungeonThree(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "dungeon3"
        self._description = "You walk through the corridor. It continues on going <u>North</u>, and"\
                            " the entrance is towards the <u>East</u>. Suddenly from deeper within,"\
                            " an enemy attacks!<br>"
        self._exits["north"] = "dungeon5"
        self._exits["east"] = "dungeon2"
        self._objects = []
        self._locations = {}
        self._npcs = {}  # enemy here?


class SceneDungeonFour(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "dungeon4"
        self._description = "You walk through the corridor. It continues on going <u>North</u>, and"\
                            " the entrance is towards the <u>West</u>. From the shadows,"\
                            "  an enemy attacks!<br>"
        self._exits["north"] = "dungeon6"
        self._exits["west"] = "dungeon2"
        self._objects = []
        self._locations = {}
        self._npcs = {}  # enemy here?


class SceneDungeonFive(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "dungeon5"
        self._description = "You enter a small room. It is mostly empty, except in front of" \
                            " you are two chests, one to the left and one to the right. <br>"
        self._exits["south"] = "dungeon3"
        self._objects = []
        self._locations = {"right": "This chest has seen some wear and tear. There is an odd smell coming from it.",
                           "left": "This chest is rather dusty. It hasn't been touched in a while."}
        self._npcs = {}  # enemy here (mimic chest) ?


class SceneDungeonSix(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "dungeon6"
        self._description = "You enter a room. A long time ago this may have been someone's" \
                            " office, as there is a large table in the middle and some barrels" \
                            " against the wall. <br>"
        self._exits["south"] = "dungeon4"
        self._objects = []
        self._locations = {"table": "The table is covered in dust, dirt and rotted papers. Among the mess you"
                                    " see a rusty key.",
                           "barrels": "Wooden storage barrels, built to last."}
        self._npcs = {}


class SceneDungeonSeven(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "dungeon7"
        self._description = "You enter a room. At the back of the room is a single chest, but" \
                            " in your way stands a giant goblin brute. It attacks!<br>"
        self._exits["south"] = "dungeon4"
        self._objects = []
        self._locations = {"chest": "A fine looking chest with hints of gold in its design."}
        self._npcs = {}  # enemy here?
