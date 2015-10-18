# import random
# from parser_game import *
import player

HP_potion = {
    "id": "HP_potion",

    "name": "Health Potion",

    "description":
    "This potion will restore 100 health."
}

Mana_potion = {
    "id": "Mana_potion",

    "name": "Mana Potion",

    "description":
    "This potion will restore 100 mana."
}

Damage_potion = {
    "id": "Damage_potion",

    "name": "Damage Potion",

    "description":
    "The damage you deal is x2"
}

Defense_potion = {
    "id": "Defense_potion",

    "name": "Defense Potion",

    "description":
    "The defense you have is x2"
}

Reverse_potion = {
    "id": "Reverse_potion",

    "name": "Reverse Potion",

    "description":
    "This potion will reverse the action you type as input while this potion is active."
}

Vowel_potion = {
    "id": "Vowel_potion",

    "name": "Vowel Potion",

    "description":
    "You have to type your input without vowels while this potion is active."
}

Onekey_potion = {
    "id": "Onekey_potion",

    "name": "Onekey Potion",

    "description":
    "You have to type on character at a type while this potion is active."
}

Double_potion = {
    "id": "Double_potion",

    "name": "Double Potion",

    "description":
    "This potion makes you type your input twice for the action to take place."
}

Random_potion = {
    "id": "Random_potion",

    "name": "Random Potion",

    "description":
    "This potion can be any of the potions that are in the game"
}

all_items = {
    "HP_potion": HP_potion,
    "Mana_potion": Mana_potion,
    "Damage_potion": Damage_potion,
    "Defense_potion": Defense_potion,
    "Reverse_potion": Reverse_potion,
    "Vowel_potion": Vowel_potion,
    "Onekey_potion": Onekey_potion,
    "Double_potion": Double_potion,
    "Random_potion": Random_potion
}


def potions(input):
    while True:
        if player.inventory.append(HP_potion):
            print(HP_potion["description"])
        elif player.inventory.append(Mana_potion):
            print(Mana_potion["description"])
        elif player.inventory.append(Damage_potion):
            print(Damage_potion["description"])
        elif player.inventory.append(Defense_potion):
            print(Defense_potion["description"])
        else:
            if player.inventory.append(Reverse_potion):
                print("You drank a Reverse_potion")
                print(Reverse_potion["description"])
            elif player.inventory.append(Vowel_potion):
                print("You drank a Vowel_potion")
                print(Vowel_potion["description"])
            elif player.inventory.append(Onekey_potion):
                print("You drank a Onekey_potion")
                print(Onekey_potion["description"])
            elif player.inventory.append(Double_potion):
                print("You drank a Double_potion")
                print(Double_potion["description"])
            elif player.inventory.append(Random_potion):
                print("You drank a Random_potion")
                print(Random_potion["description"])
        if character == "Innocent Civilian":
            if input == 1:
#                print(HP_potion["description"])
                Players.health[0] = Players.health[0] + 100
                if Players.health[0] > 1000:
                    Players.health[0] = 1000
                print("Your health now is " + str(Players.health[0]))
                break
            elif input == 2:
#                print(Mana_potion["description"])
                Players.mana[0] = Players.mana[0] + 100
                if Players.health[0] > 0:
                    Players.health[0] = 0
                print("Your mana now is " + str(Players.mana[0]))
                break
            elif input == 3:
#                print(Damage_potion["description"])
                Players.minDmg + 20
                Players.maxDmg * 2
                print("Your minimum damage now is " + Players.minDmg)
                print("Your maximum damage now is " + Players.maxDmg)
                break
            elif input == 4:
#                print(Defense_potion["description"])
                Players.armor * 2
                print("Your armor now is " + Players.armor)
                break
            else:
                if Players.inventory.append(Reverse_potion):
                    input = reversed
                    break
                elif Players.inventory.append(Onekey_potion):
                    len(input) > 1
                    if len(input()) > 1:
                        print("1")
                        break
        if character == "Unknown Warrior":
            if input == 1:
#                print(HP_potion["description"])
                Players.health[1] = Players.health[1] + 100
                if Players.health[1] > 1200:
                    Players.health[1] = 1200
                print("Your health now is " + str(Players.health[1]))
                break
            elif input == 2:
#                print(Mana_potion["description"])
                Players.mana[1] = Players.mana[1] + 100
                if Players.health[1] > 100:
                    Players.health[1] = 100
                print("Your mana now is " + str(Players.mana[1]))
                break
            elif input == 3:
#                print(Damage_potion["description"])
                Players.minDmg + 20
                Players.maxDmg * 2
                print("Your minimum damage now is " + Players.minDmg)
                print("Your maximum damage now is " + Players.maxDmg)
                break
            elif input == 4:
#                print(Defense_potion["description"])
                Players.armor * 2
                print("Your armor now is " + Players.armor)
                break
            else:
                if Players.inventory.append(Reverse_potion):
                    input = reversed
                    break
                elif Players.inventory.append(Onekey_potion):
                    len(input) > 1
                    if len(input()) > 1:
                        print("1")
                        break
        if character == "Matt Morgan":
            if input == 1:
#                print(HP_potion["description"])
                Players.health[2] = Players.health[2] + 100
                if Players.health[2] > 800:
                    Players.health[2] = 800
                print("Your health now is " + str(Players.health[2]))
                break
            elif input == 2:
#                print(Mana_potion["description"])
                Players.mana[2] = Players.mana[2] + 100
                if Players.health[2] > 50:
                    Players.health[2] = 50
                print("Your mana now is " + str(Players.mana[2]))
                break
            elif input == 3:
#                print(Damage_potion["description"])
                Players.minDmg + 20
                Players.maxDmg * 2
                print("Your minimum damage now is " + Players.minDmg)
                print("Your maximum damage now is " + Players.maxDmg)
                break
            elif input == 4:
#                print(Defense_potion["description"])
                Players.armor * 2
                print("Your armor now is " + Players.armor)
                break
            else:
                if Players.inventory.append(Reverse_potion):
                    input = reversed
                    break
                elif Players.inventory.append(Onekey_potion):
                    len(input) > 1
                    if len(input()) > 1:
                        print("1")
                        break
        if character == "Kirill The God":
            if input == 1:
#                print(HP_potion["description"])
                Players.health[3] = Players.health[3] + 100
                if Players.health[3] > 2000:
                    Players.health[3] = 2000
                print("Your health now is " + str(Players.health[3]))
                break
            elif input == 2:
#                print(Mana_potion["description"])
                Players.mana[3] = Players.mana[3] + 100
                if Players.health[3] > 400:
                    Players.health[3] = 400
                print("Your mana now is " + str(Players.mana[3]))
                break
            elif input == 3:
#                print(Damage_potion["description"])
                Players.minDmg + 20
                Players.maxDmg * 2
                print("Your minimum damage now is " + Players.minDmg)
                print("Your maximum damage now is " + Players.maxDmg)
                break
            elif input == 4:
#                print(Defense_potion["description"])
                Players.armor * 2
                print("Your armor now is " + Players.armor)
                break
            else:
                if Players.inventory.append(Reverse_potion):
                    input = reversed
                    break
                elif Players.inventory.append(Onekey_potion):
                    len(input) > 1
                    if len(input()) > 1:
                        print("1")
                        break