import pygame, sys, random
from Bird import Bird
import functionality


pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# SETTINGS

is_running = True
game_state = True
game_speed = 1400
create_pipe_timer = 200 # TIMER 5 seconds

# VARIBLES
player = Bird(screen, 100, 100, 10, (255, 255, 255))
pipes = []

while is_running:
	screen.fill((25, 25, 25))
	create_pipe_timer -= 1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.jump()

# ===========================================================

	if game_state:
		if functionality.floor_collision(player, SCREEN_HEIGHT):
			is_running = False

		if functionality.pipe_collision(player, pipes):
			is_running = False

		functionality.top_collision(player)

		player.update()

		#[CREATE PIPE]
		if create_pipe_timer <= 0:
			functionality.create_pipe(screen, pipes, game_state, SCREEN_WIDTH, SCREEN_HEIGHT)
			create_pipe_timer = game_speed / 2

		#[UPDATE PIPE] 
		for pipe in pipes:
			pipe.update()

		#[DELETE PIPE]
		functionality.delete_pipe(pipes)

	else:
		if len(pipes) > 0:
			pipes = []

	pygame.display.flip()
	clock.tick(game_speed)

