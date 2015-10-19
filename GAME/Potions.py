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
    else:
        if Reverse_potion in choice["inventory"]:
            print("You drank a Reverse_potion")
            print(Reverse_potion["description"])
        elif Vowel_potion in choice["inventory"]:
            print("You drank a Vowel_potion")
            print(Vowel_potion["description"])
        elif Onekey_potion in choice["inventory"]:
            print("You drank a Onekey_potion")
            print(Onekey_potion["description"])
        elif Double_potion in choice["inventory"]:
            print("You drank a Double_potion")
            print(Double_potion["description"])
        elif Random_potion in choice["inventory"]:
            print("You drank a Random_potion")
            print(Random_potion["description"])


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
            else:
                print("Good Job")
                # if Players.inventory.append(Reverse_potion):
                #     input = reversed
                #     break
                # elif Players.inventory.append(Onekey_potion):
                #     len(input) > 1
                #     if len(input()) > 1:
                #         print("1")
                #         break