#!/usr/bin/env python

import curses
import time

def main(screen):
	number = [0, 0, 0, 0]
	index = 0

	def display(screen):
		# we want to display at the center of the screen
		height, width = screen.getmaxyx()

		size = (2 * len(number) - 1)
		width_2 = width // 2
		height_2 = height // 2

		start_x = width_2 - size // 2

		# Draw the top part
		screen.attroff(curses.color_pair(1))
		top_str = '^ ' * len(number)
		top_str = ' '.join(top_str.split(' '))
		screen.addstr(height_2 - 1, start_x, top_str)

		# Draw the center part
		for i, n in enumerate(number):
			if i == index:
				screen.attron(curses.color_pair(1))
			else:
				screen.attroff(curses.color_pair(1))

			# Draw the number themseleves
			screen.addstr(height_2, start_x + i * 2, str(n))

		# Draw the bottom part
		screen.attroff(curses.color_pair(1))
		top_str = 'v ' * len(number)
		top_str = ' '.join(top_str.split(' '))
		screen.addstr(height_2 + 1, start_x,  top_str)

		# screen.addstr(height_2, start_x, 'MUCHEN HE')
		screen.refresh()


	def increment(index):
		if number[index] == 9:
			number[index] = 0
		else:
			number[index] += 1


	def decrement(index):
		if number[index] == 0:
			number[index] = 9
		else:
			number[index] -= 1

	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

	display(screen)

	# Temp inf loop
	program_loop = True
	while program_loop:

		# Get key input
		key = screen.getch()
		screen.clear()

		if key == curses.KEY_UP:
			increment(index)
		elif key == curses.KEY_DOWN:
			decrement(index)
		elif key == curses.KEY_RIGHT:
			if index == len(number) - 1:
				index = 0
			else:
				index += 1
		elif key == curses.KEY_LEFT:
			if index == 0:
				index = len(number) - 1
			else:
				index -= 1
		elif key == curses.KEY_ENTER or key == 10 or key == 13:
			height, width = screen.getmaxyx()

			if ''.join([str(x) for x in number]) == '1997':
				text = 'PASSCODE CORRECT!'
			else:
				text = 'PASSCODE INCORRECT!'

			screen.clear()
			screen.addstr(height // 2, width // 2 - len(text) // 2, text)
			text = 'Press any key to continue . . .'
			screen.addstr(height // 2 + 1, width // 2 - len(text) // 2, text)
			screen.refresh()
			screen.getch()

			program_loop = False
			break

		display(screen)

curses.wrapper(main)
