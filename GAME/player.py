from collections import OrderedDict
from random import *
import items
from parser_game import *
from map import *
from enemies import *
import os

name = ""
style = ""
health = 100
mana = 0
armor = 50
experience = 0
isAlive = True
inventory = []
damage = [0, 0]
chance = [0, 7]
current_room = rooms["Porch"]

a = ""

"""Here are all the characters that the player can choose from. They have health, name, inventory, armor. We
have planned for the future to make items that increase those stats. We will have different characters that use magic,
or ranged attacks. Depending on the type of the character you will be able to wear or not wear certain gear.
Currently mana and style are not used and they do not influence the game. We will add gear slots later on as well."""
civilian = {
    "name": "Innocent Civilian",
    "style": "pathetic",
    "health": 1100,
    "mana": 0,
    "armor": 60,
    "experience": 0,
    "isAlive": True,
    "inventory": [items.item_id, items.item_money, items.item_card, items.item_note, items.item_potion_health],

    "damage": [50, 100]  # random.randrange[0, 50]
    }


warrior = {
    "name": "Unknown Warrior",
    "style": "melee",
    "health": 1200,
    "mana": 100,
    "armor": 100,
    "experience": 0,
    "isAlive": True,
    "inventory": [items.item_id, items.item_money, items.item_card, items.item_note, items.item_potion_health],
    "damage": [75, 125]  # random.randrange[25, 100]
    }


mad_scientist = {
    "name": "Mad Scientist",
    "style": "a bit eccentric",
    "health": 800,
    "mana": 50,
    "armor": 50,
    "experience": 0,
    "isAlive": True,
    "inventory": [items.item_id, items.item_money, items.item_card, items.item_note, items.item_potion_health],
    "damage": [125, 200]  # random.randrange[0, 150]
    }


john_cena = {
    "name": "John Cena",
    "style": "brutal, swift death via pure power of will",
    "health": 2000,
    "mana": 400,
    "armor": 30,
    "experience": 0,
    "isAlive": True,
    "inventory": [items.item_id, items.item_money, items.item_card, items.item_note, items.item_potion_health],
    "damage": [150, 350]
    }


characters = OrderedDict([
    ("Civilian", civilian),
    ("Unknown Warrior", warrior),
    ("Mad Scientist", mad_scientist),
    ("John Cena", john_cena)])


characters_dict = {"Civilian": civilian,
                   "Unknown Warrior": warrior,
                   "Mad Scientist": mad_scientist,
                   "John Cena": john_cena}


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
            elif character_choice == normalise_input(mad_scientist["name"]):
                print_stats(mad_scientist)
                print("")
                set_stats(mad_scientist)
                a = mad_scientist
                return
            elif character_choice == normalise_input(john_cena["name"]):
                print_stats(john_cena)
                set_stats(john_cena)
                a = john_cena
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
    print("Your health: " + str(health))
    print("Your experience: " + str(experience))
    print()


