import npc
import scene
import created_items as ci
from character import *
import enemies as e


class SceneForestOne(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest1"
        self._description = "The hole leads to a forest, you can barely see the moon peek through the thick canopy above.<br>" \
                            "There is a smaller path leading <a href='west'>West</a> which splits off the main path. " \
                            "The main path continues <a href='north'>North</a>. To the <a href='east'>East</a> is rugged forest terrain with no path." \
                            " <a href='south'>South</a> leads back towards the hole in the wall.<br>"
        self._exits["north"] = "forest3"
        self._exits["east"] = "forest4"
        self._exits["west"] = "forest2"
        self._exits["south"] = "scene1"

        self._objects = [ci.rock]
        self._locations = {}
        self._npcs = {}
        self._enemy = None


class SceneForestTwo(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest2"
        self._description = "You follow the smaller path west and arrive at a small grove. <br>" \
                            "There is no path leading forward only back <a href='east'>East</a> from where you came.<br>" \
                            "In the centre of the grove you see the dead remains of a man.<br>"
        self._exits["north"] = ""
        self._exits["south"] = ""
        self._exits["east"] = "forest1"
        self._exits["west"] = ""

        self._objects = [ci.heal_potion]
        self._locations = {"man": "Corpse of a villager"}
        self._npcs = {}
        self._enemy = None
        self._loot = {"man": e.zombie}


class SceneForestThree(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest3"
        self._description = "You follow the main path north you see nothing of notice " \
                            "until you arrive at a split in the roads, one path leads " \
                            "<a href='west'>West</a> and the other splits " \
                            "<a href='east'>East</a>. You can also return <a href='south'>South</a><br>"
        self._exits["north"] = ""
        self._exits["south"] = "forest1"
        self._exits["east"] = "forest6"
        self._exits["west"] = "forest5"

        self._objects = [ci.coin]
        self._locations = {}
        self._npcs = {}
        self._enemy = None


class SceneForestFour(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest4"
        self._description = "You head east off the path into the forest <br>" \
                            "The difficult terrain is hard to navigate but after a few miles you arrive at" \
                            " a river.<br> The river runs <a href='north'>Northerly</a>. The river is too deep and " \
                            "fast here to cross. You can also return <a href='west'>West</a> to the main path.<br>"
        self._exits["north"] = "forest7"
        self._exits["south"] = ""
        self._exits["east"] = ""
        self._exits["west"] = "forest1"

        self._objects = []
        self._locations = {"river": "Fast running river, things might get caught on the riverbank.",
                           "riverbank": "Muddy, plenty of useless debris here."}
        self._loot = {"river": e.frog, "riverbank": scene.generate([ci.necklace, ci.rock], [1, 1])}
        self._npcs = {}
        self._enemy = e.boar


class SceneForestFive(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest5"
        self._description = "You follow the split west.<br>After a mile or so you notice an eery lack of sound." \
                            " The bird song has stopped and all you hear is the faint whisper of the wind as it " \
                            "rustles the leaves of the trees above.<br> The path continues <a href='north'>North</a>" \
                            " or returns <a href='east'>East</a>.<br>"
        self._exits["north"] = "forest8"
        self._exits["south"] = ""
        self._exits["east"] = "forest3"
        self._exits["west"] = ""

        self._objects = []
        self._locations = {}
        self._npcs = {}
        self._enemy = None


class SceneForestSix(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest6"
        self._description = "You follow the path that split east.<br>" \
                            "On the side of the road you spot a small rucksack. <br>The path " \
                            "continues <a href='north'>North</a> or returns <a href='west'>West</a>.<br>"
        self._exits["north"] = "forest9"
        self._exits["south"] = ""
        self._exits["east"] = ""
        self._exits["west"] = "forest3"

        self._objects = []
        self._locations = {"rucksack": "An old rugged rucksack that has seen better days."}
        self._npcs = {}
        self._loot = {"rucksack": ci.heal_potion}
        self._enemy = None


class SceneForestSeven(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest7"
        self._description = "You follow the river north and soon see a single cabin and a <a " \
                            "href='fisherman'>fisherman</a> fishing with " \
                            "his <a href='son'>son</a> from their makeshift dock. <br>You can return <a " \
                            "href='south'>South</a><br> "
        self._exits["north"] = ""
        self._exits["south"] = "forest4"
        self._exits["east"] = ""
        self._exits["west"] = ""

        self._objects = [ci.coin]
        self._locations = {"cabin": "Solidly built wood cabin"}
        self._npcs = {"fisherman": npc.fisherman, "son": npc.fishermans_son}
        self._enemy = None
        self._loot = {"cabin": ci.mana_potion}


class SceneForestEight(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest8"
        self._description = "You continue north and see nothing of notice until you come across the dead body of a " \
                            "deer. <br>" \
                            "Some kind of animal tracks lead <a href='north'>North</a> and you" \
                            " can return <a href='south'>South</a><br>"
        self._exits["north"] = "forest10"
        self._exits["south"] = "forest5"
        self._exits["east"] = ""
        self._exits["west"] = ""

        self._objects = []
        self._locations = {"deer": " The body has large claw and bite marks in its side."}
        self._npcs = {}
        self._enemy = None
        self._loot = {"deer": ci.venison}


class SceneForestNine(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest9"
        self._description = "You follow the path north. <br>" \
                            "Eventually you arrive at the bottom of a cliff face which appears impassable. " \
                            "Loose, thick vines cover the cliff face. <br>" \
                            "You can return <a href='south'>South</a><br>"
        self._exits["north"] = ""
        self._exits["south"] = "forest6"
        self._exits["east"] = ""
        self._exits["west"] = ""

        self._objects = [ci.coin]
        self._locations = {"vines": "Behind the vines you find a small den, seemingly used by smugglers. Inside you "
                                    "can see a crate, chest and a barrel",
                           "crate": "A sturdy wooden crate",
                           "barrel": "A wooden barrel solid built with metal fasteners",
                           "chest": "A long chest, fit for storing long weapons"}
        self._npcs = {}
        self._loot = {"chest": ci.ice_spear, "barrel": ci.mana_potion, "crate": ci.ice_armour}
        self._enemy = e.bear


class SceneForestTen(scene.Scene):
    def __init__(self):
        super().__init__()
        self._name = "forest10"
        self._description = "After following the animal tracks for a mile or so you can make out the shape of a hut. " \
                            "The faint flicker of firelight is visible through the broken door. <br>You can return <a " \
                            "href='south'>South</a><br> "
        self._exits["north"] = ""
        self._exits["south"] = "forest8"
        self._exits["east"] = ""
        self._exits["west"] = ""

        self._objects = [ci.coin]
        self._locations = {"hut": "Hut fallen into disrepair, smells of rotting meat."}
        self._npcs = {}
        self._enemy = None
        self._loot = {"hut": e.werewolf}
