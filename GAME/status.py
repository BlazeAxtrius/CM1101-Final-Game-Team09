from curses import wrapper
import curses
import time

# this initialises the curses window
# start_color allows the interface color to be changed
# this may cause issues on windows, so disable if necessary


stdscr = curses.initscr()
curses.start_color()
stdscr.keypad(True)


def main(stdscr):


    #Creates a visual healthbar which is proportional to the player's health integer
    
    # Clear screen
    #health = "||||||||||||||||||||"

    #if 10 > health_no > 0:
    #    health = "~~CRITICAL HEALTH~~ "    

    health = ""
    health_no = 100

    for i in range(0, 20):

        # Creates a string full of "|"s, with a count equal to about 1/4 of the player's health (for scaling)
        for i in range(0, health_no, 4):
            health = "|" + health
        
        # Adds spaces to the end of the string so that the containing box remains the same size
        health = health + (25-len(health))*" "

        # Prints out the healthbar and player 
        stdscr.addstr(1, 1, "Health: " + "[" + health + "]" + " " + str(health_no) + "  ")

        # Prints the number of "|" characters for debugging purposes
        stdscr.addstr(2, 1, "Length of healthbar: " + str(health.count("|",)) + "  ")
        
        # Testing adding more lines to the curses output
        stdscr.addstr(3, 1, "Inventory: " + "torch, laptop, notepad, plank.")


        #del(l[0:2])
        #l.append("  ")
        #health = "".join(l)

        # Resets the healthbar back to an empty string, so that it can be rebuilt
        health = ""

        # Update changes onto screen
        stdscr.refresh()

        # Simulating damage being taken
        health_no -= 5

        # Adding wait time so that simulation does not flash by
        time.sleep(0.2)


def invert(stdscr):


    #Creates a visual healthbar which is proportional to the player's health integer
    
    # Clear screen
    #health = "||||||||||||||||||||"

    #if 10 > health_no > 0:
    #    health = "~~CRITICAL HEALTH~~ "    

    health = ""
    health_no = 0

    for i in range(0, 20):

        # Creates a string full of "|"s, with a count equal to about 1/4 of the player's health (for scaling)
        for i in range(0, health_no, 4):
            health = "|" + health
        
        # Adds spaces to the end of the string so that the containing box remains the same size
        if len(health) < 25:
            health = health + (25-len(health))*" "
        else:
            pass

        #Prints out the healthbar and player 
        stdscr.addstr(1, 1, "Health: " + "[" + health + "]" + " " + str(health_no) + "  ")

        stdscr.addstr(2, 1, "Length of healthbar: " + str(health.count("|",)) + "  ")
        
        stdscr.addstr(3, 1, "Inventory: " + "torch, laptop, notepad, plank.")


        #del(l[0:2])
        #l.append("  ")
        #health = "".join(l)
        health = ""

        stdscr.refresh()

        health_no += 5

        time.sleep(0.2)

    stdscr.addstr(5,5, "Get rickitty rekt son!")
    stdscr.refresh()

    time.sleep(1)
        

wrapper(main)

wrapper(invert)