def print_enemy_stats(enemy_fight):
    """This prints the stats that the enemy has."""
    print("Name: " + enemy_fight["name"])
    print("Style: " + enemy_fight["style"])
    print("Health: " + str(enemy_fight["health"]))
    print("Max damage: " + str(enemy_fight["damage"][1]))


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
    hit_chance = randrange(4, 10)
    if hit_chance <= 3:
        print("You missed!")
        damage_dealt = 0
    else:
        damage_dealt = randrange(damage[0], damage[1])
    if item_wood_sword in inventory:
        damage_dealt_a = damage_dealt * float(1.5)
    else:
        damage_dealt_a = damage_dealt
    critchance = randrange(chance[0], chance[1])
    print("You attacked and dealt " + str(damage_dealt) + " damage your enemy")
    if enemy_fight["armor"] == 0:
        if critchance == 1:
            new_damage_dealt = damage_dealt_a * 2
            print("You made a critical hit.")
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
        elif critchance == 6:
            new_damage_dealt = damage_dealt_a * 3
            print("You made a critical hit.")
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
        else:
            new_damage_dealt = damage_dealt_a
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
    elif 1 <= enemy_fight["armor"] <= 30:
        if critchance == 1:
            new_damage_dealt = damage_dealt_a * 2
            print("You made a critical hit.")
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
        elif critchance == 6:
            new_damage_dealt = damage_dealt_a * 3
            print("You made a critical hit.")
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
        else:
            new_damage_dealt = damage_dealt_a * float(0.25)
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
    elif 31 <= enemy_fight["armor"] <= 49:
        if critchance == 1:
            new_damage_dealt = damage_dealt_a * 2
            print("You made a critical hit.")
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
        elif critchance == 6:
            new_damage_dealt = damage_dealt_a * 3
            print("You made a critical hit.")
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
        else:
            new_damage_dealt = damage_dealt_a * float(0.35)
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
    elif 50 <= enemy_fight["armor"] <= 70:
        if critchance == 1:
            new_damage_dealt = damage_dealt_a * 2
            print("You made a critical hit.")
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
        elif critchance == 6:
            new_damage_dealt = damage_dealt_a * 3
            print("You made a critical hit.")
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
        else:
            new_damage_dealt = damage_dealt_a / 2
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
    elif 71 >= enemy_fight["armor"] <= 99:
        if critchance == 1:
            new_damage_dealt = damage_dealt_a * 2
            print("You made a critical hit.")
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
        elif critchance == 6:
            new_damage_dealt = damage_dealt_a * 3
            print("You made a critical hit.")
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
        else:
            new_damage_dealt = damage_dealt_a / float(2.75)
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
    elif enemy_fight["armor"] == 100:
        if critchance == 1:
            new_damage_dealt = damage_dealt_a * 2
            print("You made a critical hit.")
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
        elif critchance == 6:
            new_damage_dealt = damage_dealt_a * 3
            print("You made a critical hit.")
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
        else:
            new_damage_dealt = damage_dealt_a / float(3.50)
            print("Your new damage is " + str(new_damage_dealt))
            enemy_fight["health"] = enemy_fight["health"] - new_damage_dealt
    return enemy_fight


# Taking damage from enemy
def take_damage(enemy_fight):
    """In this function we have the damage that the player receives from the enemies.
    We have armor reduction that is also part of this function.
    We print the damage that the enemy dealt to the player before and after the reduction from the armor.
    If the player is DEAD we print that the game is over.
    We use the global health, experience and isAlive to write this code."""
    # global armor
    global health
    global experience
    global isAlive
    damage_taken = randrange(enemy_fight["damage"][0], enemy_fight["damage"][1])
    critchance = randrange(enemy_fight["chance"][0], enemy_fight["chance"][1])
    print("The enemy attacked you with a damage of " + str(damage_taken))
    # if item_leather_armor in inventory:
    #     armor += 20
    # else:
    #     armor = armor
    if armor <= 50:
        if critchance == 7:
            new_damage_taken = damage_taken * float(1.5)
            print("The enemy critically hit you.")
            print("The enemies attack has the effect " + str(new_damage_taken) +" damage.")
            # health = health - damage_taken/2 = damage_taken/2 + damage_taken
            # health = health - new_damage_taken = new_damage_taken + damage_taken
            health = health - new_damage_taken + damage_taken
        else:
            new_damage_taken = damage_taken / 2
            print("The enemies attack has the effect " + str(new_damage_taken) +" damage.")
            # health = health - damage_taken/2 = damage_taken/2 + damage_taken
            # health = health - new_damage_taken = new_damage_taken + damage_taken
            health = health - new_damage_taken + damage_taken
    elif armor > 51:
        if critchance == 7:
            new_damage_taken = damage_taken * float(1.5)
            print("The enemy critically hit you.")
            print("The enemies attack has the effect " + str(new_damage_taken) +" damage.")
            # health = health - damage_taken/2 = damage_taken/2 + damage_taken
            # health = health - new_damage_taken = new_damage_taken + damage_taken
            health = health - new_damage_taken + damage_taken
        else:
            new_damage_taken = damage_taken / 3
            print("The enemies attack has the effect " + str(new_damage_taken) +" damage.")
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


def potion_health():
    global health
    health += 100
    inventory.remove(items.item_potion_health)
    print("You have restored 100 health")
    print()


def potion_mana():
    global mana
    mana += 100
    inventory.remove(items.item_potion_mana)
    print("You have restored 100 mana")
    print()


def potion_damage():
    global damage
    damage *= 2
    inventory.remove(items.item_potion_damage)
    print("You have increased your damage twofold temporarily")
    print()


