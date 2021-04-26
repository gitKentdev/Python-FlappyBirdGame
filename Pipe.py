import pygame

class Pipe():
	def __init__(self, screen, posX, posY, width, height, color):
		self.screen = screen
		self.posX = posX
		self.posY = posY
		self.width = width
		self.height = height
		self.color = color

		self.vel = 0.5

	def draw(self):
		pygame.draw.rect(self.screen, self.color, pygame.Rect(self.posX, self.posY, self.width, self.height))

	def update(self):
		self.posX -= self.vel
		self.draw()