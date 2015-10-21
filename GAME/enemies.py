from map import *
from items import *

"""This is the enemies file. Here we have all the enemies. We give them their stats and then we use those stats
for the combat. We will make enemies drop certain items. In the future we will make them drop swords and armor which
will benefit the player. They will increase the players stats and he will have a better chance in beating the game.
"""

enemy1 = {
    "name": "Haunted Ghost",
    "style": "ghostly",
    "health": 400,
    "armor": 0,
    "isAlive": True,
    "inventory": [item_potion_health, item_wood_sword, item_potion_defense],
    "damage": [20, 50],
    "chance": [0, 15]
}

enemy2 = {
    "name": "Small Ogre",
    "style": "heavy",
    "health": 500,
    "armor": 20,
    "isAlive": True,
    "inventory": [item_potion_health],
    "damage": [50, 80],
    "chance": [0, 15]
}

enemy3 = {
    "name": "Angry Ogre",
    "style": "really heavy",
    "health": 600,
    "armor": 50,
    "isAlive": True,
    "inventory": [item_potion_health, item_potion_defense],
    "damage": [100, 130],
    "chance": [0, 15]
}

enemy4 = {
    "name": "Evil Witch",
    "style": "magic",
    "health": 800,
    "armor": 30,
    "isAlive": True,
    "inventory": [item_potion_health, item_potion_damage],
    "damage": [120, 160],
    "chance": [0, 15]
}

enemy5 = {
    "name": "Devils servant",
    "style": "semi-demonic",
    "health": 900,
    "armor": 60,
    "isAlive": True,
    "inventory": [item_potion_health, item_potion_damage],
    "damage": [140, 180],
    "chance": [0, 15]
}

enemy6 = {
    "name": "The Devil",
    "style": "completely demonic",
    "health": 1150,
    "armor": 100,
    "isAlive": True,
    "inventory": [item_potion_health],
    "damage": [160, 300],
    "chance": [0, 15]
}

all_enemies = {
    "Haunted Ghost": enemy1,
    "Small Orge": enemy2,
    "Angry Ogre": enemy3,
    "Evil Witch": enemy4,
    "Devils servant": enemy5,
    "The Devil": enemy6
}