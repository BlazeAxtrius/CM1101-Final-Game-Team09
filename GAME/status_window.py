from curses import wrapper
import curses
import time
import pickle

# open the temp file which the value of health is stored in
op = open("shared.pkl", "rb")
import_health = pickle.load(op)


input_character = str(import_health["name"])
style = import_health["style"]
health = int(import_health["health"])
xp = import_health["xp"]
mana = import_health["mana"]
armor = import_health["armor"]
inventory = import_health["inventory"]
current_room = import_health["current_room"]

# closes the file again
op.close()

max_health = {
    "Innocent Civilian": 1100,
    "Unknown Warrior": 1200,
    "Mad Scientist": 800,
    "John Cena": 2000
    }

#this will need to be sourced using the pickle library like before



# this initialises the curses window
# start_color allows the interface color to be changed
# this may cause issues on windows, so disable if necessary
stdscr = curses.initscr()
curses.start_color()
stdscr.keypad(True)

# these lines assign text color and background color which can be called for a print statement
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_GREEN)
curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)


def main(stdscr):
    """ This is the main containment funciton for the status window. Running this function within 'wrapper' allows curses
    to be ended gracefully. The main loop is contained within this functions and it repeatedly fetches values stored in
    a temp file. A health bar is constructed using the fetched value for health, and strings are printed to the window
    and then cleared so that the loop can do the same again - allowing any text on the screen to change if a value has been
    updated. """

    # empty string to keep the python gods happy
    health_bar = ""

    # base value for counter seen at bottom of window
    x = 0

    # main loop. repeately fetches, and prints values from the temp file and makes them look pretty
    while True:
        # Open the temp file up again to read the contents at start of loop
        op = open("shared.pkl", "rb")
        import_health = pickle.load(op)
        
        # Fetching values from the imported dictionaries
        input_character = str(import_health["name"])
        style = import_health["style"]
        health = int(import_health["health"])
        xp = import_health["xp"]
        mana = import_health["mana"]
        armor = import_health["armor"]
        inventory = import_health["inventory"]
        current_room = import_health["current_room"]

        items = []
        items_2 = []
        for item in inventory:
            if len(items) < 10:
                items.append(item["id"])
            else:
                items_2.append(item["id"])
        items_joined = ', '.join(items)
        items_joined_2 = ', '.join(items_2)


        #Creates a visual healthbar which is proportional to the player's health integer
        # Creates a string full of "|"s, with a count equal to about 1/4 of the player's health (for scaling)
        for i in range(0, int((health/max_health[input_character])*100), 4):
            health_bar = "|" + health_bar

        # Adds spaces to the end of the string so that the containing box remains the same size
        health_bar = health_bar + (25-len(health_bar))*" "

        # Prints the playername
        stdscr.addstr(1, 0, " Player:  " + input_character + "         Style:  " + style + " "*100, curses.color_pair(1))

        # Prints out the healthbar and player 
        stdscr.addstr(2, 0, " Health: " + "[" + health_bar + "]" + " " + str(health) + "HP" + " "*100, curses.color_pair(1))

        # Prints the percentage health of the player
        stdscr.addstr(3, 0, " ------> " + str(int(round(health/(max_health[input_character])*100, 0))) + "%" + " "*150, curses.color_pair(1))

        # Prints the armor value of the player
        stdscr.addstr(4, 0, " Armor: " + str(armor) + " "*150, curses.color_pair(3))

        # Prints the mana value of the player
        stdscr.addstr(5, 0, " Mana: " + str(mana) + " "*150, curses.color_pair(3))

        # Prints the XP value of the player
        stdscr.addstr(6, 0, " XP: " + str(xp) + " "*150, curses.color_pair(3))
        
        # Prints the player's current inventory
        stdscr.addstr(7, 0, " Inventory: " + items_joined + " "*100, curses.color_pair(2))

        # Second line of inventory printeding to allow more items to fit onto screen
        stdscr.addstr(8, 0, " "*12 + items_joined_2 + " "*100, curses.color_pair(2))

        # Prints the player's current room
        stdscr.addstr(9, 0, " Current Room: " + current_room["name"] + " "*150, curses.color_pair(2))

        # Loop counter
        stdscr.addstr(10, 0, str(x) + " "*50)
        #del(l[0:2])
        #l.append("  ")
        #health = "".join(l)

        # Resets the healthbar back to an empty string, so that it can be rebuilt
        health_bar = ""

        # Update changes onto screen
        stdscr.refresh()
        #printing blank spaces clears any stray printed squares
        stdscr.addstr(1, 1, " "*200)
        stdscr.addstr(2, 1, " "*200)
        stdscr.addstr(3, 1, " "*200)
        stdscr.addstr(4, 1, " "*200)
        stdscr.addstr(5, 1, " "*200)
        stdscr.addstr(6, 1, " "*200)
        stdscr.addstr(7, 1, " "*200)
        stdscr.addstr(8, 1, " "*200)
        stdscr.addstr(9, 1, " "*200)
        stdscr.addstr(9, 1, " "*200)
        x += 1

        # tidy up at end of loop by closing file. Making it ready to open at start of next cycle
        op.close()

        # Adding wait time so that simulation does not flash by
        time.sleep(0.5)

        # this shit just doesn't work :(
        try:
            key = win.getkey()
        except: # in no delay mode getkey raise and exeption if no key is press 
            key = None
        if key == " ": # of we got a space then break
            break

wrapper(main)














