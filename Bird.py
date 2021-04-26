import pygame

class Bird():
	def __init__(self, screen, posX, posY, radius, color):
		self.screen = screen
		self.posX = posX
		self.posY = posY
		self.radius = radius
		self.color = color

		self.vel = 0
		self.gravity = 0.01

	def draw(self):
		pygame.draw.circle(self.screen, self.color, (self.posX, self.posY), self.radius)

	def update(self):

		if self.vel >= 3:
			self.vel = 3
		else:
			self.vel += self.gravity


		self.posY += self.vel

		self.draw()

	def jump(self):
		self.vel = -1.5