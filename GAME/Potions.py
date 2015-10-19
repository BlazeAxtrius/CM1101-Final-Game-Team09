import player
from Potions_items import *


def check_potions(choice):
    if HP_potion in choice["inventory"]:
        print(HP_potion["description"])
    elif Mana_potion in choice["inventory"]:
        print(Mana_potion["description"])
    elif Damage_potion in choice["inventory"]:
        print(Damage_potion["description"])
    elif Defense_potion in choice["inventory"]:
        print(Defense_potion["description"])


def check_potions_rev(choice):
    if Reverse_potion in choice["inventory"]:
        print("You drank a Reverse_potion")
        print(Reverse_potion["description"])
        choice["inventory"].remove(Reverse_potion)
        # while True:
        #     b = 0
        #     input = reversed
        #     if b <= 5:
        #         b += 1
        #         if b >= 5:
        #             input = reversed


def potions(input, choice):
    while True:
        if choice["name"]:
            if input == 1:
                choice["inventory"].remove(HP_potion)
                choice["health"] += 100
                if choice["health"] >= 900:
                    choice["health"] = 1000
                print("Your health now is " + str(choice["health"]))
                print("You have consumed a Health potion.")
                print(choice["inventory"])
                break
            elif input == 2:
                choice["invnetory"].remove(Mana_potion)
                choice["mana"] += 100
                if choice["mana"] >= 0:
                    choice["mana"] = 0
                print("Your mana now is " + str(player.characters["mana"]))
                print("You have consumed a Mana potion.")
                print(choice["inventory"])
                break
            elif input == 3:
                choice["damage"] *= 20
                print("Your minimum damage now is " + choice["damage"])
                print("You consumed a Damage potion")
                print(choice["inventory"])
                break
            elif input == 4:
                choice["armor"] *= 2
                print("Your armor now is " + choice["armor"])
                print("You consumed a Armor potion")
                print(choice["inventory"])
                break