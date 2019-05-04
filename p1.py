#!/usr/bin/env python

import curses
import time

# Make a new screen
stdscr = curses.initscr()

# do not echo
curses.noecho()

# 'enter' key is not needed for getting input
curses.cbreak()

# get keypad inputs
stdscr.keypad(True)

# Hide blinking cursor
curses.curs_set(0)

# Draw string (y, x, string)
stdscr.addstr(5, 5, 'Hello world')

# Update the screen (with all previous drawing functions)
stdscr.refresh()

time.sleep(3)

# Reset whatever modifcation we did above
curses.echo()
curses.nocbreak()
stdscr.keypad(False)
curses.curs_set(1)

# End the screen
curses.endwin()

# It's quite difficult to keep track of the properties
# the scope of the stuff is hard, so a 'warpper' is needed