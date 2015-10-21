from curses import wrapper
import curses
import time
import pickle

# open the temp file which the value of health is stored in
op = open("shared.pkl", "rb")
import_health = pickle.load(op)
health = int(import_health["health"])
input_character = str(import_health["name"])
inventory = import_health["inventory"]

# closes the file again
op.close()

max_health = {
    "Civillian": 1000,
    "Warrior": 1200,
    "Matt Morgan": 800,
    "Kirill the God": 2000
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
        op = open("shared.pkl", "rb")
        import_health = pickle.load(op)
        health = int(import_health["health"])

        #Creates a visual healthbar which is proportional to the player's health integer
        # Creates a string full of "|"s, with a count equal to about 1/4 of the player's health (for scaling)
        for i in range(0, int((health/max_health[input_character])*100), 4):
            health_bar = "█" + health_bar

        # Adds spaces to the end of the string so that the containing box remains the same size
        health_bar = health_bar + (25-len(health_bar))*" "

        stdscr.addstr(1, 0, " Player:  " + input_character + " "*100, curses.color_pair(1))

        # Prints out the healthbar and player 
        stdscr.addstr(2, 0, " Health: " + "[" + health_bar + "]" + " " + str(health) + "HP" + " "*50, curses.color_pair(1))

        # Prints the percentage health of the player
        stdscr.addstr(3, 0, "          " + str(int(round(health/(max_health[input_character])*100, 0))) + "%" + " ~~               " + " "*50, curses.color_pair(1))
        
        # Testing adding more lines to the curses output
        stdscr.addstr(4, 0, " Inventory: " + "torch, laptop, notepad, plank. " + " "*50, curses.color_pair(2))

        stdscr.addstr(5, 0, str(x) + " "*50)
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
        x += 1

        # tidy up at end of loop by closing file. Making it ready to open at start of next cycle
        op.close()

        # Adding wait time so that simulation does not flash by
        time.sleep(1)

        # this shit just doesn't work :(
        try:
            key = win.getkey()
        except: # in no delay mode getkey raise and exeption if no key is press 
            key = None
        if key == " ": # of we got a space then break
            break

wrapper(main)














