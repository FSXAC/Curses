#!/usr/bin/env python

import curses
import math
import random

sim_life = 100
sim_max_start_speed = 2

class PhysConsts:
	def __init__(self, g=0.1, bounce_rx=0.5, bounce_ry=0.25, start_rand=2):
		self.g = g
		self.bounce_rx = bounce_rx
		self.bounce_ry = bounce_ry
		self.start_rand = 2
		self.sim_scaling = 1

class Particle:
	def __init__(self, screen, x, y, phys):
		self.screen = screen
		self.phys = phys
		self.x = x + random.randint(-self.phys.start_rand, self.phys.start_rand)
		self.y = y + random.randint(-self.phys.start_rand, self.phys.start_rand)
		self.char = random.choice('*#.-`~@&+<>"')
		t = random.uniform(0, 6.28)
		m = random.uniform(0, sim_max_start_speed)
		self.vx = m * math.cos(t)
		self.vy = m * math.sin(t)
		self.life = sim_life

	def draw(self):
		try:
			self.screen.addstr(int(round(self.y, 0)), int(round(self.x, 0)), self.char)
		except Exception:
			pass

	def update(self):
		self.x += self.vx * self.phys.sim_scaling
		self.y += self.vy * self.phys.sim_scaling

		self.vy += self.phys.g * self.phys.sim_scaling

		height, width = self.screen.getmaxyx()
		if self.x <= 0:
			self.x = 0
			self.vx *= -self.phys.bounce_rx
		elif self.x >= width - 1:
			self.x = width - 2
			self.vx *= -self.phys.bounce_rx
		
		if self.y <= 0:
			self.y = 0
			self.vy *= -self.phys.bounce_ry
		elif self.y >= height - 1:
			self.y = height - 1
			self.vy *= -self.phys.bounce_ry

		# friction
		if self.y == height - 1:
			self.vx *= 0.6 * self.phys.sim_scaling

		self.life -= 1 * self.phys.sim_scaling

class ParticleSystem:
	def __init__(self, screen, x, y, phys):
		self.screen = screen
		self.x = x
		self.y = y
		self.particles = list()
		self.phys = phys

	def draw(self):
		for p in self.particles:
			p.draw()

	def update(self):
		to_delete = list()
		for p in self.particles:
			p.update()

			if p.life <= 0:
				to_delete.append(p)
			
		for p in to_delete:
			self.particles.remove(p)

		self.particles.append(Particle(self.screen, self.x, self.y, self.phys))

def main(screen):

	curses.mousemask(curses.BUTTON1_PRESSED)

	curses.curs_set(0)
	screen.nodelay(True)

	height, width = screen.getmaxyx()
	phys = PhysConsts()
	ps = ParticleSystem(screen, width // 2, height // 2, phys)

	sim_paused = False

	while True:

		# Get key input
		key = screen.getch()
		screen.clear()

		if key == ord('q'):
			break
		elif key == curses.KEY_UP:
			phys.g -= 0.05
		elif key == curses.KEY_DOWN:
			phys.g += 0.05
		elif key == curses.KEY_LEFT and phys.sim_scaling > 0.1:
			phys.sim_scaling -= 0.1
		elif key == curses.KEY_RIGHT and phys.sim_scaling < 2:
			phys.sim_scaling += 0.1
		elif key == ord('p'):
			sim_paused = not sim_paused
		# elif key == curses.KEY_MOUSE:
		# 	# Get data from mouse
		# 	_, mouseX, mouseY, _, _ = curses.getmouse()

		ps.draw()

		# Draw phys param data
		screen.addstr(0, 0, 'gravity : {}'.format(round(phys.g, 2)))
		screen.addstr(1, 0, 'sim rate: {}%'.format(round(phys.sim_scaling * 100)))

		if not sim_paused:
			ps.update()
			screen.refresh()

curses.wrapper(main)
