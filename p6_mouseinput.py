import curses

def main(screen):
	curses.curs_set(0)

	# Use mouse mask to tell curses what mouse input to detect
	curses.mousemask(curses.BUTTON1_PRESSED|curses.REPORT_MOUSE_POSITION)

	while True:
		# Get input (mouse click will also be included in getch)
		key = screen.getch()

		if key == curses.KEY_MOUSE:
			
			# Get data from mouse
			_, mouseX, mouseY, _, _ = curses.getmouse()
			screen.addstr(0, 0, 'Click detected at {}, {}'.format(mouseX, mouseY))
			screen.refresh()

		elif key == ord('q'):
			break

curses.wrapper(main)