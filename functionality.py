from Pipe import Pipe
import time, random

def floor_collision(player, SCREEN_HEIGHT):
	if player.posY + player.radius >= SCREEN_HEIGHT:
		return True

def pipe_collision(player, pipes):
	for pipe in pipes:
		if player.posX + player.radius >= pipe.posX and player.posX - player.radius <= pipe.posX + pipe.width:
			if player.posY - player.radius >= pipe.posY and player.posY + player.radius <= pipe.posY + pipe.height:
				return True

def top_collision(player):
	if player.posY - player.radius <= 0:
		player.posY = player.radius
		player.vel = 0

def create_pipe(screen, pipes, game_state, SCREEN_WIDTH, SCREEN_HEIGHT):
	random_height = random.choice([250, 350, 450])
	pipes.append(Pipe(screen, SCREEN_WIDTH + 100, 0, 40, random_height, (255, 255, 255)))
	pipes.append(Pipe(screen, SCREEN_WIDTH + 100, random_height + 150, 40, SCREEN_HEIGHT, (255, 255, 255)))

def delete_pipe(pipes):
	for pipe in pipes:
		if pipe.posX <= -100:
			pipes.pop(pipes.index(pipe))


