from character import *
from inventory import *
from item import *
import created_items as ci

class NPC(Character):
    def __init__(self, name, level, health):
        super().__init__(name, level, health)
        self._description = ""
        self._speech = ""
        self._commands = []

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_speech(self):
        return self._speech

    def set_speech(self, speech):
        self._speech = speech

    def get_commands(self):
        return self._commands

class Merchant(NPC):
    def __init__(self, name):
        super().__init__(name, 1, 1)
        self._description = "A person who trades various goods. <br>"
        self._speech = "Good day, would you like to <a href='buy'>Buy</a>, <a href='sell'>Sell</a> or just " \
                       "<a href='browse'>Browse</a>?<br>"
        self._inv = Inventory()

    def get_inventory(self):
        return self._inv

    def buy_from_merchant(self, item_str, player):
        item = self._inv.find_item(item_str)
        if not item:
            return "The merchant does not have " + item_str + ".<br>"
        item_cost = item.get_value()
        player_coins = get_item_quantity(player.get_inventory().get_other(), ci.coin)
        if player_coins >= item_cost:
            self._inv.remove(item)
            player.add_item(item)
            for i in range(item_cost):
                player.get_inventory().remove(ci.coin)
            return "You have bought: " + str(item.get_name()) + "<br>"
        elif player_coins < item_cost:
            return "Not enough coin!<br>"

    def sell_to_merchant(self, item_str, player):
        item = player.get_inventory().find_item(item_str)
        if not item:
            return "You do not have " + item_str + ".<br>"
        item_cost = item.get_value()
        player.remove_item(item)
        self._inv.add(item)
        for i in range(item_cost):
            player.add_item(ci.coin)
        return "You have sold: " + str(item.get_name()) + " for " + str(item_cost) + " coins.<br>"

    def merchant_browse(self):
        output_text = "Merchant " + str(self) + " has: <br>"
        inv = merchant._inv
        for weapon in inv.get_weapons().values():
            output_text += str(weapon[0]) + ". Value: " + str(weapon[0].get_value()) + "<br>"
        for armour in inv.get_armour().values():
            output_text += str(armour[0]) + ". Value: " + str(armour[0].get_value()) + "<br>"
        for throwable in inv.get_throwables().values():
            output_text += str(throwable[0]) + ". Value: " + str(throwable[0].get_value()) + "<br>"
        for consumable in inv.get_consumables().values():
            output_text += str(consumable[0]) + ". Value: " + str(consumable[0].get_value()) + "<br>"
        for other in inv.get_other().values():
            output_text += str(other[0]) + ". Value: " + str(other[0].get_value()) + "<br>"
        return output_text

# merchant for testing, change later
merchant = Merchant("Bob")
merchant.get_inventory().add(ci.heal_potion)
merchant.get_inventory().add(ci.longsword)

man = NPC("John", 1, 1)
man.set_description("A strange looking man.<br>")
man.set_speech("The man warns you about a creature on the other side of the door."
               " Remember to use attack/spell/item/flee during combat. Use 'help' for commands."
               "<br>")

fisherman = NPC("Adam", 1, 1)
fisherman.set_description("A Tall Fisherman.<br>")
fisherman.set_speech("The fisherman tells you ahead is an impassable waterfall and it would be best to turn back.<br>")

fishermans_son = NPC("Tommy", 1, 1)
fishermans_son.set_description("Young boy.<br>")
fishermans_son.set_speech("The young boy tells you that he saw a smuggler hiding behind the vines under a big cliff.<br>")