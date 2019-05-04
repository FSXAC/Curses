#!/usr/bin/env python

import curses
import time

def drawTextCenter(screen, x, y, text):
	"""
	This will draw the text in center mode
	"""

	new_x = x - len(text) // 2
	screen.addstr(y, new_x, text)
	screen.refresh()

def main(screen):

	# Note that modifying the properties here is ok because it's scoped
	# and will reset outside the wrapper
	curses.curs_set(0)

	# Using getmaxyx can get our screen dimensions
	height, width = screen.getmaxyx()

	# This will draw the text in the center of the screen
	drawTextCenter(screen, width // 2, height // 2, 'Hello world!')
	time.sleep(3)


# The warpper will automatically init some default properties
# The wrapper will also reset the properties upon exit
curses.wrapper(main)