def potion_defense():
    global armor
    armor += 10
    inventory.remove(items.item_potion_defense)
    print("You have increased your defense twofold temporarily")
    print()

potions = {
    "health": potion_health,
    "mana": potion_mana,
    "damage": potion_damage,
    "defense": potion_defense,
}


def combat(enemy_fight):
    """This is the combat function. Here the player and the enemy meet and deal damage to each other.
    First we check if there is an enemy in the room and if the enemy is in the list of enemies.
    We print that the player met an enemy. We tell the player to type a command in order to deal damage to the enemy.
    We will make it more interesting in the future when we ask the player to input different actions and not just ATTACK.
    We print the health and damage after every action. If you type ATTACK wrong, you will miss and deal 0 damage.
    Also we will add a timer for more pressure on the player. This might make the player miss spell and therefore
    miss the attack."""
    combat = [0, 6]
    print("You have come across a " + enemy_fight["name"])
    print()
    print("Here are their stats: ")
    print_enemy_stats(enemy_fight)
    print()
    print("Fight the enemy with all your might.")
    print()
    while enemy_fight["isAlive"] and isAlive:
        try:
            hit = randrange(combat[0], combat[1])
            if hit == 1:
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
                else:
                    print("You missed!")
                    print()
                    take_damage(enemy_fight)
                    print()
                    print_enemy_stats(enemy_fight)
                    print()
                    print_player(choice)
                    print("────────────────────────────────────────────────────────────")
            elif hit == 2:
                print("SWING to hit enemy!!!")
                print()
                if (normalise_input(input("> ")))[0] == "swing":
                    print()
                    attack_enemy(enemy_fight)
                    print()
                    take_damage(enemy_fight)
                    print()
                    print_enemy_stats(enemy_fight)
                    print()
                    print_player(choice)
                else:
                    print("You missed!")
                    print()
                    take_damage(enemy_fight)
                    print()
                    print_enemy_stats(enemy_fight)
                    print()
                    print_player(choice)
                    print("────────────────────────────────────────────────────────────")
            elif hit == 3:
                print("FIGHT to hit enemy!!!")
                print()
                if (normalise_input(input("> ")))[0] == "fight":
                    print()
                    attack_enemy(enemy_fight)
                    print()
                    take_damage(enemy_fight)
                    print()
                    print_enemy_stats(enemy_fight)
                    print()
                    print_player(choice)
                else:
                    print("You missed!")
                    print()
                    take_damage(enemy_fight)
                    print()
                    print_enemy_stats(enemy_fight)
                    print()
                    print_player(choice)
                    print("────────────────────────────────────────────────────────────")
            elif hit == 4:
                print("STAB to hit enemy!!!")
                print()
                if (normalise_input(input("> ")))[0] == "stab":
                    print()
                    attack_enemy(enemy_fight)
                    print()
                    take_damage(enemy_fight)
                    print()
                    print_enemy_stats(enemy_fight)
                    print()
                    print_player(choice)
                else:
                    print("You missed!")
                    print()
                    take_damage(enemy_fight)
                    print()
                    print_enemy_stats(enemy_fight)
                    print()
                    print_player(choice)
                    print("────────────────────────────────────────────────────────────")
            elif hit == 5:
                print("POKE to hit enemy!!!")
                print()
                if (normalise_input(input("> ")))[0] == "poke":
                    print()
                    attack_enemy(enemy_fight)
                    print()
                    take_damage(enemy_fight)
                    print()
                    print_enemy_stats(enemy_fight)
                    print()
                    print_player(choice)
                else:
                    print("You missed!")
                    print()
                    take_damage(enemy_fight)
                    print()
                    print_enemy_stats(enemy_fight)
                    print()
                    print_player(choice)
                    print("────────────────────────────────────────────────────────────")
            if enemy_fight["health"] < 0:
                enemy_fight["isAlive"] = False
                for item in enemy_fight["inventory"]:
                    current_room["items"].append(item)
                    enemy_fight["inventory"].remove(item)
        except:
            print("You missed!")
            print()
            take_damage(enemy_fight)
            print()
            print_enemy_stats(enemy_fight)
            print()
            print_player(choice)
            print("────────────────────────────────────────────────────────────")
        if not enemy_fight["isAlive"]:
            for item in enemy_fight["inventory"]:
                current_room["items"].append(item)
                enemy_fight["inventory"].remove(item)
            
