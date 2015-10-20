from map import *

enemy1 = {
    "name": "Haunted Ghost",
    "style": "ghostly",
    "health": 500,
    "armor": 0,
    "isAlive": True,
    "inventory": [HP_potion],
    "damage": [30, 60],
    "place": rooms["entrance"]
}


def set_stats_e(enemy1):
    global name_e
    global health_e
    global armor_e
    global isAlive_e
    global damage_e
    name_e = enemy1["name"]
    health_e = enemy1["heath"]
    armor_e = enemy1["armor"]
    isAlive_e = enemy1["isAlive"]
    damage_e = enemy1["damage"]