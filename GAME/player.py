from collections import OrderedDict
from random import *
import items
import parser_game
from map import *
from enemies import *

name = ""
style = ""
health = 100
mana = 0
armor = 50
experience = 0
isAlive = True
inventory = []
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
    "inventory": [items.item_id, items.item_money, items.item_card, items.item_note, items.item_potion_health, item_rusty_key],

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
    "inventory": [items.item_id, items.item_money, items.item_card, items.item_note, items.item_potion_health, item_rusty_key],
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
    "inventory": [items.item_id, items.item_money, items.item_card, items.item_note, items.item_potion_health, item_rusty_key],
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
    "inventory": [items.item_id, items.item_money, items.item_card, items.item_note, items.item_potion_health, item_rusty_key],
    "damage": [100, 500]  # random.randrange[100, 500]
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
#    for key in player:
 #       if player:
  #          print(key + ": " + str(player[key]))
    global health
    global experience
    print("Health: " + str(health))
    print("Experience " + str(experience))


def print_enemy1(enemy):
    for key1 in enemy:
        print(key1 + ": " + str(enemy1[key1]))


def compute_experience(damage_taken):
    experience_gain = randrange(0, damage_taken*2 + 1)
    return experience_gain


def take_damage_enemy1(enemy1, damage_dealt):
    enemy1["health"] = enemy1["health"] - randrange(damage[0], damage[1])
    if enemy1["health"] <= 0:
        enemy1["isAlive"] = False
        enemy1["health"] = 0
    return enemy1


def take_damage(choice, damage_dealt):
    global health
    global experience
    global isAlive
    damage_taken = randrange(enemy1["damage"][0], enemy1["damage"][1])
    health = health - damage_taken
    experience = experience + compute_experience(damage_taken)
    if health <= 0:
        isAlive = False
        print('You are DEAD!')
    return choice


def check_potions():
    if HP_potion in inventory:
        print(HP_potion["description"])
    elif Mana_potion in inventory:
        print(Mana_potion["description"])
    elif Damage_potion in inventory:
        print(Damage_potion["description"])
    elif Defense_potion in inventory:
        print(Defense_potion["description"])


def check_potions_rev():
    if Reverse_potion in inventory:
        print("You drank a Reverse_potion")
        print(Reverse_potion["description"])
        inventory.remove(Reverse_potion)
        # while True:
        #     b = 0
        #     input = reversed
        #     if b <= 5:
        #         b += 1
        #         if b >= 5:
        #             input = reversed


def potion_health():
    global health
    health += 100
    inventory.remove(items.item_potion_health)
    print("You have restored 100 health")
    print()


def potion_effect(t):
    while True:
        if name:
            if input == "health potion":
                inventory.remove(HP_potion)
                health += 100
                print("Your health now is " + str(player.health))
                print("You have consumed a Health potion.")
                print(inventory)
                break
            elif input == str(2):
                inventory.remove(Mana_potion)
                mana += 100
                print("Your mana now is " + str(player.mana))
                print("You have consumed a Mana potion.")
                print(inventory)
                break
            elif input == str(3):
                inventory.remove(Damage_potion)
                damage *= 20
                print("Your minimum damage now is " + player.damage)
                print("You consumed a Damage potion")
                print(inventory)
                break
            elif input == str(4):
                inventory.remove(Defense_potion)
                armor *= 2
                print("Your armor now is " + player.armor)
                print("You consumed a Armor potion")
                print(inventory)
                break

potions = {
    "health potion": health,
}


def combat():
    for enemy in all_enemies:
        print("true")
        if enemy[rooms] == current_room[enemy]:
            print("true")
            enemy_fight = enemy
            print("true")
            print(enemy_fight[isAlive])
            while enemy_fight[isAlive] and isAlive:
                damage_dealt = damage
                damage_dealt = enemy_fight[0]
                take_damage_enemy1(enemy1, damage_dealt)
                take_damage(choice, damage_dealt)
                if input() == "strong":
                    print_enemy1(enemy1)
                    print()
                    print_player(choice)
                    print()
                    continue
                else:
                    input("Try again")
                print_enemy1(enemy1)
                print()
                print_player(choice)
                print("")
                print()
                if enemy_fight[isAlive] == False:
                    break
