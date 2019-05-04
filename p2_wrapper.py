#!/usr/bin/env python

import curses
import time

def main(screen):

	# Note that modifying the properties here is ok because it's scoped
	# and will reset outside the wrapper
	curses.curs_set(0)

	screen.addstr(4, 4, 'Hello world')
	screen.refresh()

	time.sleep(3)


# The warpper will automatically init some default properties
# The wrapper will also reset the properties upon exit
curses.wrapper(main)