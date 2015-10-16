from collections import OrderedDict
import random

name = ["Innocent Civilian", "Unknown Warrior", "Matt Morgan", "Kirill The God"]
classes = ["basic", "warrior", "lecturer", "mage"]
print(str(name))
character = input("Which character would you like to play with?: ")
health = [1000, 1200, 800, 2000]
mana = [0, 100, 50, 400]
armor = [50, 100, 80, 30]
experience = 0

e_name = ["Haunted Ghost", "Evil Witch", "One-eyed Ogre", "Demon Knight", "Undead King"]
e_health = [500, 700, 1200, 1600, 2500]
e_armor = [0, 20, 40, 80, 120]

isAlive = True
minDmg = 0
maxDmg = 50
inventory = []
inventory_e = []

while True:
    if character == "Innocent Civilian":
        print("You are a " + character.lower() + ".")
        print("Your fighting style is " + classes[0] + ".")
        break
    elif character not in name:
        print("Character not found")
        character = input("Which character would you like to play with?: ")
    else:
        print("Your character is " + character + "!")
        if character == "Unknown Warrior":
            print("You are a " + classes[1] + "!")
        elif character == "Matt Morgan":
            print("You are a cool " + classes[2] + "!")
            print("For all intents and purposes use your lecturer skills to fight the enemies.")
        else:
            print("You are a " + classes[3] + "!")
        break

for b in name:
    if b == character:
        i = name.index(character)

for e in name:
    if e == e_name:
        e_i = name.index(e_name)


def print_stat_order(stats):

    stats = OrderedDict([("Name", name[i]), ("Class", classes[i]), ("Health", health[i]),
                         ("Armor", armor[i]), ("Experience", experience), "Alive", isAlive])

    e_stats = OrderedDict([("Name", name[e_i]), ("Health", health[e_i]), ("Armor", armor[e_i]), "Alive", isAlive])

    print("\nPLAYER STATUS:")

    for key_base, value_base in stats.items():
        print(key_base + ": " + str(value_base))

    print("\nENEMY STATUS:")

    for key_base, value_base in e_stats.items():
        print(key_base + ": " + str(value_base))

    return print_stat_order

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