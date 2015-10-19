from collections import OrderedDict
from map import rooms
import random
from Potions_items import *
import parser_game

inventory = []
current_room = rooms["Reception"]

a = ""

civilian = {
    "name": "Innocent Civilian",
    "type": "pathetic",
    "health": 1000,
    "mana": 0,
    "armor": 50,
    "experience": 0,
    "isAlive": True,
    "inventory": ["Phone", "gum", "wallet"],
    "damage": [0, 50]  # random.randrange[0, 50]
    }

# print("Name" + ": " + civilian["name"], "\n"
#       "Type" + ": " + civilian["type"], "\n"
#       "Health" + ": " + str(civilian["health"]), "\n"
#       "Mana" + ": " + str(civilian["mana"]), "\n"
#       "Armor" + ": " + str(civilian["armor"]), "\n"
#       "Experience" + ": " + str(civilian["experience"]), "\n"
#       "IsAlive" + ": " + str(civilian["isAlive"]), "\n"
#       "Inventory" + ": " + str(civilian["inventory"]), "\n"
#       "Damage" + ": " + str(civilian["damage"]) + "\n")

warrior = {
    "name": "Unknown Warrior",
    "type": "melee",
    "health": 1200,
    "mana": 100,
    "armor": 100,
    "experience": 0,
    "isAlive": True,
    "inventory": [],
    "damage": [25, 100]  # random.randrange[25, 100]
    }

# print("Name" + ": " + warrior["name"], "\n"
#       "Type" + ": " + warrior["type"], "\n"
#       "Health" + ": " + str(warrior["health"]), "\n"
#       "Mana" + ": " + str(warrior["mana"]), "\n"
#       "Armor" + ": " + str(warrior["armor"]), "\n"
#       "Experience" + ": " + str(warrior["experience"]), "\n"
#       "IsAlive" + ": " + str(warrior["isAlive"]), "\n"
#       "Inventory" + ": " + str(warrior["inventory"]), "\n"
#       "Damage" + ": " + str(warrior["damage"]) + "\n")

matt_morgan = {
    "name": "Matt Morgan",
    "type": "a bit eccentric",
    "health": 800,
    "mana": 50,
    "armor": 80,
    "experience": 0,
    "isAlive": True,
    "inventory": [],
    "damage": [0, 150]  # random.randrange[0, 150]
    }

# print("Name" + ": " + matt_morgan["name"], "\n"
#       "Type" + ": " + matt_morgan["type"], "\n"
#       "Health" + ": " + str(matt_morgan["health"]), "\n"
#       "Mana" + ": " + str(matt_morgan["mana"]), "\n"
#       "Armor" + ": " + str(matt_morgan["armor"]), "\n"
#       "Experience" + ": " + str(matt_morgan["experience"]), "\n"
#       "IsAlive" + ": " + str(matt_morgan["isAlive"]), "\n"
#       "Inventory" + ": " + str(matt_morgan["inventory"]), "\n"
#       "Damage" + ": " + str(matt_morgan["damage"]) + "\n")

kirill = {
    "name": "Kirill the God",
    "type": "brutal, swift death via pure power of will",
    "health": 2000,
    "mana": 400,
    "armor": 30,
    "experience": 0,
    "isAlive": True,
    "inventory": [],
    "damage": [100, 500]  # random.randrange[100, 500]
    }

# print("Name" + ": " + kirill["name"], "\n"
#       "Type" + ": " + kirill["type"], "\n"
#       "Health" + ": " + str(kirill["health"]), "\n"
#       "Mana" + ": " + str(kirill["mana"]), "\n"
#       "Armor" + ": " + str(kirill["armor"]), "\n"
#       "Experience" + ": " + str(kirill["experience"]), "\n"
#       "IsAlive" + ": " + str(kirill["isAlive"]), "\n"
#       "Inventory" + ": " + str(kirill["inventory"]), "\n"
#       "Damage" + ": " + str(kirill["damage"]) + "\n")

characters = OrderedDict([
    ("Civilian", civilian),
    ("Unknown Warrior", warrior),
    ("Matt Morgan", matt_morgan),
    ("Kirill The God", kirill)])


def choose_character(choice):
    global a
    while True:
        print("""You find four names written down on a scrap of paper next to you.
One looks familiar... Yes... it's yours""")

        for name in characters:
            print(str(characters[name]["name"]))

        character_choice = input("Which character would you like to play with?: ")
        character_choice = parser_game.normalise_input(character_choice)
        print(character_choice)
        for choice in characters:
            if character_choice == civilian["name"]:
                print_stats(character_choice)
                a = civilian
                return
            elif character_choice == warrior["name"]:
                print_stats(character_choice)
                a = warrior
                return
            elif character_choice == matt_morgan["name"]:
                print_stats(character_choice)
                a = matt_morgan
                return
            elif character_choice == kirill["name"]:
                print_stats(character_choice)
                a = kirill
                return
            else:
                print("That's not on the list, are you okay?")
                break
    return choice


def print_stats(character_choice):
    if character_choice == civilian["name"]:
        print("You are " + str(civilian["name"]) + ".")
        print("Your fighting style is " + str(civilian["type"]) + ".")
        print("You have " + str(civilian["health"]) + " health, " + str(civilian["mana"]) + " mana, and " + str(civilian["armor"]) + " armor.")

choose_character(input)


#print_stats()
# while True:
    # damage = float(random.randint(minDmg, maxDmg))
    # damage_2 = float(random.randint(minDmg, maxDmg))
    # damage = random.randint(0, 50)
    # damage_2 = random.randint(0, 50)
    # damage_armor_red_enemy = (damage - ((damage * (armor[e_i] / 100)) / 2))
    # damage_armor_red = (damage_2 - ((damage_2*(armor[i]/100))/2))

    # print("damage " + str(damage))
    # print("damage_2 " + str(damage_2))
    # print("damage_armor_red_enemy " + str(damage_armor_red_enemy))
    # print("damage_armor_red " + str(damage_armor_red))

    # def compute_experience(exp, dmg):
        # result = random.randint(0, dmg*2) + exp
        # return result

    # def take_damage(experience, dmg):
        # global health
        # health[i] = stats["Health"] - dmg
        # result = compute_experience(experience, dmg)
        # return result

    # def deal_damage(dmg):
        # e_health[e_i] = e_stats["Health"] - dmg

    # experience = compute_experience(experience, int(damage_armor_red_enemy))
    # experience = take_damage(experience, int(damage_armor_red))
    # deal_damage(damage_armor_red_enemy)

    # stats = OrderedDict([("Name", name[i]), ("Class", classes[i]), ("Health", health[i]), ("Armor", armor[i]), ("Experience", experience), "Alive", isAlive])

    # e_stats = OrderedDict([("Name", name[e_i]), ("Health", health[e_i]), ("Armor", armor[e_i]), "Alive", isAlive])

    # if health[i] <= 0:
        # isAlive = False
        # print("Your hero has been slain.\nGame Over!")
        # break
    # elif e_health[e_i] <= 0:
        # print(e_stats['Name'] + " has been slain! " + stats['Name'] + " is victorious!")
        # break

    # def print_player_stats():
        # for key_1, value in character.items():
            # print(key_1 + ": " + str(value))
        # print(character['Name'] + " survives!")

    # def print_player_stats_enemy():
        # for key_1, value in e_stats.items():
            # print(key_1 + ": " + str(value))
        # print(e_stats['Name'] + " survives!")

    # print("\nYour new stats: \n")
    # print_player_stats()
    # print("\nEnemy's new stats: \n")
    # print_player_stats_enemy()