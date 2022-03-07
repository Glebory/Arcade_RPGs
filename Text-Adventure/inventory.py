from item import *
"""
The players inventory, split into distinct sections for certain items.
Each item is stored as:
    "items name":[item_object, quantity]
This makes it easier to access in other classes that take input.
"""


# checks for presence of item in an inventory section, either adds
# it or adds to quantity
def addPresenceCheck(inv, item):
    if item.get_name() in inv:
        old_quantity = get_item_quantity(inv, item)
        inv[item.get_name()] = [item, old_quantity + 1]
    else:
        inv[item.get_name()] = [item, 1]


# checks for presence of item in an inventory section, either removes
# it completely or takes 1 from quantity
def removePresenceCheck(inv, item):
    if item.get_name() in inv:
        old_quantity = get_item_quantity(inv, item)
        inv[item.get_name()] = [item, old_quantity - 1]
        if get_item_quantity(inv, item) <= 0:
            inv.pop(item.get_name())


# retrieves item from inventory using its name
def get_item_object(inv, item):
    items_list = []
    for key in inv.keys():
        # when a player makes a choice its in upper case always
        items_list.append([key.upper(), key])
    for items in items_list:
        if item == items[0]:
            return (inv[items[1]])[0]


def get_item_quantity(inv, item):
    return (inv[item.get_name()])[1]


class Inventory:
    def __init__(self):
        self._weapons = {}
        self._armour = {}
        self._throwables = {}
        self._consumables = {}
        self._other = {}

    # adds to the corresponding section
    def add(self, item):
        if isinstance(item, Weapon):
            addPresenceCheck(self._weapons, item)
        elif isinstance(item, Armour):
            addPresenceCheck(self._armour, item)
        elif isinstance(item, Throwable):
            addPresenceCheck(self._throwables, item)
        elif isinstance(item, Consumable):
            addPresenceCheck(self._consumables, item)
        else:
            addPresenceCheck(self._other, item)

    # removes from the corresponding section
    def remove(self, item):
        if isinstance(item, Weapon):
            removePresenceCheck(self._weapons, item)
        elif isinstance(item, Armour):
            removePresenceCheck(self._armour, item)
        elif isinstance(item, Throwable):
            removePresenceCheck(self._throwables, item)
        elif isinstance(item, Consumable):
            removePresenceCheck(self._consumables, item)
        else:
            removePresenceCheck(self._other, item)

    def get_weapons(self):
        return self._weapons

    def get_armour(self):
        return self._armour

    def get_throwables(self):
        return self._throwables

    def get_consumables(self):
        return self._consumables

    def get_other(self):
        return self._other

    def find_item(self, item_str):
        item = None
        if get_item_object(self._weapons, item_str.upper()):
            item = get_item_object(self._weapons, item_str.upper())
        if get_item_object(self._armour, item_str.upper()):
            item = get_item_object(self._armour, item_str.upper())
        if get_item_object(self._throwables, item_str.upper()):
            item = get_item_object(self._throwables, item_str.upper())
        if get_item_object(self._consumables, item_str.upper()):
            item = get_item_object(self._consumables, item_str.upper())
        if get_item_object(self._other, item_str.upper()):
            item = get_item_object(self._other, item_str.upper())
        return item

