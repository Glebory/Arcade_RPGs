from item import *

stick = Item("Stick", "A stick from a tree branch", 1)

longsword = Weapon("Longsword", "A sharp sword made from steel", 5, "Melee", 3)
flame_sword = Weapon("Flame Sword", "Fiery blade that catches fire when wielded", 50, "Fire", 7)

iron_armour = Armour("Iron Armour", "Metal armour made from iron", 6, "Melee", 5)

rock = Throwable("Rock", "A heavy rock", 2, 2)
bomb = Throwable("Bomb", "An explosive packed with gunpowder", 20, 10, "Fire")

heal_potion = HealthGiver("Healing Potion", "A deep red potion that restores some health", 8, 10)

str_tonic = StrengthGiver("Strength Tonic", "A tonic which makes the user stronger", 8, 3, 3)

