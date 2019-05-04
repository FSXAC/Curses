#!/usr/bin/env python

import curses
import time

def line(screen, x1, y1, x2, y2):
	# TODO: not working perfectly
	if x2 < x1:
		x1, x2 = x2, x1
		y1, y2 = y2, y1

	dx = x2 - x1
	dy = y2 - y1
	for x in range(x1, x2):
		y = y1 + dy * (x - x1) / dx
		screen.addstr(int(y), int(x), '*')
	
	screen.refresh()

def main(screen):
	curses.curs_set(0)
	curses.mousemask(curses.BUTTON1_PRESSED)

	x1, y1 = None, None

	while True:

		# Get key input
		key = screen.getch()
		# screen.clear()

		if key == curses.KEY_MOUSE:
			_, mouseX, mouseY, _, _ = curses.getmouse()

			screen.addstr(0, 0, '({}, {})'.format(mouseX, mouseY))
			screen.refresh()

			if not x1 and not y1:
				x1, y1 = mouseX, mouseY
			else:
				line(screen, x1, y1, mouseX, mouseY)
				x1, y1 = None, None				

		elif key == ord('q'):
			break
		
		elif key == ord('c'):
			screen.clear()

curses.wrapper(main)
