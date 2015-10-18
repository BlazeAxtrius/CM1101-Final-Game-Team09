# import random
from parser_game import *

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
    normalise_input(input())
    while True:
        if input == 1:
            print(HP_potion["description"])
            health = health + 100
            print("Your health now is " + health)
        elif input == 2:
            print(Mana_potion["description"])
            mana = mana + 100
            print("Your mana now is " + mana)
        elif input == 3:
            print(Damage_potion["description"])
            minDmg = minDmg + 20
            maxDmg = maxDmg * 2
            print("Your minimum damage now is " + minDmg)
            print("Your maximum damage now is " + maxDmg)
        elif input == 4:
            print(Defense_potion["description"])
            armor = armor * 2
            print("Your armor now is " + armor)
        else:
            if inventory.append(Reverse_potion):
                input = reversed
            elif inventory.append(Onekey_potion):
                len(input) > 1
                if len(input()) > 1:

