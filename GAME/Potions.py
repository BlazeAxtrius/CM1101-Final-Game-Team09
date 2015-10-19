import player
from Potions_items import *


def check_potions():
    if HP_potion in player.inventory:
        print(HP_potion["description"])
    elif Mana_potion in player.inventory:
        print(Mana_potion["description"])
    elif Damage_potion in player.inventory:
        print(Damage_potion["description"])
    elif Defense_potion in player.inventory:
        print(Defense_potion["description"])


def check_potions_rev():
    if Reverse_potion in player.inventory:
        print("You drank a Reverse_potion")
        print(Reverse_potion["description"])
        player.inventory.remove(Reverse_potion)
        # while True:
        #     b = 0
        #     input = reversed
        #     if b <= 5:
        #         b += 1
        #         if b >= 5:
        #             input = reversed


def potions(input):
    while True:
        if player.name:
            if input == str(1):
                player.inventory.remove(HP_potion)
                player.health += 100
                print("Your health now is " + str(player.health))
                print("You have consumed a Health potion.")
                print(player.inventory)
                break
            elif input == str(2):
                player.inventory.remove(Mana_potion)
                player.mana += 100
                print("Your mana now is " + str(player.mana))
                print("You have consumed a Mana potion.")
                print(player.inventory)
                break
            elif input == str(3):
                player.damage *= 20
                print("Your minimum damage now is " + player.damage)
                print("You consumed a Damage potion")
                print(player.inventory)
                break
            elif input == str(4):
                player.armor *= 2
                print("Your armor now is " + player.armor)
                print("You consumed a Armor potion")
                print(player.inventory)
                break