from items import *
from map import rooms

carry_weight = 0
inventory = [item_id, item_laptop, item_money]

#calculate how much the player is carrying
for item in inventory:
    carry_weight += float(item["mass"])

# Start game at the reception
current_room = rooms["Reception"]
