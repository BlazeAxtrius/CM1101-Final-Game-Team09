from map import rooms
from room_states import change_room_state
from room_states import rooms_states
from room_states import change_description
from room_states import get_room_state
import random

dire = ["east", "west", "north", "south"]


def remove_punct(text):
    text_new = ""
    for ch in text:
        if ch in {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                  "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}:
            text_new = text_new + ch
    return text_new


def remove_spaces(text):
    text = text.strip()
    print(text)


def normalise_input(text):
    text = text.lower()
    text_new = ""
    for ch in text:
        if ch in {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                  "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}:
            text_new = text_new + ch
    return text_new


def display_room(room):
    print("\n\n" + str(room["name"]).upper() + "\n\n" + room["description"] + "\n\n")
    return


def exit_leads_to(exits, direction):
    #
    # room = exits[direction]
    #
    # x = ["Going " + direction + " will lead to " + room + ".",
    # room + " is to the " + direction + ".",
    # "By going " + direction + " you will get to " + room + ".",
    # room + " is located to the " + direction + ".",
    # "Going " + direction + " takes you to " + room + "."]
    # y = random.randint(0, 4)

    if direction not in exits:
        return 0

    return exits[direction]


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
        else:
            if user_input in dire:
                a = random.randint(0, 3)
                list_deny = ["Going " + user_input.upper() + " is not an option.",
                             "I cannot go " + user_input.upper() + ".",
                             "Walking " + user_input.upper() + " is impossible!",
                             "Something is blocking my path."]
                print(list_deny[a])
            else:
                print("\nPlease write a valid direction!\n")
    return user_input


def move(exits, direction):
    return rooms[exits[direction]]


def change_room_desc(current_room, index):
    change_room_state(current_room["name"], index)

    # Gets the new description as a string.
    a = rooms_states["Reception"]["state_" + str(change_description("Reception"))]

    # Changes the current description of the room to the new one.
    current_room["description"] = a


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
        if direction == "south" and get_room_state(rooms_states["Reception"]) == 1:
            change_room_desc(current_room, 3)
        #    status = 1
        # if current_room["name"] == "Reception" and get_room_state(rooms_states["Reception"]) == 3 and status == 0:
        #     print("IT IS TRUE")
        #     change_room_desc(current_room, 1)
        # print("Debug#1 " + str(current_room["name"]))
        # print("Debug#2 " + str(get_room_state(rooms_states["Reception"])) + "\n")

        current_room = move(exits, direction)

main()