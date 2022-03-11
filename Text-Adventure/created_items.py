from item import *

coin = Item("Coin", "A round coin made from some metal", 1)
necklace = Item("Necklace", "A beautiful pearl necklace", 100)
venison = Item("Venison chunk", "A large chunk of deer meat", 5)


stick = Item("Stick", "A stick from a tree branch", 1)
d_key = Item("Dungeon Key", "A rusty key that was found in the dungeon", 1)

longsword = Weapon("Longsword", "A sharp sword made from steel", 5, "Melee", 3)
flame_sword = Weapon("Flame Sword", "Fiery blade that catches fire when wielded", 50, "Fire", 7)
ice_spear = Weapon("Ice Spear", "A short spear, the spearhead encrusted in ice", 50, "Water", 7)
staff = Weapon("Staff", "Arcane wooden staff", 5, "Melee", 1)
dagger = Weapon("Dagger", "A short dagger", 5, "Melee", 2)
icepick = Weapon("Icepick Dagger", "A razor-sharp dagger imbued with ice", 35, "Ice", 5)

cloth_armour = Armour("Cloth Armour", "Cheap clothing that offers little protection", 2, None, 2)
iron_armour = Armour("Iron Armour", "Metal armour made from iron", 10, "Melee", 5)
ice_armour = Armour("Ice Armour", "Leather armour coated in ice", 50, "Water", 5)
leather_armour = Armour("Leather Armour", "Light leather armour",10, "Ranged", 5)

rock = Throwable("Rock", "A heavy rock", 2, 2)
bomb = Throwable("Bomb", "An explosive packed with gunpowder", 20, 10, "Fire")

heal_potion = HealthGiver("Healing Potion", "A deep red potion that restores some health", 8, 10)

mana_potion = ManaGiver("Mana Potion", "A bright blue potion that restores some mana", 8, 10)

str_tonic = StrengthGiver("Strength Tonic", "A tonic which makes the user stronger", 8, 3, 3)

fire_resist = ResistanceGiver("Flame Tonic", "A tonic which gives the user fire resistance", 10, None, 5, "Fire")
