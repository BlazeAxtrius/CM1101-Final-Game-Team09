#!/usr/bin/python3

from map import *
import player
from items import *
from parser_game import *
from time import *

"""Pickle is going to create a file in your repo called 'shared.pkl'. This file contains the variables
i need for the status window to work. It does not matter if you delete it or not, so if it causes any
problems while pulling or pushing to Github, just delete it"""
import pickle


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:
    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'
    >>> list_of_items([item_id])
    'id card'
    >>> list_of_items([])
    ''
    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'
    """
    
    names = []
    for item in items:
        names.append(item["name"])
    names = ', '.join(names)
    return names
    

def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:
    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>
    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>
    >>> print_room_items(rooms["Admins"])
    (no output)
    """

    # check that the list of items is not empty
    if (room["items"] != ([])) and ((item_torch in player.inventory) or (rooms["Entrance"]["first_visit"] == True)):
        # prints the list of items
        print("There is a " + list_of_items(room["items"]) + " here.\n")
    elif item_torch in room["items"]:
        print("There is " + item_torch["name"] + " here.\n")
    else:
        print("")
    if (item_lamp in room["items"]) and not (item_torch in player.inventory):
        print("There is " + item_lamp["name"] + " here.\n")
    else:
        print("")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:
    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>
    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>
    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    
    # Check to detect items in the room
    if len(room["items"]) != 0:
        # Display items if they are present
        print_room_items(room)


def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:
    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:
    GO <EXIT NAME UPPERCASE> to <where it leads>.
    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def find_locked_door(direction):
    # Find the next room for given direction
    # next_room = rooms[player.current_room["exits"][direction]]
    next_room = rooms[player.current_room["exits"][direction]]
    # Search through each locked door
    for locked_door in locked_room_exits:
        # If the current room and next room correspond to the locked door and the door is locked
        if (player.current_room["name"] in locked_room_exits[locked_door]["rooms"]) and (next_room["name"] in locked_room_exits[locked_door]["rooms"]):
            return locked_door


def carrying_right_key(direction, inv_items):
    """This function returns whether the player is carrying the right key to be
    able to unlock the door in a certain direction
    """
    carrying_key = False
    locked_door = find_locked_door(direction)
    for key_search in inv_items:
        # If the key for the door is found
        if locked_room_exits[locked_door]["key_required"] == key_search["id"]:
            carrying_key = True
    return carrying_key


def exit_locked(direction):
    """This function checks, given the direction the user wishes to go 
    (e.g. south) and checks whether the door between the two rooms is locked.
    For example:
    >>> exit_locked("south")
    True
    >>> exit_locked("west")
    False
    """
    # Door is open unless found otherwise
    door_locked = False
    # Find the next room for given direction
    # next_room = exit_leads_to(player.current_room["exits"], direction)
    next_room = rooms[player.current_room["exits"][direction]]
    # Search through each locked door
    for locked_door in locked_room_exits:
        # If the current room and next room correspond to the locked door and the door is locked
        if (player.current_room["name"] in locked_room_exits[locked_door]["rooms"]) and (next_room["name"] in locked_room_exits[locked_door]["rooms"]) and locked_room_exits[locked_door]["locked"]:
            door_locked = True
    return door_locked


def wooden_plank_required(direction): 
    wooden_plank_needed = False
    locked_door = find_locked_door(direction)
    # If the current room and next room correspond to the locked door and the key is the plank
    if locked_room_exits[locked_door]["key_required"] == "plank":
        wooden_plank_needed = True
    return wooden_plank_needed  


