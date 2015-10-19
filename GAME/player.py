from collections import OrderedDict
from map import rooms
from random import *
from items import *
from Potions_items import *
import parser_game

name = ""
style = ""
health = 100
mana = 0
armor = 50
experience = 0
isAlive = True
inventory = [item_id, item_money, item_pen]
damage = [0, 0]
current_room = rooms["storage, F-1"]

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
    "style": "melee",
    "health": 1200,
    "mana": 100,
    "armor": 100,
    "experience": 0,
    "isAlive": True,
    "inventory": [item_id, item_money, item_card, item_note],
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
    "style": "a bit eccentric",
    "health": 800,
    "mana": 50,
    "armor": 80,
    "experience": 0,
    "isAlive": True,
    "inventory": [item_id, item_money, item_card, item_note],
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
    "style": "brutal, swift death via pure power of will",
    "health": 2000,
    "mana": 400,
    "armor": 30,
    "experience": 0,
    "isAlive": True,
    "inventory": [item_id, item_money, item_card, item_note],
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
        for choice in characters:
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