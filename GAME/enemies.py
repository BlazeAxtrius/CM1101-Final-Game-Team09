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
    "inventory": [item_potion_health],
    "damage": [30, 60],
    "chance": [0, 15]
}

enemy2 = {
    "name": "Small Ogre",
    "style": "heavy",
    "health": 500,
    "armor": 20,
    "isAlive": True,
    "inventory": [item_potion_health],
    "damage": [70, 110],
    "chance": [0, 15]
}

enemy3 = {
    "name": "Angry Ogre",
    "style": "really heavy",
    "health": 650,
    "armor": 70,
    "isAlive": True,
    "inventory": [item_potion_health],
    "damage": [120, 150],
    "chance": [0, 15]
}

enemy4 = {
    "name": "Evil Witch",
    "style": "magic",
    "health": 800,
    "armor": 30,
    "isAlive": True,
    "inventory": [item_potion_health],
    "damage": [130, 180],
    "chance": [0, 15]
}

enemy5 = {
    "name": "Devils servant",
    "style": "semi-demonic",
    "health": 900,
    "armor": 60,
    "isAlive": True,
    "inventory": [item_potion_health],
    "damage": [200, 240],
    "chance": [0, 15]
}

enemy6 = {
    "name": "The Devil",
    "style": "completely demonic",
    "health": 1150,
    "armor": 100,
    "isAlive": True,
    "inventory": [item_potion_health],
    "damage": [250, 300],
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