def clue_required(direction): 
    clue_needed = False
    locked_door = find_locked_door(direction)
    # If the current room and next room correspond to the locked door and the key is the plank
    if locked_room_exits[locked_door]["key_required"] == "clue":
        clue_needed = True
    return clue_needed 


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print
    "TAKE <ITEM ID> to take <item name>."
    and for each item in the inventory print
    "DROP <ITEM ID> to drop <item name>."
    For example, the menu of actions available at the Reception may look like this:
    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?
    """
    if (item_lamp in inv_items) or (item_torch in inv_items) or (rooms["Entrance"]["first_visit"] == True):
        # Iterate over available exits
        for direction in exits:
            # Print the exit name and where it leads to
            print_exit(direction, exit_leads_to(exits, direction))
            # If there is a locked door and the player carries the right key
            if exit_locked(direction) and carrying_right_key(direction, inv_items) and not wooden_plank_required(direction) and not clue_required(direction):
                print("UNLOCK " + direction.upper() + " to unlock the " + direction + " door.")
            elif exit_locked(direction) and carrying_right_key(direction, inv_items) and wooden_plank_required(direction):
                print("USE PLANK " + direction.upper() + " to cover the gap in the floor to your " + direction + ".")
            elif exit_locked(direction) and carrying_right_key(direction, inv_items) and clue_required(direction):
                print("USE CLUE " + direction.upper() + " to work out how to get into the secret room to the " + direction + ".")
    if (item_torch in inv_items) or (rooms["Entrance"]["first_visit"] == True) :
        # For all possible item you can pick up
        for take_item in room_items:
            print("TAKE " + take_item["id"].upper() + " to take a " + take_item["name"] + ".")
    if (item_lamp in room_items) and not (item_torch in inv_items):
        print("TAKE " + item_lamp["id"].upper() + " to take a " + item_lamp["name"] + ".")
    if item_torch in room_items:
        print("TAKE " + item_torch["id"].upper() + " to take a " + item_torch["name"] + ".")
    print("VIEW inventory")
    print("What do you want to do?")


def print_inventory():
    try:
        print()
        print("You find on your person: \n")
        for item in player.inventory:
            print(item["id"].upper() + ", " + item["name"])
        print()
        print("What would you like to do?")
        print()
        print("USE <ITEM>")
        print("DROP <ITEM>")
        print("VIEW all item descriptions")
        print("EXIT inventory")
        player_command = normalise_input(input("> "))

        if player_command[0] == "use":
            for item in player.inventory:
                item_exists = False
                if player_command[1] == item["id"]:
                    use_item = player_command[1]
                    execute_use(use_item)
                    item_exists = True
                if not item_exists:
                    print("That makes no sense")
                    break
                print_inventory()
        elif player_command[0] == "view":
            print("Here is what you are carrying: ")
            for item in player.inventory:
                print("> " + item["name"].capitalize())
                print(item["description"])
                print()
            return
        elif command[0] == "drop":
            if len(command) > 1:
                execute_drop(command[1])
            else:
                print("Drop what?")
        elif player_command[0] == "exit":
            return
        else:
            print("That makes no sense")
            print_inventory()
    except:
        print("That makes no sense")
        print_inventory()
        

def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:
    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """

    return chosen_exit in exits


def current_weight(inv_items):
    # calculate how much the player is carrying
    carry_weight = 0
    for item in inv_items:
        carry_weight += item["mass"]
    return carry_weight


def execute_use(item):
    """This function looks for an item in the players inventory,
    removes it from the inventory, and then affects the player or the world state depending on the item"""
    for player_item in player.inventory:
        if item == player_item["id"]:
            if player_item["isPotion"]:
                print(player_item["description"])
                while True:
                    confirmation = normalise_input(input("Are you sure you want to use potion? (YES|NO) \n> "))
                    print()
                    if confirmation[0] == "yes":
                        player.potion_health()
                        
                    elif confirmation[0] == "no":
                        return
                    else:
                        print("Enter YES or NO to confirm whether to use the potion")
            else:
                print("You cannot use this item right now")


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    # direction = normalise_input(direction)
    if player.current_room == rooms["Entrance"]:
        if (direction == "east") and (rooms["Entrance"]["first_visit"] == True):
                player.current_room = rooms["Basement storage"]
                print("You crash through some weak floorboards into a storage room below")
                rooms["Entrance"]["first_visit"] = False
                locked_room_exits["Hole_In_Floor"]["locked"] = True
                return
    # If there is a valid exit and this door is not locked
    if is_valid_exit(player.current_room["exits"], direction) and not exit_locked(direction):
        # Move player into the next room
        player.current_room = rooms[player.current_room["exits"][direction]]
        print("You move in to the " + player.current_room["name"])
    # If the door between the two rooms is locked
    elif is_valid_exit(player.current_room["exits"], direction) and exit_locked(direction):
        if player.current_room == rooms["Ground floor west hallway"] and (direction == "west"):
            print("You need to find something to cover the hole first")
        else:
            print("This door is locked")
    else:
        print("You cannot go there") 


def execute_take(input_item_id, inv_items):
    """This function takes an input_item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    try:
        if (current_weight(inv_items) + all_items[input_item_id]["mass"]) > 12.0:
            print("You are carrying too much")        
        elif all_items[input_item_id] in player.current_room["items"]:
            player.current_room["items"].remove(all_items[input_item_id])
            player.inventory.append(all_items[input_item_id])
            if input_item_id == "torch":
                print("You can now see the floor and any items that may also be there.")
            if input_item_id == "lamp":
                print("""You can now see doors and other objects in the room, but the light,
