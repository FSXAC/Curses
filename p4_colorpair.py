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

	# Create color pairs
	# (id, foreground, background)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

	# Set the color as an attribute to the screen
	screen.attron(curses.color_pair(1))

	# Using getmaxyx can get our screen dimensions
	height, width = screen.getmaxyx()

	# This will draw the text in the center of the screen
	drawTextCenter(screen, width // 2, height // 2, 'Hello world!')

	# Stop the colors
	screen.attroff(curses.color_pair(1))
	time.sleep(3)


# The warpper will automatically init some default properties
# The wrapper will also reset the properties upon exit
curses.wrapper(main)
