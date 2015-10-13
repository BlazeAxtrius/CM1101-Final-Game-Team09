#!/usr/bin/python3

from map import rooms
import string

dire = ["east", "west", "north", "south"]


def remove_punct(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, "")
    return text

    
def remove_spaces(text):
    text = text.strip()
    return text


def normalise_input(text):
    text = text.lower()
    text_new = ""
    for ch in text:
        if ch in {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                  "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}:
            text_new = text_new + ch
#   remove_punct(text)
    return text_new

    
def display_room(room):
    print("\n" + str(room["name"]).upper() + "\n\n" + room["description"] + "\n")
#    print("""
#
#    """, str(room["name"]).upper(), """
#
#    """, room["description"], """
#
#    """)
    return

    
def exit_leads_to(exits, direction):

#    if direction not in exits:
#        return 0
#
#    return exits[direction]

    exit_room = exits[direction]
    exit_room = rooms[exit_room]["name"]

    return exit_room
    

def print_menu_line(direction, leads_to):
    if leads_to == 0:
        return 0
    else:
        return "Go " + direction.upper() + " to " + leads_to


def print_menu(exits):
    print("You can:")
    exit_list = []
    for ch in dire:
        if ch not in exits:
            pass
        else:
            exit_list.append(ch)
            print(print_menu_line(ch, exit_leads_to(exits, ch)))
    return exit_list


def is_valid_exit(exits, user_input):
    if user_input in exits:
        return True
    else:
        return False


def menu(exits):
    print_menu(exits)
    while True:
        user_input = input("\nUser: ")
        user_input = normalise_input(user_input)
        if is_valid_exit(exits, user_input):
            break
    return user_input


def move(exits, direction):
    return rooms[exits[direction]]


# This is the entry point of our program
def main():
    # Start game at the reception
    current_room = rooms["Reception"]

    # Main game loop
    while True:
        # status = 0

        display_room(current_room)

        exits = current_room["exits"]

        # print("Debug#3 " + str(current_room["name"]))
        # print("Debug#4 " + str(get_room_state(rooms_states["Reception"])) + "\n")
        direction = menu(exits)

        # status = 1
        # if current_room["name"] == "Reception" and get_room_state(rooms_states["Reception"]) == 3 and status == 0:
        #     print("IT IS TRUE")
        #     change_room_desc(current_room, 1)
        # print("Debug#1 " + str(current_room["name"]))
        # print("Debug#2 " + str(get_room_state(rooms_states["Reception"])) + "\n")

        current_room = move(exits, direction)


main()