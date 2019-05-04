#!/usr/bin/env python

import curses
import time
import math

def circle(screen, x0, y0, r):
	def drawCircle(screen, xc, yc, x, y):
		x, y = int(x), int(y)
		screen.addstr(yc + y, xc + x, '*')
		screen.addstr(yc + y, xc - x, '*')
		screen.addstr(yc - y, xc + x, '*')
		screen.addstr(yc - y, xc - x, '*')
		screen.addstr(yc + x, xc + y, '*')
		screen.addstr(yc + x, xc - y, '*')
		screen.addstr(yc - x, xc + y, '*')
		screen.addstr(yc - x, xc - y, '*')
	
	x, y = 0, r
	d = 3 - 2 * r

	drawCircle(screen, x0, y0, x, y)
	while y >= x:

		x += 1
		if d > 0:
			y -= 1
			d += 4 * (x - y) + 10
		else:
			d += 4 * x + 6

		drawCircle(screen, x0, y0, x, y)

	screen.refresh()

def main(screen):

	frameCount = 0

	curses.curs_set(0)
	screen.nodelay(True)

	while True:

		# Get key input
		key = screen.getch()
		screen.clear()

		if key == ord('q'):
			break

		height, width = screen.getmaxyx()

		radius = 10 * (math.sin(frameCount * 0.05) + 1) + 5
		circle(screen, width // 2, height // 2, radius)

		frameCount += 1

curses.wrapper(main)
