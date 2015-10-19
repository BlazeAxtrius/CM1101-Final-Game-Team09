from collections import OrderedDict
from map import rooms
from random import *
from items import *
from Potions_items import *
import parser_game
import map

name = ""
style = ""
health = 100
mana = 0
armor = 50
experience = 0
isAlive = True
inventory = [item_id, item_money, item_pen]
damage = [0, 0]
current_room = rooms["porch"]

a = ""

civilian = {
    "name": "Innocent Civilian",
    "style": "pathetic",
    "health": 1000,
    "mana": 0,
    "armor": 50,
    "experience": 0,
    "isAlive": True,
    "inventory": [item_id, item_money, item_card,item_note],
    "damage": [20, 50]  # random.randrange[0, 50]
    }


warrior = {
    "name": "Unknown Warrior",
    "style": "melee",
    "health": 1200,
    "mana": 100,
    "armor": 100,
    "experience": 0,
    "isAlive": True,
    "inventory": [item_id, item_money, item_card, item_note],
    "damage": [25, 100]  # random.randrange[25, 100]
    }


matt_morgan = {
    "name": "Matt Morgan",
    "style": "a bit eccentric",
    "health": 800,
    "mana": 50,
    "armor": 80,
    "experience": 0,
    "isAlive": True,
    "inventory": [item_id, item_money, item_card, item_note],
    "damage": [30, 150]  # random.randrange[0, 150]
    }


kirill = {
    "name": "Kirill the God",
    "style": "brutal, swift death via pure power of will",
    "health": 2000,
    "mana": 400,
    "armor": 30,
    "experience": 0,
    "isAlive": True,
    "inventory": [item_id, item_money, item_card, item_note],
    "damage": [100, 500]  # random.randrange[100, 500]
    }


enemy1 = {
    "name": "Haunted Ghost",
    "style": "ghostly",
    "health": 500,
    "armor": 0,
    "isAlive": True,
    "inventory": [HP_potion],
    "damage": [30, 60],
}


characters = OrderedDict([
    ("Civilian", civilian),
    ("Unknown Warrior", warrior),
    ("Matt Morgan", matt_morgan),
    ("Kirill The God", kirill)])


characters_dict = {"Civilian": civilian,
     "Unknown Warrior": warrior,
     "Matt Morgan": matt_morgan,
     "Kirill The God": kirill}


def print_choices():
    print("""You find four names written down on the scrap of paper you found
next to you. One looks familiar... Yes... it's yours""")
    print()
    print("┌────────────────────────┐")
    for name in characters:
        print("│ " + str(characters[name]["name"]), end = '')
        for space in range(1,26 -(len(str(characters[name]["name"])) + 2)):
            print(" ", end='')
        print("│")
    print("│                        │")
    print("""│ Who would you least    │
│ like to be?:           │""")
    print("└────────────────────────┘")        
    print("")
    print("Enter the character you thought of straight away.")


def print_stats(character_choice):
    print()
    print("You are now " + str(character_choice["name"]) + ".")
    print("Your fighting style is " + str(character_choice["style"]) + ".")
    print("You have " + str(character_choice["health"]) + " health, " + str(character_choice["mana"]) + " mana, and " + str(character_choice["armor"]) + " armor.")
    print()


def set_stats(character_choice):
    global name
    global style
    global health
    global mana
    global armor
    global experience
    global isAlive
    global inventory
    global damage
    name = character_choice["name"]
    style = character_choice["style"]
    health = character_choice["health"]
    mana = character_choice["mana"]
    armor = character_choice["armor"]
    experience = character_choice["experience"]
    isAlive = character_choice["isAlive"]
    inventory = character_choice["inventory"]
    damage = character_choice["damage"]


def choose_character(choice):
    global a
    while True:
        print_choices()
        character_choice = input("> ")
        character_choice = parser_game.normalise_input(character_choice)
        for name in characters:
            # print(alpha)
            # print(character_choice)
            # if alpha in character_choice:
            #     return alpha
            if character_choice == parser_game.normalise_input(civilian["name"]):
                print_stats(civilian)
                set_stats(civilian)
                a = civilian
                return
            elif character_choice == parser_game.normalise_input(warrior["name"]):
                print_stats(warrior)
                set_stats(warrior)
                a = warrior
                return
            elif character_choice == parser_game.normalise_input(matt_morgan["name"]):
                print_stats(matt_morgan)
                print("")
                set_stats(matt_morgan)
                a = matt_morgan
                return
            elif character_choice == parser_game.normalise_input(kirill["name"]):
                print_stats(kirill)
                set_stats(kirill)
                a = kirill
                return
            else:
                print("You need to pick something from the list.")
                break
    return choice


def print_player(player):
    for key in player:
        if player:
            print(key + ": " + str(player[key]))


def print_enemy1(enemy):
    for key1 in enemy:
        print(key1 + ": " + str(enemy1[key1]))


def compute_experience(damage):
    damage = randrange(0, damage*2 + 1)
    return damage


def take_damage_enemy1(enemy1, damage_dealt):
    enemy1["health"] = enemy1["health"] - choice["damage"]
    if enemy1["health"] <= 0:
        enemy1["isAlive"] = False
        enemy1["health"] = 0
    return enemy1


def take_damage(choice, damage_dealt):
    choice["health"] = choice["health"] - enemy1["damage"]
    choice["experience"] = choice["experience"] + compute_experience(damage)
    if choice["health"] <= 0:
        choice["isAlive"] = False
        choice["health"] = 0
        print('You are DEAD!')
    return choice


while enemy1["isAlive"] and isAlive:
    damage_dealt = damage
    damage_dealt = enemy1["damage"]
    take_damage_enemy1(enemy1, damage_dealt)
    take_damage(choice, damage_dealt)
    if input == "strong":
        continue
    else:
        input("Try again")
    print_enemy1(enemy1)
    print()
    print_player(choice)
    print("")
    print()
    if enemy1['isAlive'] == False:
        break