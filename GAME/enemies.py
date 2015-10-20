from map import *
from items import *

enemy1 = {
    "name": "Haunted Ghost",
    "style": "ghostly",
    "health": 500,
    "armor": 0,
    "isAlive": True,
    "inventory": [item_potion_health],
    "damage": [30, 60],
}

enemy2 = {
    "name": "Small Ogre",
    "style": "heavy",
    "health": 800,
    "armor": 20,
    "isAlive": True,
    "inventory": [item_potion_health],
    "damage": [70, 110],
}

enemy3 = {
    "name": "Angry Ogre",
    "style": "really heavy",
    "health": 1000,
    "armor": 70,
    "isAlive": True,
    "inventory": [item_potion_health],
    "damage": [120, 150],
}

enemy4 = {
    "name": "Evil Witch",
    "style": "magic",
    "health": 1300,
    "armor": 30,
    "isAlive": True,
    "inventory": [item_potion_health],
    "damage": [130, 180],
}

enemy5 = {
    "name": "Devils servant",
    "style": "semi-demonic",
    "health": 1600,
    "armor": 60,
    "isAlive": True,
    "inventory": [item_potion_health],
    "damage": [200, 240],
}

enemy6 = {
    "name": "The Devil",
    "style": "completely demonic",
    "health": 2000,
    "armor": 100,
    "isAlive": True,
    "inventory": [item_potion_health],
    "damage": [250, 300],
}

all_enemies = {
    "Haunted Ghost": enemy1,
    "Small Orge": enemy2,
    "Angry Ogre": enemy3,
    "Evil Witch": enemy4,
    "Devils servant": enemy5,
    "The Devil": enemy6
}