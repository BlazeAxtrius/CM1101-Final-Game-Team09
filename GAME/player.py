from collections import OrderedDict
import random

civilian = {
    "name": "Innocent Civilian",
    "type": "pathetic",
    "health": 1000,
    "mana": 0,
    "armor": 50,
    "experience": 0,
    "isAlive": True,
    "inventory": [],
    "damage": [0,50]
    }

warrior = {
    "name": "Unknown warrior",
    "type": "melee",
    "health": 1200,
    "mana": 100,
    "armor": 100,
    "experience": 0,
    "isAlive": True,
    "inventory": [],
    "damage": [25,100]
    }

matt_morgan = {
    "name": "Matt Morgan",
    "type": "a bit eccentric",
    "health": 800,
    "mana": 50,
    "armor": 80,
    "experience": 0,
    "isAlive": True,
    "inventory": [],
    "damage": [0,150]
    }

kirill = {
    "name": "Kirill the God",
    "type": "brutal, swift death via pure power of will",
    "health": 2000,
    "mana": 400,
    "armor": 30,
    "experience": 0,
    "isAlive": True,
    "inventory": [],
    "damage": [100,500]
    }

characters = {
    "Civilian": civilian,
    "Warrior": warrior,
    "Matt Morgan": matt_morgan,
    "Kirill": kirill
    }


def choose_character():
    print("You find four names written down on a scrap of paper next to you.\nOne looks familiar... Yes... it's yours")

    for name in characters:
        print("\n" + str(characters[name]["name"]))
    
    character_choice = input("Which character would you like to play with?: ")

    for name in characters:
        if character_choice == name:
            character_found = True
        else:
            character_found = False
        
    if not character_found:
        print("That's not on the list, are you okay?")
    return (character_choice, character_found)

#player = civilian
def print_stats(player):
    print("You are the " + civilian["name"] + ".")
    print("Your fighting style is " + civilian["type"] + ".")
    print("You have " + str(civilian["health"]) + " health, " + str(civilian["mana"]) + " mana, and " + str(civilian["armor"]) + " armor.")

print_stats()

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