isn't strong enough to see the floor""")
        else:
            print("You cannot take that.")
    except:
        print("You cannot take that.")
       

def execute_drop(input_item_id):
    """This function takes an input_item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    try:
        if all_items[input_item_id] in player.inventory:
            player.inventory.remove(all_items[input_item_id])
            player.current_room["items"].append(all_items[input_item_id])
        elif input_item_id not in player.inventory:
            print("You cannot drop that.")
    except:
        print("You cannot drop that")


def execute_unlock(direction, inv_items, special):
    """This function unlocks a door in a certain direction as long as the door
    is currently locked and the player is carrying the right key in the 
    inventory, inv_items.
    """
    # If there is a valid exit and this door is locked
    if is_valid_exit(player.current_room["exits"], direction) and exit_locked(direction):
        locked_door = find_locked_door(direction)
        # If the door is locked and you are carrying the right key
        if exit_locked(direction) and carrying_right_key(direction, inv_items):
            # Unlock the door
            locked_room_exits[locked_door]["locked"] = False
            if special == "plank":
                print("You have used the plank to cover the hole")
                player.inventory.remove(all_items["plank"])
            elif special == "clue":
                print("You managed to open the secret door, I wonder what is inside?")
            else:
                print("The " + direction + " door is now unlocked.")
        elif not carrying_right_key(direction, inv_items):
            if player.current_room == rooms["Ground floor west hallway"] and (direction == "west"):
                print("You need to find something to cover the hole first")
            else:
                print("You are not carrying the right key to unlock this door")
    # If the door between the two rooms is not locked
    elif is_valid_exit(player.current_room["exits"], direction) and not exit_locked(direction):
        if player.current_room == rooms["Ground floor west hallway"] and (direction == "west"):
            print("The hole is already covered")
        else:
            print("This door wasn't locked anyway")
    else:
        print("You cannot unlock that")


def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.
    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1], player.inventory)
        else:
            print("Take what?")

    elif (command[0] == "unlock") or ((command[0] == "use") and ((command[1] == "plank") or (command[1] == "clue"))):
            if len(command) > 1:
                if command[0] == "unlock":
                    execute_unlock(command[1], player.inventory, "")
                else:
                    execute_unlock(command[2], player.inventory, command[1])
            else:
                print("Unlock what?")

    elif command[0] == "view":
        print_inventory()
        
    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.
    """

    for all_enemies in player.current_room["enemy"]:
        if all_enemies in player.current_room["enemy"]:
            print("You met an enemy.")
            player.combat()

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")
    print()
    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:
    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


def victory():
    if player.current_room == rooms["Porch"] and (rooms["Entrance"]["first_visit"] == False):
        return True
    else:
        return False


def print_victory_message():
    print()
    print("""You finally made it out of the house alive! Why did you even 
decide to enter to start with?""")
    print("")
    print(" __  __            _      __          ______")
    print(" \ \/ /__  __ __  | | /| / /__  ___  / / / /")
    print("  \  / _ \/ // /  | |/ |/ / _ \/ _ \/_/_/_/ ")
    print("  /_/\___/\_,_/   |__/|__/\___/_//_(_|_|_)  ")


def intro():
    print("\n\n\n\n\n\n\n\n\n")
    print("""Oh God last night... The drink, the music... People being sick 
as usual... Maybe someone twerking? The images flood your mind as you drift
away once more.""")
    sleep(1)
    print("""\nYou look around, trying to work out where you are. A ruffled piece
of paper sits a metre away in the dirt right next to a rusty old key. You walk
over and pick up the paper and the key beside it.""")
    sleep(1)
    print("""\nYou unfold the piece of paper.""")
    print()
    sleep(1)
    player.choose_character(input)
    sleep(1)
    print("""\nYou don't really know whats going on, probably because you have a 
hangover, but you decide to carry on anyway and move onto the porch of 
the house in front of you.""")
    print()
    print("────────────────────────────────────────────────────────────")
    sleep(1)


def status_update():
    shared = {"health": player.health}
    fp = open("shared.pkl", "wb")
    pickle.dump(shared, fp)
    fp.close()


# This is the entry point of our program
def main():
    intro()
    # Main game loop
    while True:
        # Update the status screen with any changed values
        status_update()

        # Display game status (room description, inventory etc.)
        print_room(player.current_room)

        # Show the menu with possible actions and ask the player
        command = menu(player.current_room["exits"], player.current_room["items"], player.inventory)
        
        # Execute the player's command
        execute_command(command)

        if victory():
            print_victory_message()
            break

        print("────────────────────────────────────────────────────────────")


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()
