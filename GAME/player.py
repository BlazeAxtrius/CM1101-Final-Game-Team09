from collections import OrderedDict
from random import *
import items
from parser_game import *
from map import *
from enemies import *
import os
from Potions_items import *

name = ""
style = ""
health = 100
mana = 0
armor = 50
experience = 0
isAlive = True
inventory = []
damage = [0, 0]
current_room = rooms["Porch"]

a = ""

"""Here are all the characters that the player can choose from. They have health, name, inventory, armor. We
have planned for the future to make items that increase those stats. We will have different characters that use magic,
or ranged attacks. Depending on the type of the character you will be able to wear or not wear certain gear.
Currently mana and style are not used and they do not influence the game. We will add gear slots later on as well."""
civilian = {
    "name": "Innocent Civilian",
    "style": "pathetic",
    "health": 1000,
    "mana": 0,
    "armor": 600,
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
    "damage": [50, 150]  # random.randrange[0, 150]
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
    print("│                        │")
    for name in characters:
        print("│ " + str(characters[name]["name"]), end = '')
        for space in range(1, 26 - (len(str(characters[name]["name"])) + 2)):
            print(" ", end='')
        print("│")
        print("│                        │")
    print("│                        │")
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
        character_choice = normalise_input(character_choice)
        for name in characters:
            # print(alpha)
            # print(character_choice)
            # if alpha in character_choice:
            #     return alpha
            if character_choice == normalise_input(civilian["name"]):
                print_stats(civilian)
                set_stats(civilian)
                a = civilian
                return
            elif character_choice == normalise_input(warrior["name"]):
                print_stats(warrior)
                set_stats(warrior)
                a = warrior
                return
            elif character_choice == normalise_input(matt_morgan["name"]):
                print_stats(matt_morgan)
                print("")
                set_stats(matt_morgan)
                a = matt_morgan
                return
            elif character_choice == normalise_input(kirill["name"]):
                print_stats(kirill)
                set_stats(kirill)
                a = kirill
                return
            else:
                print("You need to pick something from the list.")
                break
    return choice


def print_game_over():
    print("  _____                 ____                 ______")
    print(" / ___/__ ___ _  ___   / __ \_  _____ ____  / / / /")
    print("/ (_ / _ `/  ' \/ -_) / /_/ / |/ / -_) __/ /_/_/_/")
    print("\___/\_,_/_/_/_/\__/  \____/|___/\__/_/   (_|_|_) ")
    print()


def print_player(player):
    """This print the stats that the player has."""
    global health
    global experience
    print("Health: " + str(health))
    print("Experience: " + str(experience))


def print_enemy_stats(enemy_fight):
    """This prints the stats that the enemy has."""
    print("Name: " + all_enemies[enemy_fight]["name"])
    print("Style: " + all_enemies[enemy_fight]["style"])
    print("Health: " + str(all_enemies[enemy_fight]["health"]))
    print("Max damage: " + str(all_enemies[enemy_fight]["damage"][1]))


def compute_experience(damage_taken):
    """This function gives the player experience depending on the damage that the player took from the enemy."""
    experience_gain = randrange(0, damage_taken*2 + 1)
    return experience_gain


# Taking damage from player

def attack_enemy(enemy_fight):
    """This is the damage that the player deals to the enemy. We print the damage dealt before and after the armor
    reduction. We have code that is currently not used but we plan on making more enemies in the future and
    to use these lines of code for them.
    """
    damage_dealt = randrange(damage[0], damage[1])
    print("You attacked and dealt " + str(damage_dealt) + " damage your enemy")
    if all_enemies[enemy_fight]["armor"] == 0:
        new_damage_dealt = damage_dealt
        print("Your new damage is " + str(new_damage_dealt))
        # enemy1["health"] = enemy1["health"] - new_damage_dealt = new_damage_dealt + damage_dealt
        all_enemies[enemy_fight]["health"] = all_enemies[enemy_fight]["health"] - new_damage_dealt
    elif 1 <= all_enemies[enemy_fight]["armor"] <= 30:
        new_damage_dealt = damage_dealt * float(0.25)
        print("Your new damage is " + str(new_damage_dealt))
        # enemy1["health"] = enemy1["health"] - new_damage_dealt = new_damage_dealt + damage_dealt
        all_enemies[enemy_fight]["health"] = all_enemies[enemy_fight]["health"] - new_damage_dealt + damage_dealt
    elif 31 <= all_enemies[enemy_fight]["armor"] <= 49:
        new_damage_dealt = damage_dealt * float(0.35)
        print("Your new damage is " + str(new_damage_dealt))
        # enemy1["health"] = enemy1["health"] - new_damage_dealt = new_damage_dealt + damage_dealt
        all_enemies[enemy_fight]["health"] = all_enemies[enemy_fight]["health"] - new_damage_dealt + damage_dealt
    elif 50 <= all_enemies[enemy_fight]["armor"] <= 70:
        new_damage_dealt = damage_dealt / 2
        print("Your new damage is " + str(new_damage_dealt))
        # enemy1["health"] = enemy1["health"] - new_damage_dealt = new_damage_dealt + damage_dealt
        all_enemies[enemy_fight]["health"] = all_enemies[enemy_fight]["health"] - new_damage_dealt + damage_dealt
    elif 71 >= all_enemies[enemy_fight]["armor"] <= 99:
        new_damage_dealt = damage_dealt / float(2.75)
        print("Your new damage is " + str(new_damage_dealt))
        # enemy1["health"] = enemy1["health"] - new_damage_dealt = new_damage_dealt + damage_dealt
        all_enemies[enemy_fight]["health"] = all_enemies[enemy_fight]["health"] - new_damage_dealt + damage_dealt
    elif all_enemies[enemy_fight]["armor"] == 100:
        new_damage_dealt = damage_dealt / float(3.50)
        print("Your new damage is " + str(new_damage_dealt))
        # enemy1["health"] = enemy1["health"] - new_damage_dealt = new_damage_dealt + damage_dealt
        all_enemies[enemy_fight]["health"] = all_enemies[enemy_fight]["health"] - new_damage_dealt + damage_dealt
    all_enemies[enemy_fight]["health"] = all_enemies[enemy_fight]["health"] - damage_dealt
    if all_enemies[enemy_fight]["health"] <= 0:
        all_enemies[enemy_fight]["isAlive"] = False
        all_enemies[enemy_fight]["health"] = 0
    return enemy_fight

# Taking damage from enemy


def take_damage(enemy_fight):
    """In this function we have the damage that the player receives from the enemies.
    We have armor reduction that is also part of this function.
    We print the damage that the enemy dealt to the player before and after the reduction from the armor.
    If the player is DEAD we print that the game is over.
    We use the global health, experience and isAlive to write this code."""
    global health
    global experience
    global isAlive
    damage_taken = randrange(all_enemies[enemy_fight]["damage"][0], all_enemies[enemy_fight]["damage"][1])
    print("The enemy attacked you with a damage of " + str(damage_taken))
    if armor <= 50:
        new_damage_taken = damage_taken / 2
        print("Enemy new damage is " + str(new_damage_taken))
        # health = health - damage_taken/2 = damage_taken/2 + damage_taken
        # health = health - new_damage_taken = new_damage_taken + damage_taken
        health = health - new_damage_taken + damage_taken
    elif armor > 51:
        new_damage_taken = damage_taken / 3
        print("Enemy new damage is " + str(new_damage_taken))
        # health = health - damage_taken/3 = damage_taken/3 + damage_taken
        # health = health - new_damage_taken = new_damage_taken + damage_taken
        health = health - new_damage_taken + damage_taken
    health = health - damage_taken
    experience = experience + compute_experience(damage_taken)
    if health <= 0:
        isAlive = False
        print('You are DEAD!')
        print_game_over()
        os._exit(1)
    return


def check_potions():
    """This function checks if the player has a potion in his inventory. We use
    this for when the player takes a potion. We want to print what the potion does
    so the person playing knows what he just took."""
    if HP_potion in inventory:
        print(HP_potion["description"])
    elif Mana_potion in inventory:
        print(Mana_potion["description"])
    elif Damage_potion in inventory:
        print(Damage_potion["description"])
    elif Defense_potion in inventory:
        print(Defense_potion["description"])


# def check_potions_rev():
#     if Reverse_potion in inventory:
#         print("You drank a Reverse_potion")
#         print(Reverse_potion["description"])
#         inventory.remove(Reverse_potion)
#         while True:
#             b = 0
#             input = reversed
#             if b <= 5:
#                 b += 1
#                 if b >= 5:
#                     input = reversed


def potion_health():
    global health
    health += 100
    inventory.remove(items.item_potion_health)
    print("You have restored 100 health")
    print()


def potion_mana():
    mana += 100
    inventory.remove(items.item_potion_mana)
    print("You have restored 100 mana")
    print()


def potion_damage():
    damage *= 2
    inventory.remove(items.item_potion_damage)
    print("You have increased your damage twofold temporarily")
    print()


def potion_defense():
    armor *= 2
    inventory.remove(items.item_potion_damage)
    print("You have increased your defense twofol temporarily")
    print()

potions = {
    "health": potion_health,
    "mana": potion_mana,
    "damage": potion_damage,
    "defense": potion_defense,
}


def combat():
    """This is the combat function. Here the player and the enemy meet and deal damage to each other.
    First we check if there is an enemy in the room and if the enemy is in the list of enemies.
    We print that the player met an enemy. We tell the player to type a command in order to deal damage to the enemy.
    We will make it more interesting in the future when we ask the player to input different actions and not just ATTACK.
    We print the health and damage after every action. If you type ATTACK wrong, you will miss and deal 0 damage.
    Also we will add a timer for more pressure on the player. This might make the player miss spell and therefore
    miss the attack."""
    for enemy in all_enemies:
        if all_enemies[enemy]["name"] == current_room["enemy"][0]["name"]:
            enemy_fight = enemy
            break
    print("You have come across a " + all_enemies[enemy_fight]["name"])
    print()
    print("Here are their stats: ")
    print_enemy_stats(enemy_fight)
    print()
    while all_enemies[enemy_fight]["isAlive"] and isAlive:
        try:
            print("ATTACK to deal damage")
            print()
            if (normalise_input(input("> ")))[0] == "attack":
                print()
                attack_enemy(enemy_fight)
                print()
                take_damage(enemy_fight)
                print()
                print_enemy_stats(enemy_fight)
                print()
                print_player(choice)
                if all_enemies[enemy_fight]["isAlive"] == False:
                    print("You killed your enemy!")
                    print("It dropped a Health potion")
                    current_room["items"].append(all_enemies[enemy_fight]["inventory"][0])
                    current_room["enemy"].remove(all_enemies[enemy_fight])
                    print("────────────────────────────────────────────────────────────")
                    print()
                    print()
                    break
                print("────────────────────────────────────────────────────────────")
                continue
            else:
                print("You missed!")
                print()
                take_damage(enemy_fight)
                print()
                print_enemy_stats(enemy_fight)
                print()
                print_player(choice)
                print("────────────────────────────────────────────────────────────")
        except:
            print("You missed!")
            print()
            take_damage(enemy_fight)
            print()
            print_enemy_stats(enemy_fight)
            print()
            print_player(choice)
            print("────────────────────────────────────────────────────────────")
